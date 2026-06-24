#!/usr/bin/env python3
"""Derive the deterministic 1-5 score from six explicit subscores."""

from __future__ import annotations

import argparse
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

from common import CONFIG_PATH, ContractError, atomic_write_json, load_json, validate_artifact, validate_path
from lab_notebook import log_event
from verification_evidence import access_class, confirmed_metadata, strict_verified

SUBSCORE_FIELDS = (
    "geographic_completeness",
    "scenario_richness",
    "technical_accessibility",
    "documentation_currency",
    "licensing",
    "integration_effort",
)


def derive_score(subscores: dict[str, int]) -> dict[str, object]:
    missing = set(SUBSCORE_FIELDS) - set(subscores)
    extra = set(subscores) - set(SUBSCORE_FIELDS)
    if missing or extra:
        raise ContractError(f"invalid subscore fields; missing={sorted(missing)}, extra={sorted(extra)}")
    if any(not isinstance(value, int) or isinstance(value, bool) or not 1 <= value <= 5 for value in subscores.values()):
        raise ContractError("all subscores must be integers from 1 to 5")

    mean = sum(Decimal(value) for value in subscores.values()) / Decimal(len(SUBSCORE_FIELDS))
    rounded = int(mean.quantize(Decimal("1"), rounding=ROUND_HALF_UP))
    gates: list[str] = []
    critical = ("geographic_completeness", "technical_accessibility", "licensing")
    if any(subscores[field] <= 2 for field in critical):
        rounded = min(rounded, 3)
        gates.append("critical_factor_cap_3")
    award_five = (
        all(subscores[field] >= 4 for field in (*critical, "documentation_currency"))
        and min(subscores.values()) >= 3
    )
    if rounded == 5 and not award_five:
        rounded = 4
        gates.append("score_5_readiness_gate")
    return {"mean": float(mean), "score": rounded, "gates": gates}


def _applicable_families(country: dict) -> set[str]:
    required = set(load_json(CONFIG_PATH)["hazard_families_required"]["families"])
    summary = country["fragmentation_summary"].lower()
    for family in tuple(required):
        family_pattern = re.escape(family).replace("_", r"[-_ ]")
        pattern = rf"{family_pattern}[^.;]{{0,120}}\b(?:n/?a|not applicable)\b"
        if re.search(pattern, summary):
            required.remove(family)
    return required


def evidence_subscores(country: dict) -> tuple[dict[str, int], str, dict[str, object]]:
    material = [
        source
        for source in country["sources"]
        if source["is_material"] and not source["is_fallback"] and strict_verified(source)
    ]
    applicable = _applicable_families(country)
    families = {
        family
        for source in material
        for family in confirmed_metadata(source).get("flood_types") or []
    }
    missing = sorted(applicable - families)
    if not material:
        geographic = 1
    elif not missing:
        geographic = 5 if country["coverage_model"] == "nationally_unified" else 4
    elif len(missing) == 1:
        geographic = 3
    else:
        geographic = 2

    scenarios = {
        str(scenario).lower()
        for source in material
        for scenario in confirmed_metadata(source).get("scenarios") or []
    }
    metadata_text = " ".join(scenarios)
    if not material:
        scenario_score = 1
    elif not scenarios:
        scenario_score = 2
    elif len(scenarios) < 3:
        scenario_score = 3
    elif len(scenarios) < 5:
        scenario_score = 4
    else:
        scenario_score = 5 if re.search(
            r"depth|velocity|climate|future|extreme", metadata_text
        ) else 4

    access_scores = {
        "service": 5,
        "api": 5,
        "download": 5,
        "viewer": 4,
        "document": 3,
        "dataset_page": 3,
    }
    technical = max((access_scores.get(access_class(source), 1) for source in material), default=1)

    dates = [
        confirmed_metadata(source).get("last_update")
        for source in material
        if confirmed_metadata(source).get("last_update")
    ]
    documentation = 2 if not dates else (4 if len(dates) == len(material) else 3)

    licences = [
        confirmed_metadata(source).get("license")
        for source in material
        if confirmed_metadata(source).get("license")
    ]
    licensing = 2 if not licences else (4 if len(licences) == len(material) else 3)

    if not material:
        integration = 1
    elif country["coverage_model"] == "nationally_unified":
        integration = 4
    elif country["coverage_model"] == "national_catalogue_with_regional_publishers":
        integration = 3
    else:
        integration = 2

    subscores = {
        "geographic_completeness": geographic,
        "scenario_richness": scenario_score,
        "technical_accessibility": technical,
        "documentation_currency": documentation,
        "licensing": licensing,
        "integration_effort": integration,
    }
    confidence = (
        "high"
        if geographic >= 4 and technical >= 4 and documentation >= 3
        else "medium"
        if material and geographic >= 3
        else "low"
    )
    evidence = {
        "applicable_families": sorted(applicable),
        "confirmed_families": sorted(families),
        "missing_families": missing,
        "strict_material_source_ids": [source["id"] for source in material],
    }
    return subscores, confidence, evidence


def enforce_evidence_caps(country: dict, subscores: dict[str, int]) -> dict[str, int]:
    caps, _, _ = evidence_subscores(country)
    exceeded = {
        field: {"submitted": value, "cap": caps[field]}
        for field, value in subscores.items()
        if value > caps[field]
    }
    if exceeded:
        raise ContractError(f"subscores exceed confirmed-evidence caps: {exceeded}")
    return caps


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("country")
    parser.add_argument("--subscores", help="JSON object; defaults to country.subscores")
    parser.add_argument("--confidence", choices=["high", "medium", "low"])
    parser.add_argument(
        "--from-evidence",
        action="store_true",
        help="derive subscores and confidence from strict verification evidence",
    )
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--actor", choices=["claude_code"])
    args = parser.parse_args()
    try:
        country = validate_path(args.country)
        evidence_details: dict[str, object] = {}
        if args.from_evidence:
            subscores, derived_confidence, evidence_details = evidence_subscores(country)
        else:
            subscores = json.loads(args.subscores) if args.subscores else country["subscores"]
            derived_confidence = args.confidence
        if subscores is None:
            raise ContractError("subscores are required")
        enforce_evidence_caps(country, subscores)
        result = derive_score(subscores)
        result["score_provisional"] = bool(country["deferred_regions"])
        result["evidence"] = evidence_details
        if args.write:
            if args.actor != "claude_code":
                raise ContractError("--write requires --actor claude_code")
            confidence = args.confidence or derived_confidence or country["confidence"]
            if confidence is None:
                raise ContractError("--write requires --confidence for an unscored country")
            country.update(
                {
                    "subscores": subscores,
                    "score": result["score"],
                    "confidence": confidence,
                    "score_provisional": result["score_provisional"],
                }
            )
            validate_artifact(country)
            atomic_write_json(args.country, country)
            log_event(
                "claude_code",
                "score",
                f"Derived country score {result['score']}/5 from explicit subscores.",
                iso2=country["iso2"],
                details={
                    "subscores": subscores,
                    "mean": result["mean"],
                    "gates": result["gates"],
                    "confidence": confidence,
                    "score_provisional": result["score_provisional"],
                },
            )
        print(json.dumps(result, sort_keys=True))
        return 0
    except (ContractError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env python3
"""Verify sources against the dataset-resolved evidence standard."""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from pathlib import Path
from typing import Any

from common import (
    ContractError,
    atomic_write_json,
    load_json,
    utc_now,
    validate_artifact,
    validate_path,
)
from lab_notebook import log_event
from probe_capabilities import ProbeError, probe_url
from validate_url import validate_url
from verification_evidence import (
    ALL_ACCESS_CLASSES,
    CONFIRMED_ACCESS_CLASSES,
    STANDARD,
)

FLOOD_LAYER_PATTERN = re.compile(
    r"(flood|inund|hazard|risk|depth|velocity|waterlog|stormwater|surface.?water|"
    r"fluvial|coastal|pluvial|high.?water|hochwasser|überschw|ueberschw|"
    r"starkregen|geschwindigkeit|wassertiefe|overstrom|alluv|powodzi|banjir|"
    r"tuilte|kouzui|shinsui|침수|홍수|洪水|淹没|"
    r"น้ำท่วม|inondazione|inundação|inundacion)",
    re.IGNORECASE,
)
HTML_TYPES = {"text/html", "application/xhtml+xml"}


def _successful(result: dict[str, Any]) -> bool:
    status = result.get("http_status")
    return isinstance(status, int) and 200 <= status < 400


def _bounded_link_result(result: dict[str, Any]) -> dict[str, Any]:
    return {
        key: result.get(key)
        for key in (
            "http_status",
            "content_type",
            "final_url",
            "bytes",
            "range_honored",
            "error",
        )
    }


def _probe_evidence(probe: dict[str, Any]) -> dict[str, Any]:
    return {
        "service_type": probe.get("service_type"),
        "layer_count": probe.get("layer_count"),
        "layers_truncated": probe.get("layers_truncated")
        or len(probe.get("layers") or []) > 25,
        "layers": (probe.get("layers") or [])[:25],
        "crs": (probe.get("crs") or [])[:20],
        "formats": (probe.get("formats") or [])[:20],
        "bbox": probe.get("bbox"),
        "declared_update": probe.get("declared_update"),
    }


def _service_is_relevant(capabilities: dict[str, Any]) -> bool:
    text = " ".join(str(item) for item in capabilities.get("layers") or [])
    return bool(FLOOD_LAYER_PATTERN.search(text))


def _download_is_data(result: dict[str, Any]) -> bool:
    content_type = (result.get("content_type") or "").split(";", 1)[0].lower()
    if content_type in HTML_TYPES:
        return False
    return content_type.startswith(
        (
            "application/",
            "image/tiff",
            "text/csv",
            "application/geo+json",
        )
    )


def _empty_confirmed() -> dict[str, Any]:
    return {
        "flood_types": [],
        "scenarios": [],
        "coverage": None,
        "formats": [],
        "license": None,
        "last_update": None,
    }


def _normalize_audit(audit: dict[str, Any] | None) -> dict[str, Any]:
    audit = copy.deepcopy(audit or {})
    audit.setdefault("outcome", "lead")
    audit.setdefault("access_class", "ambiguous")
    audit.setdefault("authority_confirmed", False)
    audit.setdefault("dataset_identity_confirmed", False)
    audit.setdefault("human_usable", False)
    audit.setdefault("selected_role", None)
    audit.setdefault("selected_url", None)
    audit.setdefault("confirmed", _empty_confirmed())
    audit.setdefault("reason", "No dataset-resolved audit evidence was supplied.")
    confirmed = audit["confirmed"]
    for key, default in _empty_confirmed().items():
        confirmed.setdefault(key, copy.deepcopy(default))
    if audit["access_class"] not in ALL_ACCESS_CLASSES:
        raise ContractError(f"invalid access_class {audit['access_class']!r}")
    if audit["outcome"] not in {"confirmed", "lead", "unavailable"}:
        raise ContractError(f"invalid audit outcome {audit['outcome']!r}")
    if audit["selected_role"] not in {"primary", "service", "download", None}:
        raise ContractError(f"invalid selected_role {audit['selected_role']!r}")
    return audit


def _failed_verification(
    *,
    audit: dict[str, Any],
    link_results: dict[str, dict[str, Any]],
    checked_at: str,
    selected: dict[str, Any] | None = None,
    capabilities: dict[str, Any] | None = None,
) -> dict[str, Any]:
    selected = selected or next(iter(link_results.values()), {})
    evidence = {
        "standard": STANDARD,
        "outcome": audit["outcome"],
        "access_class": audit["access_class"],
        "authority_confirmed": bool(audit["authority_confirmed"]),
        "dataset_identity_confirmed": bool(audit["dataset_identity_confirmed"]),
        "human_usable": bool(audit["human_usable"]),
        "selected_role": audit["selected_role"],
        "selected_url": audit["selected_url"],
        "confirmed": audit["confirmed"],
        "reason": str(audit["reason"])[:1000],
        "links": link_results,
    }
    if audit.get("browser"):
        evidence["browser"] = audit["browser"]
    if capabilities:
        evidence["capabilities"] = capabilities
    return {
        "status": "failed",
        "http_status": selected.get("http_status"),
        "content_type": selected.get("content_type"),
        "final_url": selected.get("final_url"),
        "evidence": evidence,
        "checked_at": checked_at,
        "checked_by": "claude_code",
    }


def verify_source(
    source: dict[str, Any],
    timeout: float = 30.0,
    audit: dict[str, Any] | None = None,
) -> tuple[dict[str, Any], str | None]:
    audit = _normalize_audit(audit)
    link_results: dict[str, dict[str, Any]] = {}
    for role in ("primary", "service", "download"):
        url = source["links"].get(role)
        if url:
            link_results[role] = _bounded_link_result(validate_url(url, timeout))

    checked_at = utc_now()
    successful_roles = {
        role for role, result in link_results.items() if _successful(result)
    }
    if not successful_roles:
        audit.update(
            {
                "outcome": "unavailable",
                "access_class": "unavailable",
                "human_usable": False,
                "selected_role": None,
                "selected_url": None,
            }
        )
        if audit["reason"] == "No dataset-resolved audit evidence was supplied.":
            audit["reason"] = "No candidate link resolved successfully."
        return (
            _failed_verification(
                audit=audit, link_results=link_results, checked_at=checked_at
            ),
            None,
        )

    selected_role = audit["selected_role"]
    if selected_role is None and audit["outcome"] == "confirmed":
        selected_role = next(
            (role for role in ("service", "download", "primary") if role in successful_roles),
            None,
        )
        audit["selected_role"] = selected_role
    if selected_role:
        candidate_url = source["links"].get(selected_role)
        if not candidate_url:
            raise ContractError(
                f"{source['id']}: selected role {selected_role} has no candidate URL"
            )
        selected_result = link_results[selected_role]
        audit["selected_url"] = selected_result.get("final_url") or candidate_url
    else:
        selected_result = next(
            (link_results[role] for role in ("primary", "service", "download") if role in successful_roles),
            next(iter(link_results.values())),
        )

    capabilities = None
    raw_probe = None
    declared_update = None
    service_url = source["links"].get("service")
    if service_url and "service" in successful_roles:
        try:
            raw_probe = probe_url(service_url, timeout)
            capabilities = _probe_evidence(raw_probe)
            declared_update = raw_probe.get("declared_update")
        except ProbeError as exc:
            if audit["outcome"] == "confirmed" and selected_role == "service":
                audit.update(
                    {
                        "outcome": "lead",
                        "access_class": "ambiguous",
                        "dataset_identity_confirmed": False,
                        "human_usable": False,
                        "reason": f"Service capability probe failed: {str(exc)[:500]}",
                    }
                )

    if audit["outcome"] == "confirmed":
        problems: list[str] = []
        if audit["access_class"] not in CONFIRMED_ACCESS_CLASSES:
            problems.append("access class is not dataset-resolved")
        if not audit["authority_confirmed"]:
            problems.append("publisher authority is unconfirmed")
        if not audit["dataset_identity_confirmed"]:
            problems.append("dataset identity is unconfirmed")
        if not audit["human_usable"]:
            problems.append("human usability is unconfirmed")
        if selected_role not in successful_roles:
            problems.append("selected link did not resolve")
        if selected_role == "service":
            if not capabilities:
                problems.append("service capabilities were not confirmed")
            elif not _service_is_relevant(raw_probe or capabilities):
                problems.append("service exposes no recognizably flood-related layers")
        if selected_role == "download" and not _download_is_data(selected_result):
            problems.append("download resolved to HTML or a non-data response")
        if selected_role == "primary" and audit["access_class"] in {
            "viewer",
            "document",
            "dataset_page",
        } and not audit.get("browser"):
            problems.append("page-based access lacks browser audit evidence")
        if problems:
            audit.update(
                {
                    "outcome": "lead",
                    "human_usable": False,
                    "reason": "; ".join(problems),
                }
            )

    if audit["outcome"] != "confirmed":
        if audit["outcome"] == "unavailable":
            audit["access_class"] = "unavailable"
        return (
            _failed_verification(
                audit=audit,
                link_results=link_results,
                checked_at=checked_at,
                selected=selected_result,
                capabilities=capabilities,
            ),
            None,
        )

    evidence = {
        "standard": STANDARD,
        "outcome": "confirmed",
        "access_class": audit["access_class"],
        "authority_confirmed": True,
        "dataset_identity_confirmed": True,
        "human_usable": True,
        "selected_role": selected_role,
        "selected_url": audit["selected_url"],
        "confirmed": audit["confirmed"],
        "reason": str(audit["reason"])[:1000],
        "links": link_results,
    }
    if audit.get("browser"):
        evidence["browser"] = audit["browser"]
    if capabilities:
        evidence["capabilities"] = capabilities
    selected = link_results[selected_role]
    return (
        {
            "status": "verified",
            "http_status": selected["http_status"],
            "content_type": selected["content_type"],
            "final_url": selected["final_url"],
            "evidence": evidence,
            "checked_at": checked_at,
            "checked_by": "claude_code",
        },
        str(declared_update) if declared_update is not None else audit["confirmed"]["last_update"],
    )


def verify_country(
    country: dict[str, Any],
    timeout: float = 30.0,
    *,
    audits: dict[str, Any] | None = None,
    reverify: bool = False,
) -> dict[str, Any]:
    updated = copy.deepcopy(country)
    audits = audits or {}
    for source in updated["sources"]:
        if source["verification"]["status"] == "superseded":
            continue
        if not reverify and source["verification"]["status"] != "unverified":
            continue
        verification, declared_update = verify_source(
            source, timeout, audits.get(source["id"])
        )
        source["verification"] = verification
        if declared_update is not None:
            source["last_update"] = str(declared_update)
    validate_artifact(updated)
    return updated


def verification_delta(
    original: dict[str, Any], updated: dict[str, Any]
) -> dict[str, Any]:
    before = {source["id"]: source for source in original["sources"]}
    changes: dict[str, Any] = {}
    for source in updated["sources"]:
        previous = before[source["id"]]
        if (
            source["verification"] != previous["verification"]
            or source["last_update"] != previous["last_update"]
        ):
            changes[source["id"]] = {
                "verification": source["verification"],
                "last_update": source["last_update"],
            }
    return {
        "schema_version": original["schema_version"],
        "actor": "claude_code",
        "iso2": original["iso2"],
        "append_sources": [],
        "country_updates": {},
        "source_verification": changes,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("country")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--audit", help="JSON object keyed by source ID")
    parser.add_argument("--reverify", action="store_true")
    parser.add_argument("--delta-output")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--actor", choices=["claude_code"])
    args = parser.parse_args()
    try:
        if (args.write or args.delta_output) and args.actor != "claude_code":
            raise ContractError("writes require --actor claude_code")
        if args.write and args.reverify:
            raise ContractError(
                "terminal re-verification must use --delta-output and tools/apply_delta.py"
            )
        country = validate_path(args.country)
        audits = load_json(args.audit) if args.audit else {}
        updated = verify_country(
            country, args.timeout, audits=audits, reverify=args.reverify
        )
        if args.delta_output:
            atomic_write_json(args.delta_output, verification_delta(country, updated))
        if args.write:
            atomic_write_json(args.country, updated)
        if args.write:
            old_statuses = {
                source["id"]: source["verification"]["status"]
                for source in country["sources"]
            }
            for source in updated["sources"]:
                if old_statuses.get(source["id"]) != source["verification"]["status"]:
                    log_event(
                        "claude_code",
                        "verification",
                        "Dataset-resolved verification completed with status "
                        f"{source['verification']['status']}.",
                        iso2=updated["iso2"],
                        source_id=source["id"],
                        details={
                            "http_status": source["verification"]["http_status"],
                            "content_type": source["verification"]["content_type"],
                            "final_url": source["verification"]["final_url"],
                            "checked_at": source["verification"]["checked_at"],
                            "access_class": source["verification"]["evidence"][
                                "access_class"
                            ],
                            "outcome": source["verification"]["evidence"]["outcome"],
                        },
                    )
        counts: dict[str, int] = {}
        for source in updated["sources"]:
            status = source["verification"]["status"]
            counts[status] = counts.get(status, 0) + 1
        print(json.dumps(counts, sort_keys=True))
        return 0
    except (ContractError, OSError, ValueError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

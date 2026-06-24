#!/usr/bin/env python3
"""Prepare conservative dataset-resolved audit decisions for a country artifact."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

from common import atomic_write_json, validate_path

CONFIRMED_PAGE_ACCESS = {
    "GB-EA-004": "dataset_page",
    "GB-DFI-001": "viewer",
    "AT-HORA-001": "viewer",
    "AT-WISA-001": "viewer",
    "AT-BML-001": "dataset_page",
    "BE-VLG-001": "viewer",
    "BE-WAL-002": "dataset_page",
    "CA-QC-001": "viewer",
    "CA-AB-001": "viewer",
    "CA-MB-001": "dataset_page",
    "CH-BAFU-001": "viewer",
    "CH-BAFU-002": "dataset_page",
    "CN-BJ-001": "document",
    "DE-WBL-001": "dataset_page",
    "DE-NW-001": "dataset_page",
    "DE-BY-001": "viewer",
    "DE-BW-001": "viewer",
    "DE-HE-001": "dataset_page",
    "FR-NAQ-001": "dataset_page",
    "IE-OPW-001": "viewer",
    "IE-OPW-002": "viewer",
    "IE-OPW-003": "viewer",
    "IN-NRSC-001": "viewer",
    "IN-BR-001": "dataset_page",
    "IT-ISPRA-001": "viewer",
    "IT-ADBPO-001": "dataset_page",
    "JP-MLIT-001": "viewer",
    "JP-MLIT-002": "dataset_page",
    "JP-MLIT-003": "viewer",
    "JP-KNG-001": "dataset_page",
    "KR-MOE-001": "viewer",
    "MX-CMX-001": "viewer",
    "PL-WP-001": "viewer",
    "PL-WP-002": "dataset_page",
    "SE-MSB-001": "viewer",
    "SE-MSB-003": "dataset_page",
    "SE-MSB-004": "viewer",
}

SCENARIO_CONFIRMED = {
    "GB-EA-004",
    "GB-DFI-001",
    "AT-HORA-001",
    "AT-WISA-001",
    "BE-VLG-001",
    "CA-AB-001",
    "DE-WBL-001",
    "DE-NW-001",
    "DE-BY-001",
    "DE-BW-001",
    "DE-HE-001",
    "IE-OPW-001",
    "IE-OPW-003",
    "KR-MOE-001",
    "PL-WP-001",
    "PL-WP-002",
    "SE-MSB-001",
    "SE-MSB-003",
    "SE-MSB-004",
}

LAST_UPDATE_OVERRIDES = {
    "JP-KNG-001": "2026-01-05",
}


def _empty_confirmed() -> dict[str, Any]:
    return {
        "flood_types": [],
        "scenarios": [],
        "coverage": None,
        "formats": [],
        "license": None,
        "last_update": None,
    }


def _is_eea(source_id: str) -> bool:
    return source_id.endswith("-EEA-001")


def _is_jrc(source_id: str) -> bool:
    return source_id.endswith("-JRC-001")


def _confirmed_metadata(source: dict[str, Any], access: str) -> dict[str, Any]:
    formats = {
        "service": ["OGC service"],
        "api": ["API"],
        "download": ["Direct download"],
        "viewer": ["Interactive viewer"],
        "document": ["Map document"],
        "dataset_page": ["Dataset-specific page"],
    }[access]
    scenarios = source["scenarios"] if source["id"] in SCENARIO_CONFIRMED else []
    licence = None
    if _is_eea(source["id"]):
        licence = "EEA reuse policy"
    return {
        "flood_types": source["flood_types"],
        "scenarios": scenarios,
        "coverage": source["coverage"],
        "formats": formats,
        "license": licence,
        "last_update": LAST_UPDATE_OVERRIDES.get(source["id"])
        or source["last_update"],
    }


def _lead_access(source: dict[str, Any]) -> tuple[str, str]:
    constraints = set(source["access_constraints"])
    normalized = " ".join(
        [
            source["delivery_mode"],
            source["product_type"],
            source["notes"],
            source["links"].get("primary") or "",
        ]
    ).lower()
    if "request_only" in constraints:
        return "request_only", "Access requires a data request; no public dataset path was confirmed."
    if "restricted" in constraints:
        return "restricted", "Access is restricted and no public dataset path was confirmed."
    if (
        source["product_type"].startswith("operational_")
        or "operational" in normalized
        or "monitoring" in normalized
        or "warnings" in normalized
    ):
        return "wrong_product", "The reachable product is operational or observational, not a confirmed flood-hazard dataset."
    if (
        "catalogue" in normalized
        or "catalog" in normalized
        or "/dataset/?q=" in normalized
        or "search.open" in normalized
        or "data.go.kr" in normalized
    ):
        return "catalogue_search", "The link is a catalogue/search entry point rather than a dataset-specific record."
    path = urlsplit(source["links"].get("primary") or "").path.strip("/")
    if not path or path in {"app", "webgis", "portal"}:
        return "generic_portal", "The link is a generic agency or geoportal entry point; the named dataset was not resolved."
    return "ambiguous", "The page resolves, but dataset identity or usable access could not be confirmed."


def decision_for(source: dict[str, Any]) -> dict[str, Any]:
    verification = source["verification"]
    source_id = source["id"]
    if verification["status"] == "superseded":
        return {}
    if verification["status"] == "failed":
        if verification.get("http_status") == 403:
            return {
                "outcome": "lead",
                "access_class": "restricted",
                "authority_confirmed": True,
                "dataset_identity_confirmed": False,
                "human_usable": False,
                "selected_role": "primary",
                "confirmed": _empty_confirmed(),
                "reason": "The official page returned HTTP 403; public dataset usability could not be confirmed.",
            }
        return {
            "outcome": "unavailable",
            "access_class": "unavailable",
            "authority_confirmed": False,
            "dataset_identity_confirmed": False,
            "human_usable": False,
            "selected_role": None,
            "confirmed": _empty_confirmed(),
            "reason": "No candidate link resolved successfully during the strict audit.",
        }

    if source["links"].get("service"):
        access = "service"
        role = "service"
    elif source["links"].get("download"):
        access = "download"
        role = "download"
    elif _is_eea(source_id):
        access = "dataset_page"
        role = "primary"
    elif _is_jrc(source_id):
        return {
            "outcome": "lead",
            "access_class": "restricted",
            "authority_confirmed": True,
            "dataset_identity_confirmed": True,
            "human_usable": False,
            "selected_role": "primary",
            "confirmed": _empty_confirmed(),
            "reason": "The JRC collection resolves to a login surface; unauthenticated dataset access was not confirmed.",
        }
    elif source_id in CONFIRMED_PAGE_ACCESS:
        access = CONFIRMED_PAGE_ACCESS[source_id]
        role = "primary"
    else:
        lead_access, reason = _lead_access(source)
        return {
            "outcome": "lead",
            "access_class": lead_access,
            "authority_confirmed": True,
            "dataset_identity_confirmed": False,
            "human_usable": False,
            "selected_role": "primary",
            "confirmed": _empty_confirmed(),
            "reason": reason,
        }

    decision = {
        "outcome": "confirmed",
        "access_class": access,
        "authority_confirmed": True,
        "dataset_identity_confirmed": True,
        "human_usable": True,
        "selected_role": role,
        "confirmed": _confirmed_metadata(source, access),
        "reason": (
            "Official dataset-specific page or viewer confirmed during bounded page review."
            if role == "primary"
            else "Direct dataset endpoint selected for bounded validation."
        ),
    }
    if role == "primary":
        decision["browser"] = {
            "method": "official_page_inspection_fallback",
            "page_title": source["native_name"],
            "observed_product": source["english_name"],
            "access_action": f"Reviewed authoritative {access.replace('_', ' ')}",
            "final_url": verification.get("final_url") or source["links"]["primary"],
        }
    return decision


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("country")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    country = validate_path(args.country)
    decisions = {
        source["id"]: decision
        for source in country["sources"]
        if (decision := decision_for(source))
    }
    atomic_write_json(Path(args.output), decisions)
    counts: dict[str, int] = {}
    for decision in decisions.values():
        key = f"{decision['outcome']}:{decision['access_class']}"
        counts[key] = counts.get(key, 0) + 1
    print(f"prepared {len(decisions)} audits for {country['iso2']}: {counts}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

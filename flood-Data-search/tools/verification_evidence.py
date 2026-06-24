"""Shared helpers for dataset-resolved verification evidence."""

from __future__ import annotations

from typing import Any

STANDARD = "dataset_resolved_v1"

CONFIRMED_ACCESS_CLASSES = {
    "service",
    "api",
    "download",
    "viewer",
    "document",
    "dataset_page",
}
REACHABLE_LEAD_ACCESS_CLASSES = {
    "request_only",
    "generic_portal",
    "catalogue_search",
    "restricted",
    "ambiguous",
    "wrong_product",
}
ALL_ACCESS_CLASSES = CONFIRMED_ACCESS_CLASSES | REACHABLE_LEAD_ACCESS_CLASSES | {
    "unavailable"
}


def evidence_for(source: dict[str, Any]) -> dict[str, Any]:
    evidence = source.get("verification", {}).get("evidence")
    return evidence if isinstance(evidence, dict) else {}


def is_strict_evidence(evidence: dict[str, Any]) -> bool:
    return evidence.get("standard") == STANDARD


def access_class(source: dict[str, Any]) -> str:
    evidence = evidence_for(source)
    value = evidence.get("access_class")
    return value if value in ALL_ACCESS_CLASSES else "ambiguous"


def outcome(source: dict[str, Any]) -> str:
    evidence = evidence_for(source)
    value = evidence.get("outcome")
    return value if value in {"confirmed", "lead", "unavailable"} else "lead"


def confirmed_metadata(source: dict[str, Any]) -> dict[str, Any]:
    confirmed = evidence_for(source).get("confirmed")
    return confirmed if isinstance(confirmed, dict) else {}


def strict_verified(source: dict[str, Any]) -> bool:
    evidence = evidence_for(source)
    return (
        source.get("verification", {}).get("status") == "verified"
        and is_strict_evidence(evidence)
        and evidence.get("outcome") == "confirmed"
        and evidence.get("access_class") in CONFIRMED_ACCESS_CLASSES
        and evidence.get("authority_confirmed") is True
        and evidence.get("dataset_identity_confirmed") is True
        and evidence.get("human_usable") is True
        and bool(evidence.get("selected_url"))
    )


def reachable_lead(source: dict[str, Any]) -> bool:
    evidence = evidence_for(source)
    return (
        source.get("verification", {}).get("status") == "failed"
        and is_strict_evidence(evidence)
        and evidence.get("outcome") == "lead"
    )


def unavailable(source: dict[str, Any]) -> bool:
    evidence = evidence_for(source)
    return (
        source.get("verification", {}).get("status") == "failed"
        and (
            not is_strict_evidence(evidence)
            or evidence.get("outcome") == "unavailable"
        )
    )


def semantic_errors(source: dict[str, Any], prefix: str) -> list[str]:
    verification = source["verification"]
    if verification["status"] == "unverified":
        return []
    if verification["status"] == "superseded":
        evidence = evidence_for(source)
        return (
            []
            if evidence.get("replacement_id") or evidence.get("superseded_by")
            else [f"{prefix}.verification.evidence: superseded source lacks replacement_id"]
        )
    evidence = evidence_for(source)
    if not is_strict_evidence(evidence):
        return [f"{prefix}.verification.evidence: missing {STANDARD} evidence"]

    errors: list[str] = []
    required = {
        "standard",
        "outcome",
        "access_class",
        "authority_confirmed",
        "dataset_identity_confirmed",
        "human_usable",
        "selected_role",
        "selected_url",
        "confirmed",
        "reason",
    }
    missing = required - set(evidence)
    if missing:
        errors.append(
            f"{prefix}.verification.evidence: missing fields {sorted(missing)}"
        )
        return errors
    if evidence["access_class"] not in ALL_ACCESS_CLASSES:
        errors.append(f"{prefix}.verification.evidence.access_class: invalid value")
    if evidence["outcome"] not in {"confirmed", "lead", "unavailable"}:
        errors.append(f"{prefix}.verification.evidence.outcome: invalid value")
    if evidence["selected_role"] not in {"primary", "service", "download", None}:
        errors.append(f"{prefix}.verification.evidence.selected_role: invalid value")
    confirmed = evidence["confirmed"]
    if not isinstance(confirmed, dict):
        errors.append(f"{prefix}.verification.evidence.confirmed: must be an object")
    else:
        confirmed_required = {
            "flood_types",
            "scenarios",
            "coverage",
            "formats",
            "license",
            "last_update",
        }
        missing_confirmed = confirmed_required - set(confirmed)
        if missing_confirmed:
            errors.append(
                f"{prefix}.verification.evidence.confirmed: missing fields "
                f"{sorted(missing_confirmed)}"
            )
    if verification["status"] == "verified" and not strict_verified(source):
        errors.append(
            f"{prefix}.verification: verified requires confirmed, authoritative, "
            "dataset-specific, human-usable access"
        )
    if verification["status"] == "failed" and evidence["outcome"] == "confirmed":
        errors.append(
            f"{prefix}.verification: failed status cannot have confirmed outcome"
        )
    return errors

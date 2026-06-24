#!/usr/bin/env python3
"""Apply an actor-scoped structured delta without mutating candidate fields."""

from __future__ import annotations

import argparse
import copy
import sys
from pathlib import Path
from typing import Any

from common import ContractError, atomic_write_json, load_json, validate_artifact, validate_path
from candidate_guard import guard_country
from lab_notebook import log_event

CODEX_COUNTRY_FIELDS = {
    "coverage_model",
    "fragmentation_summary",
    "top_regions",
    "deferred_regions",
    "discovery_metrics",
}
CLAUDE_COUNTRY_FIELDS = {
    "score",
    "confidence",
    "score_provisional",
    "subscores",
}
TERMINAL_STATUSES = {"verified", "failed", "superseded"}


def _validate_delta_shape(delta: dict[str, Any], actor: str, country: dict[str, Any]) -> None:
    allowed = {
        "schema_version",
        "actor",
        "iso2",
        "append_sources",
        "country_updates",
        "source_verification",
    }
    extras = set(delta) - allowed
    if extras:
        raise ContractError(f"delta has unsupported properties: {sorted(extras)}")
    if delta.get("schema_version") != country["schema_version"]:
        raise ContractError("delta schema_version does not match country artifact")
    if delta.get("actor") != actor:
        raise ContractError("delta actor does not match --actor")
    if delta.get("iso2") != country["iso2"]:
        raise ContractError("delta ISO2 does not match country artifact")


def _append_sources(country: dict[str, Any], actor: str, sources: list[dict[str, Any]]) -> None:
    existing = {source["id"] for source in country["sources"]}
    for source in sources:
        source_id = source.get("id")
        if source_id in existing:
            raise ContractError(f"source {source_id} already exists; candidate records are immutable")
        provenance = source.get("provenance") or {}
        if provenance.get("produced_by") != actor:
            raise ContractError(f"source {source_id} provenance does not match actor {actor}")
        if provenance.get("round") == 2 and not source.get("supersedes_id"):
            raise ContractError(f"round-2 source {source_id} must set supersedes_id")
        if actor == "codex" and provenance.get("round") == 2:
            if source["supersedes_id"] not in existing:
                raise ContractError(
                    f"round-2 source {source_id} supersedes unknown source "
                    f"{source['supersedes_id']}"
                )
        country["sources"].append(copy.deepcopy(source))
        existing.add(source_id)


def _update_country(country: dict[str, Any], actor: str, updates: dict[str, Any]) -> None:
    allowed = CODEX_COUNTRY_FIELDS if actor == "codex" else CLAUDE_COUNTRY_FIELDS
    disallowed = set(updates) - allowed
    if disallowed:
        raise ContractError(
            f"{actor} cannot update country fields: {sorted(disallowed)}"
        )
    if actor == "codex" and any(
        source["provenance"]["round"] == 2 for source in country["sources"]
    ) and updates:
        raise ContractError("Codex round 2 may append replacements only")
    country.update(copy.deepcopy(updates))


def _update_verification(
    country: dict[str, Any], actor: str, updates: dict[str, dict[str, Any]]
) -> None:
    if updates and actor != "claude_code":
        raise ContractError("only claude_code may update verification fields")
    by_id = {source["id"]: source for source in country["sources"]}
    for source_id, update in updates.items():
        if source_id not in by_id:
            raise ContractError(f"verification update references unknown source {source_id}")
        if set(update) - {"verification", "last_update"}:
            raise ContractError(f"verification update for {source_id} changes candidate fields")
        source = by_id[source_id]
        old_status = source["verification"]["status"]
        new_verification = update.get("verification", source["verification"])
        new_status = new_verification["status"]
        if old_status in TERMINAL_STATUSES and new_status == "unverified":
            raise ContractError(f"cannot reverse terminal source {source_id} to unverified")
        if new_status != "unverified" and new_verification.get("checked_by") != "claude_code":
            raise ContractError(f"terminal source {source_id} must be checked by claude_code")
        source["verification"] = copy.deepcopy(new_verification)
        if "last_update" in update:
            source["last_update"] = update["last_update"]


def apply_delta(country: dict[str, Any], delta: dict[str, Any], actor: str) -> dict[str, Any]:
    _validate_delta_shape(delta, actor, country)
    updated = copy.deepcopy(country)
    _append_sources(updated, actor, delta.get("append_sources", []))
    _update_country(updated, actor, delta.get("country_updates", {}))
    _update_verification(updated, actor, delta.get("source_verification", {}))
    validate_artifact(updated)
    return updated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--actor", required=True, choices=["codex", "claude_code"])
    parser.add_argument("--country", required=True)
    parser.add_argument("--delta", required=True)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        country = validate_path(args.country)
        delta = load_json(args.delta)
        updated = apply_delta(country, delta, args.actor)
        if args.dry_run:
            print(f"delta valid for {updated['iso2']}")
        else:
            atomic_write_json(args.country, updated)
            guard_country(updated, actor=args.actor, sync=True)
            log_event(
                args.actor,
                "discovery" if args.actor == "codex" else "verification",
                "Applied an actor-scoped structured delta.",
                iso2=updated["iso2"],
                details={
                    "appended_source_ids": [
                        source["id"] for source in delta.get("append_sources", [])
                    ],
                    "country_fields": sorted(delta.get("country_updates", {})),
                    "verification_source_ids": sorted(
                        delta.get("source_verification", {})
                    ),
                },
            )
            print(f"updated {args.country}")
        return 0
    except (ContractError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

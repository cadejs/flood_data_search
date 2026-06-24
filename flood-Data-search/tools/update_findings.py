#!/usr/bin/env python3
"""Claude Code-owned append/update interface for findings.json."""

from __future__ import annotations

import argparse
import sys

from common import ContractError, atomic_write_json, load_json, validate_artifact, validate_path
from lab_notebook import log_event


def apply_findings_delta(findings: dict, delta: dict, actor: str) -> dict:
    if actor != "claude_code":
        raise ContractError("only claude_code may write findings")
    allowed = {
        "schema_version",
        "actor",
        "round",
        "append_items",
        "item_updates",
        "status_updates",
    }
    extras = set(delta) - allowed
    if extras:
        raise ContractError(f"unsupported findings delta fields: {sorted(extras)}")
    if delta.get("schema_version") != findings["schema_version"]:
        raise ContractError("findings delta schema version mismatch")
    if delta.get("actor") != actor:
        raise ContractError("findings delta actor mismatch")
    if "round" in delta:
        target_round = delta["round"]
        if target_round not in {1, 2} or target_round < findings["round"] or target_round > findings["round"] + 1:
            raise ContractError(f"illegal findings round transition to {target_round}")
        findings["round"] = target_round
    existing = {(item["iso2"], item["id"]) for item in findings["items"]}
    for item in delta.get("append_items", []):
        key = (item["iso2"], item["id"])
        if key in existing:
            raise ContractError(f"only one finding per source is allowed: {item['id']}")
        if findings["round"] == 2 and item["status"] == "unresolved":
            raise ContractError("round-2 findings must be resolved or marked human_review")
        findings["items"].append(item)
        existing.add(key)
    by_key = {(item["iso2"], item["id"]): item for item in findings["items"]}
    for key, updates in delta.get("item_updates", {}).items():
        iso2, separator, source_id = key.partition(":")
        if not separator or (iso2, source_id) not in by_key:
            raise ContractError(f"unknown finding update target {key}")
        if set(updates) - {"problem", "evidence", "request"}:
            raise ContractError(f"unsupported finding update fields for {key}")
        by_key[(iso2, source_id)].update(updates)
    for key, status in delta.get("status_updates", {}).items():
        iso2, separator, source_id = key.partition(":")
        if not separator or (iso2, source_id) not in by_key:
            raise ContractError(f"unknown finding status target {key}")
        if status not in {"unresolved", "resolved", "human_review"}:
            raise ContractError(f"invalid finding status {status}")
        by_key[(iso2, source_id)]["status"] = status
    validate_artifact(findings)
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--findings", default="data/findings.json")
    parser.add_argument("--delta", required=True)
    parser.add_argument("--actor", required=True, choices=["claude_code", "codex"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        findings = validate_path(args.findings)
        delta = load_json(args.delta)
        updated = apply_findings_delta(findings, delta, args.actor)
        if not args.dry_run:
            atomic_write_json(args.findings, updated)
            for item in delta.get("append_items", []):
                log_event(
                    "claude_code",
                    "finding",
                    item["problem"],
                    iso2=item["iso2"],
                    source_id=item["id"],
                    details={
                        "request": item["request"],
                        "status": item["status"],
                        "evidence": item["evidence"],
                    },
                )
        print(f"findings valid; {len(updated['items'])} item(s)")
        return 0
    except (ContractError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

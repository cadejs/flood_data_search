#!/usr/bin/env python3
"""Perform an actor-aware manifest state transition."""

from __future__ import annotations

import argparse
import sys

from common import ContractError, atomic_write_json, load_json, utc_now, validate_artifact, validate_path
from lab_notebook import log_event
from verification_evidence import semantic_errors as verification_semantic_errors

TRANSITIONS = {
    "planned": {"discovered", "deferred", "failed"},
    "discovered": {"verified", "deferred", "failed"},
    "verified": {"built", "failed"},
    "built": {"failed"},
    "failed": {"discovered", "verified"},
    "deferred": {"planned", "discovered"},
}


def allowed_actor(current: str, target: str, actor: str) -> bool:
    if target == "discovered":
        return actor == "codex"
    if target in {"verified", "built", "failed"}:
        return actor == "claude_code"
    if target in {"planned", "deferred"}:
        return actor in {"codex", "claude_code"}
    return False


def transition_manifest(
    manifest: dict,
    country: dict,
    target: str,
    actor: str,
    now: str | None = None,
) -> dict:
    entry = next(
        (item for item in manifest["countries"] if item["iso2"] == country["iso2"]), None
    )
    if entry is None:
        raise ContractError(f"{country['iso2']} is not present in the manifest")
    current = entry["status"]
    if target != current and target not in TRANSITIONS[current]:
        raise ContractError(f"illegal manifest transition {current} -> {target}")
    if target != current and not allowed_actor(current, target, actor):
        raise ContractError(f"{actor} cannot perform manifest transition {current} -> {target}")
    if target in {"verified", "built"}:
        material = [source for source in country["sources"] if source["is_material"]]
        unverified = [
            source["id"]
            for source in material
            if source["verification"]["status"] == "unverified"
        ]
        if unverified:
            raise ContractError(
                f"cannot mark {target}; material records remain unverified: {unverified}"
            )
        evidence_errors = [
            error
            for index, source in enumerate(country["sources"])
            for error in verification_semantic_errors(
                source, f"$.sources[{index}]"
            )
        ]
        if evidence_errors:
            raise ContractError(
                f"cannot mark {target}; dataset-resolved audit is incomplete:\n"
                + "\n".join(evidence_errors)
            )
    if target == "built" and country["score"] is None:
        raise ContractError("cannot mark built before scoring")
    entry.update(
        {
            "status": target,
            "score": country["score"],
            "confidence": country["confidence"],
            "source_count": len(country["sources"]),
            "updated_at": now or utc_now(),
        }
    )
    validate_artifact(manifest)
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", default="data/manifest.json")
    parser.add_argument("--country", required=True)
    parser.add_argument("--status", required=True, choices=sorted(TRANSITIONS))
    parser.add_argument("--actor", required=True, choices=["codex", "claude_code"])
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    try:
        manifest = validate_path(args.manifest)
        country = validate_path(args.country)
        transition_manifest(manifest, country, args.status, args.actor)
        if args.dry_run:
            print(f"transition valid: {country['iso2']} -> {args.status}")
        else:
            atomic_write_json(args.manifest, manifest)
            log_event(
                args.actor,
                "manifest_transition",
                f"Transitioned manifest status to {args.status}.",
                iso2=country["iso2"],
                details={
                    "status": args.status,
                    "score": country["score"],
                    "confidence": country["confidence"],
                    "source_count": len(country["sources"]),
                },
            )
            print(f"manifest updated: {country['iso2']} -> {args.status}")
        return 0
    except (ContractError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

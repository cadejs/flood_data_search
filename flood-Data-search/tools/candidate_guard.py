#!/usr/bin/env python3
"""Fingerprint immutable candidate fields and reject silent rewrites/deletions."""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

from common import ROOT, SCHEMA_VERSION, ContractError, atomic_write_json, load_json, validate_path

INDEX_PATH = ROOT / ".pipeline" / "candidate_fingerprints.json"
MUTABLE_SOURCE_FIELDS = {"verification", "last_update"}


def candidate_payload(source: dict[str, Any]) -> dict[str, Any]:
    return {
        key: value
        for key, value in source.items()
        if key not in MUTABLE_SOURCE_FIELDS
    }


def candidate_fingerprint(source: dict[str, Any]) -> str:
    payload = json.dumps(
        candidate_payload(source),
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def load_index(path: Path = INDEX_PATH) -> dict[str, Any]:
    if not path.exists():
        return {"schema_version": SCHEMA_VERSION, "countries": {}}
    index = load_json(path)
    if set(index) != {"schema_version", "countries"}:
        raise ContractError("candidate fingerprint index has invalid fields")
    if index["schema_version"] != SCHEMA_VERSION:
        raise ContractError("candidate fingerprint index version mismatch")
    if not isinstance(index["countries"], dict):
        raise ContractError("candidate fingerprint countries must be an object")
    return index


def guard_country(
    country: dict[str, Any],
    *,
    actor: str | None = None,
    sync: bool = False,
    index_path: Path = INDEX_PATH,
) -> dict[str, Any]:
    index = load_index(index_path)
    baseline = index["countries"].setdefault(country["iso2"], {})
    current = {source["id"]: source for source in country["sources"]}

    deleted = sorted(set(baseline) - set(current))
    if deleted:
        raise ContractError(f"candidate records cannot be deleted: {deleted}")
    for source_id, source in current.items():
        fingerprint = candidate_fingerprint(source)
        if source_id in baseline:
            if baseline[source_id] != fingerprint:
                raise ContractError(
                    f"immutable candidate fields changed for {source_id}; append a replacement"
                )
            continue
        if not sync:
            raise ContractError(f"candidate index is missing new source {source_id}")
        if actor is None:
            raise ContractError("syncing new candidates requires an actor")
        if source["provenance"]["produced_by"] != actor:
            raise ContractError(
                f"new source {source_id} is owned by "
                f"{source['provenance']['produced_by']}, not {actor}"
            )
        baseline[source_id] = fingerprint
    if sync:
        atomic_write_json(index_path, index)
    return index


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("country")
    parser.add_argument("--actor", choices=["codex", "claude_code"])
    parser.add_argument("--sync", action="store_true")
    parser.add_argument("--index", default=str(INDEX_PATH))
    args = parser.parse_args()
    try:
        country = validate_path(args.country)
        guard_country(
            country,
            actor=args.actor,
            sync=args.sync,
            index_path=Path(args.index),
        )
        print(f"candidate guard passed for {country['iso2']}")
        return 0
    except (ContractError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())


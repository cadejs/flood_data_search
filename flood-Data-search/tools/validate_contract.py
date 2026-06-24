#!/usr/bin/env python3
"""Validate contract artifacts and cross-file manifest consistency."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from common import CONFIG_PATH, ContractError, DATA_DIR, load_json, validate_path
from candidate_guard import guard_country


def discover_paths(inputs: list[str]) -> list[Path]:
    if not inputs:
        inputs = [str(DATA_DIR)]
    discovered: list[Path] = []
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            discovered.extend(sorted(path.glob("*.json")))
        else:
            discovered.append(path)
    return discovered


def validate_manifest_consistency(paths: list[Path]) -> list[str]:
    errors: list[str] = []
    artifacts = {path.name: load_json(path) for path in paths}
    manifest = artifacts.get("manifest.json")
    if not manifest:
        return errors

    entries = manifest["countries"]
    seen: set[str] = set()
    for index, entry in enumerate(entries):
        iso2 = entry["iso2"]
        if iso2 in seen:
            errors.append(f"manifest countries[{index}]: duplicate ISO2 {iso2}")
        seen.add(iso2)
        country = artifacts.get(f"{iso2}.json")
        if country:
            if entry["report_scope"] != country["report_scope"]:
                errors.append(f"{iso2}: manifest report_scope does not match country file")
            if entry["source_count"] != len(country["sources"]):
                errors.append(f"{iso2}: manifest source_count does not match country file")
            if entry["score"] != country["score"]:
                errors.append(f"{iso2}: manifest score does not match country file")
            if entry["confidence"] != country["confidence"]:
                errors.append(f"{iso2}: manifest confidence does not match country file")

    if CONFIG_PATH.exists():
        config = load_json(CONFIG_PATH)
        expected = ["GB"] + config["final_order"]
        actual = [entry["iso2"] for entry in entries]
        if actual != expected:
            errors.append(
                "manifest order must be GB followed by config/countries.json final_order"
            )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", help="JSON files or directories; defaults to data/")
    args = parser.parse_args()

    paths = discover_paths(args.paths)
    failures: list[str] = []
    for path in paths:
        try:
            artifact = validate_path(path)
            if artifact.get("artifact_type") == "country":
                guard_country(artifact)
        except (ContractError, OSError, ValueError) as exc:
            failures.append(f"{path}: {exc}")

    failures.extend(validate_manifest_consistency(paths))
    if failures:
        print("\n\n".join(failures), file=sys.stderr)
        return 1
    print(f"validated {len(paths)} artifact(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

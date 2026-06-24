#!/usr/bin/env python3
"""Prepare findings updates after a dataset-resolved full-source audit."""

from __future__ import annotations

import argparse
from pathlib import Path

from common import CONFIG_PATH, atomic_write_json, load_json, validate_path
from verification_evidence import access_class, evidence_for


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default="data")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    data_dir = Path(args.data_dir)
    config = load_json(CONFIG_PATH)
    findings = validate_path(data_dir / "findings.json")
    existing = {(item["iso2"], item["id"]): item for item in findings["items"]}
    append_items = []
    item_updates = {}
    status_updates = {}

    for iso2 in config["final_order"]:
        country = validate_path(data_dir / f"{iso2}.json")
        for source in country["sources"]:
            if not source["is_material"] or source["verification"]["status"] != "failed":
                continue
            evidence = evidence_for(source)
            problem = (
                f"Dataset-resolved verification did not confirm usable access for "
                f"{source['id']} ({source['agency']} — {source['english_name']}). "
                f"Classification: {evidence.get('outcome', 'unavailable')} / "
                f"{access_class(source)}. {evidence.get('reason', '')}"
            )
            request = (
                "Human review: provide a current authoritative dataset-specific "
                "viewer, document, service, API, or download as a superseding "
                "candidate, or accept this coverage/access gap in the readiness score."
            )
            finding_evidence = {
                "verification_standard": evidence.get("standard"),
                "outcome": evidence.get("outcome"),
                "access_class": access_class(source),
                "http_status": source["verification"].get("http_status"),
                "final_url": source["verification"].get("final_url"),
                "checked_at": source["verification"].get("checked_at"),
            }
            key = (iso2, source["id"])
            string_key = f"{iso2}:{source['id']}"
            if key in existing:
                item_updates[string_key] = {
                    "problem": problem,
                    "evidence": finding_evidence,
                    "request": request,
                }
                status_updates[string_key] = "human_review"
            else:
                append_items.append(
                    {
                        "iso2": iso2,
                        "id": source["id"],
                        "problem": problem,
                        "evidence": finding_evidence,
                        "request": request,
                        "status": "human_review",
                    }
                )

    delta = {
        "schema_version": findings["schema_version"],
        "actor": "claude_code",
        "round": 2,
        "append_items": append_items,
        "item_updates": item_updates,
        "status_updates": status_updates,
    }
    atomic_write_json(args.output, delta)
    print(
        f"prepared {len(append_items)} new finding(s) and "
        f"{len(item_updates)} update(s)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

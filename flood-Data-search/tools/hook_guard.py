#!/usr/bin/env python3
"""Claude Code PostToolUse guard for data artifact writes."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

from common import ROOT
from candidate_guard import guard_country
from common import validate_path


def block(reason: str) -> int:
    print(json.dumps({"decision": "block", "reason": reason}))
    return 0


def main() -> int:
    try:
        event = json.load(sys.stdin)
    except json.JSONDecodeError as exc:
        return block(f"Hook received invalid JSON: {exc}")
    path_value = (event.get("tool_input") or {}).get("file_path") or (
        event.get("tool_input") or {}
    ).get("path")
    if not path_value:
        return 0
    path = Path(path_value)
    try:
        resolved = path.resolve()
        data_root = (ROOT / "data").resolve()
        resolved.relative_to(data_root)
    except (OSError, ValueError):
        return 0
    if resolved.suffix != ".json":
        return 0

    validation = subprocess.run(
        [sys.executable, str(ROOT / "tools" / "validate_contract.py"), str(resolved)],
        capture_output=True,
        text=True,
        check=False,
    )
    if validation.returncode:
        return block(f"Contract validation failed for {resolved.name}: {validation.stderr[:4000]}")

    if resolved.name not in {"manifest.json", "findings.json"}:
        try:
            country = validate_path(resolved)
            guard_country(country, actor="claude_code", sync=True)
        except Exception as exc:
            return block(f"Candidate immutability check failed for {resolved.name}: {exc}")
        verification = subprocess.run(
            [
                sys.executable,
                str(ROOT / "tools" / "verify_pending.py"),
                str(resolved),
                "--write",
                "--actor",
                "claude_code",
            ],
            capture_output=True,
            text=True,
            check=False,
        )
        if verification.returncode:
            return block(
                f"Automatic verification failed for {resolved.name}: "
                f"{verification.stderr[:4000]}"
            )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

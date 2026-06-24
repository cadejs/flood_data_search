#!/usr/bin/env python3
"""Append bounded audit events and render the shared lab notebook."""

from __future__ import annotations

import argparse
import fcntl
import json
import os
import sys
from pathlib import Path
from typing import Any

from common import ROOT, atomic_write_text, utc_now

LOG_PATH = ROOT / "logs" / "lab_notebook.jsonl"
NOTEBOOK_PATH = ROOT / "LAB_NOTEBOOK.md"
EVENTS = {
    "decision",
    "implementation",
    "discovery",
    "verification",
    "score",
    "manifest_transition",
    "finding",
    "build",
    "test",
    "human_review",
    "handoff",
}
FORBIDDEN_DETAIL_KEYS = {
    "raw",
    "raw_payload",
    "body",
    "response_body",
    "xml",
    "html",
    "capabilities_xml",
}
MAX_EVENT_BYTES = 12 * 1024


class NotebookError(ValueError):
    pass


def _validate_details(value: Any, path: str = "details") -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if str(key).lower() in FORBIDDEN_DETAIL_KEYS:
                raise NotebookError(f"{path}.{key}: raw payload fields are forbidden")
            _validate_details(item, f"{path}.{key}")
    elif isinstance(value, list):
        if len(value) > 200:
            raise NotebookError(f"{path}: arrays are limited to 200 items")
        for index, item in enumerate(value):
            _validate_details(item, f"{path}[{index}]")
    elif isinstance(value, str) and len(value) > 4000:
        raise NotebookError(f"{path}: strings are limited to 4000 characters")
    elif value is not None and not isinstance(value, (str, int, float, bool)):
        raise NotebookError(f"{path}: unsupported value type {type(value).__name__}")


def validate_event(event: dict[str, Any]) -> None:
    required = {"timestamp", "actor", "event", "iso2", "source_id", "summary", "details"}
    if set(event) != required:
        raise NotebookError(f"event fields must be exactly {sorted(required)}")
    if event["actor"] not in {"codex", "claude_code", "human", "toolkit"}:
        raise NotebookError("invalid notebook actor")
    if event["event"] not in EVENTS:
        raise NotebookError("invalid notebook event type")
    if not isinstance(event["summary"], str) or not event["summary"].strip():
        raise NotebookError("summary is required")
    _validate_details(event["details"])
    size = len(json.dumps(event, ensure_ascii=False).encode("utf-8"))
    if size > MAX_EVENT_BYTES:
        raise NotebookError(f"event exceeds {MAX_EVENT_BYTES} bytes")


def read_events(path: Path = LOG_PATH) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    events = []
    with path.open("r", encoding="utf-8") as handle:
        for line_number, line in enumerate(handle, start=1):
            if not line.strip():
                continue
            try:
                event = json.loads(line)
                validate_event(event)
                events.append(event)
            except (json.JSONDecodeError, NotebookError) as exc:
                raise NotebookError(f"{path}:{line_number}: {exc}") from exc
    return events


def _format_details(details: dict[str, Any]) -> list[str]:
    lines: list[str] = []
    for key, value in details.items():
        label = key.replace("_", " ")
        if isinstance(value, (dict, list)):
            rendered = json.dumps(value, ensure_ascii=False, sort_keys=True)
        else:
            rendered = str(value)
        lines.append(f"- {label}: {rendered}")
    return lines


def render_notebook(events: list[dict[str, Any]]) -> str:
    lines = [
        "# Flood Data Readiness Lab Notebook",
        "",
        "Append-only audit history shared by Codex, Claude Code, and human reviewers.",
        "The structured source is `logs/lab_notebook.jsonl`; regenerate this view",
        "with `python3 tools/lab_notebook.py render`.",
        "",
        "Raw service payloads are deliberately excluded.",
        "",
    ]
    for event in events:
        scope = ""
        if event["iso2"]:
            scope += f" · {event['iso2']}"
        if event["source_id"]:
            scope += f" · {event['source_id']}"
        lines.extend(
            [
                f"## {event['timestamp']} — {event['event']}{scope}",
                "",
                f"**Actor:** {event['actor']}",
                "",
                event["summary"],
                "",
            ]
        )
        detail_lines = _format_details(event["details"])
        if detail_lines:
            lines.extend(detail_lines)
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def rebuild_notebook(log_path: Path = LOG_PATH, notebook_path: Path = NOTEBOOK_PATH) -> None:
    lock_path = log_path.with_suffix(log_path.suffix + ".lock")
    lock_path.parent.mkdir(parents=True, exist_ok=True)
    with lock_path.open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        atomic_write_text(notebook_path, render_notebook(read_events(log_path)))
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)


def log_event(
    actor: str,
    event_type: str,
    summary: str,
    *,
    iso2: str | None = None,
    source_id: str | None = None,
    details: dict[str, Any] | None = None,
    timestamp: str | None = None,
    log_path: Path = LOG_PATH,
    notebook_path: Path = NOTEBOOK_PATH,
) -> dict[str, Any]:
    event = {
        "timestamp": timestamp or utc_now(),
        "actor": actor,
        "event": event_type,
        "iso2": iso2,
        "source_id": source_id,
        "summary": summary.strip(),
        "details": details or {},
    }
    validate_event(event)
    log_path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = log_path.with_suffix(log_path.suffix + ".lock")
    with lock_path.open("a+", encoding="utf-8") as lock:
        fcntl.flock(lock.fileno(), fcntl.LOCK_EX)
        with log_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        atomic_write_text(notebook_path, render_notebook(read_events(log_path)))
        fcntl.flock(lock.fileno(), fcntl.LOCK_UN)
    return event


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    record = subparsers.add_parser("record")
    record.add_argument("--actor", required=True, choices=["codex", "claude_code", "human", "toolkit"])
    record.add_argument("--event", required=True, choices=sorted(EVENTS))
    record.add_argument("--summary", required=True)
    record.add_argument("--iso2")
    record.add_argument("--source-id")
    record.add_argument("--details", default="{}", help="bounded JSON object")
    subparsers.add_parser("render")
    subparsers.add_parser("check")
    args = parser.parse_args()
    try:
        if args.command == "record":
            details = json.loads(args.details)
            if not isinstance(details, dict):
                raise NotebookError("--details must decode to an object")
            log_event(
                args.actor,
                args.event,
                args.summary,
                iso2=args.iso2,
                source_id=args.source_id,
                details=details,
            )
        elif args.command == "render":
            rebuild_notebook()
        else:
            expected = render_notebook(read_events())
            actual = NOTEBOOK_PATH.read_text(encoding="utf-8") if NOTEBOOK_PATH.exists() else ""
            if expected != actual:
                raise NotebookError("LAB_NOTEBOOK.md is missing or out of date")
        return 0
    except (NotebookError, OSError, json.JSONDecodeError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

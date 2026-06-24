#!/usr/bin/env python3
"""Shared contract, JSON, and filesystem helpers."""

from __future__ import annotations

import json
import os
import re
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

SCHEMA_VERSION = "1.0.0"
ROOT = Path(__file__).resolve().parents[1]
SCHEMA_PATH = ROOT / "tools" / "schema.json"
CONFIG_PATH = ROOT / "config" / "countries.json"
DATA_DIR = ROOT / "data"


class ContractError(ValueError):
    """Raised when an artifact violates the frozen contract."""


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_json(path: str | Path) -> Any:
    with Path(path).open("r", encoding="utf-8") as handle:
        return json.load(handle)


def atomic_write_json(path: str | Path, value: Any) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=False) + "\n"
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def atomic_write_text(path: str | Path, payload: str) -> None:
    destination = Path(path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(
        prefix=f".{destination.name}.", suffix=".tmp", dir=destination.parent
    )
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, destination)
    finally:
        if os.path.exists(temporary):
            os.unlink(temporary)


def _resolve_ref(root: dict[str, Any], reference: str) -> dict[str, Any]:
    if not reference.startswith("#/"):
        raise ContractError(f"unsupported external schema reference: {reference}")
    node: Any = root
    for part in reference[2:].split("/"):
        part = part.replace("~1", "/").replace("~0", "~")
        node = node[part]
    return node


def _type_matches(value: Any, expected: str) -> bool:
    return {
        "object": isinstance(value, dict),
        "array": isinstance(value, list),
        "string": isinstance(value, str),
        "integer": isinstance(value, int) and not isinstance(value, bool),
        "number": isinstance(value, (int, float)) and not isinstance(value, bool),
        "boolean": isinstance(value, bool),
        "null": value is None,
    }.get(expected, False)


def _validate_format(value: str, format_name: str, path: str) -> list[str]:
    if format_name == "uri":
        parsed = urlparse(value)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            return [f"{path}: expected an absolute HTTP(S) URI"]
    elif format_name == "date-time":
        try:
            parsed_dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed_dt.tzinfo is None:
                raise ValueError
        except ValueError:
            return [f"{path}: expected an RFC 3339 date-time"]
    return []


def _schema_errors(
    value: Any,
    schema: dict[str, Any],
    root: dict[str, Any],
    path: str = "$",
) -> list[str]:
    if "$ref" in schema:
        return _schema_errors(value, _resolve_ref(root, schema["$ref"]), root, path)

    if "oneOf" in schema:
        outcomes = [_schema_errors(value, option, root, path) for option in schema["oneOf"]]
        matches = [errors for errors in outcomes if not errors]
        if len(matches) == 1:
            return []
        if not matches:
            shortest = min(outcomes, key=len)
            return [f"{path}: did not match any allowed artifact shape"] + shortest[:8]
        return [f"{path}: matched more than one allowed artifact shape"]

    errors: list[str] = []
    expected_type = schema.get("type")
    if expected_type is not None:
        expected_types = [expected_type] if isinstance(expected_type, str) else expected_type
        if not any(_type_matches(value, item) for item in expected_types):
            return [f"{path}: expected type {' or '.join(expected_types)}"]

    if "const" in schema and value != schema["const"]:
        errors.append(f"{path}: expected constant {schema['const']!r}")
    if "enum" in schema and value not in schema["enum"]:
        errors.append(f"{path}: value {value!r} is not in the allowed enum")

    if isinstance(value, dict):
        required = schema.get("required", [])
        for key in required:
            if key not in value:
                errors.append(f"{path}: missing required property {key!r}")
        properties = schema.get("properties", {})
        for key, item in value.items():
            child_path = f"{path}.{key}"
            if key in properties:
                errors.extend(_schema_errors(item, properties[key], root, child_path))
            else:
                additional = schema.get("additionalProperties", True)
                if additional is False:
                    errors.append(f"{child_path}: additional property is not allowed")
                elif isinstance(additional, dict):
                    errors.extend(_schema_errors(item, additional, root, child_path))
        if "maxProperties" in schema and len(value) > schema["maxProperties"]:
            errors.append(f"{path}: too many properties")

    if isinstance(value, list):
        if "minItems" in schema and len(value) < schema["minItems"]:
            errors.append(f"{path}: expected at least {schema['minItems']} items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            errors.append(f"{path}: expected at most {schema['maxItems']} items")
        if schema.get("uniqueItems"):
            canonical = [json.dumps(item, sort_keys=True, ensure_ascii=False) for item in value]
            if len(canonical) != len(set(canonical)):
                errors.append(f"{path}: array items must be unique")
        item_schema = schema.get("items")
        if item_schema:
            for index, item in enumerate(value):
                errors.extend(_schema_errors(item, item_schema, root, f"{path}[{index}]"))

    if isinstance(value, str):
        if "minLength" in schema and len(value) < schema["minLength"]:
            errors.append(f"{path}: string is too short")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            errors.append(f"{path}: string is too long")
        if "pattern" in schema and not re.fullmatch(schema["pattern"], value):
            errors.append(f"{path}: string does not match {schema['pattern']!r}")
        if "format" in schema:
            errors.extend(_validate_format(value, schema["format"], path))

    if isinstance(value, (int, float)) and not isinstance(value, bool):
        if "minimum" in schema and value < schema["minimum"]:
            errors.append(f"{path}: value is below minimum {schema['minimum']}")
        if "maximum" in schema and value > schema["maximum"]:
            errors.append(f"{path}: value exceeds maximum {schema['maximum']}")

    return errors


def _semantic_errors(artifact: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if artifact.get("schema_version") != SCHEMA_VERSION:
        errors.append(
            f"$.schema_version: expected {SCHEMA_VERSION!r}, got "
            f"{artifact.get('schema_version')!r}"
        )

    if artifact.get("artifact_type") == "country":
        from verification_evidence import semantic_errors as verification_semantic_errors

        iso2 = artifact["iso2"]
        ids: set[str] = set()
        for index, source in enumerate(artifact["sources"]):
            prefix = f"$.sources[{index}]"
            source_id = source["id"]
            if source_id in ids:
                errors.append(f"{prefix}.id: duplicate source ID {source_id}")
            ids.add(source_id)
            if not source_id.startswith(f"{iso2}-"):
                errors.append(f"{prefix}.id: source ID must start with {iso2}-")
            if not any(source["links"].values()):
                errors.append(f"{prefix}.links: at least one candidate link is required")
            if source["supersedes_id"] == source_id:
                errors.append(f"{prefix}.supersedes_id: a record cannot supersede itself")
            evidence_size = len(
                json.dumps(source["verification"]["evidence"], ensure_ascii=False).encode("utf-8")
            )
            if evidence_size > 8192:
                errors.append(f"{prefix}.verification.evidence: exceeds the 8 KiB bound")
            verification = source["verification"]
            if verification["status"] == "unverified":
                non_null = [
                    field
                    for field in (
                        "http_status",
                        "content_type",
                        "final_url",
                        "checked_at",
                        "checked_by",
                    )
                    if verification[field] is not None
                ]
                if non_null or verification["evidence"] is not None:
                    errors.append(
                        f"{prefix}.verification: unverified records must have empty evidence fields"
                    )
            else:
                if verification["checked_at"] is None or verification["checked_by"] is None:
                    errors.append(
                        f"{prefix}.verification: terminal records require checked_at and checked_by"
                    )
                errors.extend(verification_semantic_errors(source, prefix))
        for index, source in enumerate(artifact["sources"]):
            supersedes_id = source["supersedes_id"]
            if supersedes_id is not None and supersedes_id not in ids:
                errors.append(
                    f"$.sources[{index}].supersedes_id: unknown source ID {supersedes_id}"
                )
        if artifact["score"] is None:
            if artifact["subscores"] is not None or artifact["confidence"] is not None:
                errors.append("$.score: score, confidence, and subscores must be populated together")
        elif artifact["subscores"] is None or artifact["confidence"] is None:
            errors.append("$.score: score, confidence, and subscores must be populated together")

    return errors


def validate_artifact(artifact: Any, schema_path: str | Path = SCHEMA_PATH) -> None:
    schema = load_json(schema_path)
    errors = _schema_errors(artifact, schema, schema)
    if isinstance(artifact, dict):
        errors.extend(_semantic_errors(artifact))
    if errors:
        raise ContractError("\n".join(errors))


def validate_path(path: str | Path, schema_path: str | Path = SCHEMA_PATH) -> dict[str, Any]:
    artifact = load_json(path)
    validate_artifact(artifact, schema_path)
    return artifact


def is_http_url(value: str | None) -> bool:
    if not value:
        return False
    parsed = urlparse(value)
    return parsed.scheme in {"http", "https"} and bool(parsed.netloc)

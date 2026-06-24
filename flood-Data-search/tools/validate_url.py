#!/usr/bin/env python3
"""Bounded URL validation: HEAD followed by a ranged GET."""

from __future__ import annotations

import argparse
import http.client
import json
import sys
import urllib.error
import urllib.parse
import urllib.request
from typing import Any

from lab_notebook import log_event

MAX_BYTES = 64 * 1024
USER_AGENT = "FloodDataReadiness/1.0 (+bounded-link-validator)"


def _open(request: urllib.request.Request, timeout: float):
    return urllib.request.urlopen(request, timeout=timeout)


def _status(response: Any) -> int | None:
    return getattr(response, "status", None) or getattr(response, "code", None)


def _headers(response: Any) -> Any:
    return getattr(response, "headers", {})


def validate_url(url: str, timeout: float = 20.0) -> dict[str, Any]:
    result: dict[str, Any] = {
        "http_status": None,
        "content_type": None,
        "final_url": None,
        "bytes": 0,
        "head_status": None,
        "range_honored": None,
        "error": None,
    }
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        result["error"] = "GET: only absolute HTTP(S) URLs are allowed"
        return result

    head = urllib.request.Request(
        url,
        method="HEAD",
        headers={"User-Agent": USER_AGENT, "Accept-Encoding": "identity"},
    )
    try:
        with _open(head, timeout) as response:
            result["head_status"] = _status(response)
    except urllib.error.HTTPError as exc:
        try:
            result["head_status"] = exc.code
        finally:
            exc.close()
    except (urllib.error.URLError, ValueError, OSError, http.client.HTTPException) as exc:
        result["error"] = f"HEAD: {type(exc).__name__}: {exc}"

    get = urllib.request.Request(
        url,
        method="GET",
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Encoding": "identity",
            "Range": f"bytes=0-{MAX_BYTES - 1}",
        },
    )
    try:
        with _open(get, timeout) as response:
            headers = _headers(response)
            body = response.read(MAX_BYTES)
            result.update(
                {
                    "http_status": _status(response),
                    "content_type": headers.get_content_type()
                    if hasattr(headers, "get_content_type")
                    else headers.get("Content-Type"),
                    "final_url": response.geturl(),
                    "bytes": len(body),
                    "range_honored": _status(response) == 206
                    or bool(headers.get("Content-Range")),
                    "error": None,
                }
            )
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read(MAX_BYTES)
            headers = exc.headers or {}
            content_type = (
                headers.get_content_type()
                if hasattr(headers, "get_content_type")
                else headers.get("Content-Type")
            )
            result.update(
                {
                    "http_status": exc.code,
                    "content_type": content_type,
                    "final_url": exc.geturl(),
                    "bytes": len(body),
                    "range_honored": exc.code == 206 or bool(headers.get("Content-Range")),
                    "error": f"HTTPError: {exc.reason}",
                }
            )
        finally:
            exc.close()
    except (urllib.error.URLError, ValueError, OSError, http.client.HTTPException) as exc:
        result["error"] = f"GET: {type(exc).__name__}: {exc}"
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--timeout", type=float, default=20.0)
    parser.add_argument("--actor", choices=["codex", "claude_code"])
    parser.add_argument("--iso2")
    parser.add_argument("--source-id")
    args = parser.parse_args()
    result = validate_url(args.url, args.timeout)
    if args.actor:
        log_event(
            args.actor,
            "verification" if args.actor == "claude_code" else "discovery",
            "Ran a bounded URL check.",
            iso2=args.iso2,
            source_id=args.source_id,
            details={
                key: result[key]
                for key in (
                    "http_status",
                    "content_type",
                    "final_url",
                    "bytes",
                    "head_status",
                    "range_honored",
                )
            },
        )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0 if result["http_status"] and 200 <= result["http_status"] < 400 else 1


if __name__ == "__main__":
    raise SystemExit(main())

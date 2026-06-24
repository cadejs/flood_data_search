#!/usr/bin/env python3
"""Safely distil common geospatial and open-data service payloads."""

from __future__ import annotations

import argparse
import json
import re
import socket
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from typing import Any

from lab_notebook import log_event

MAX_PAYLOAD_BYTES = 20 * 1024 * 1024
MAX_OUTPUT_BYTES = 50 * 1024
MAX_LAYERS = 200
USER_AGENT = "FloodDataReadiness/1.0 (+bounded-capability-prober)"


class ProbeError(ValueError):
    pass


def _local(tag: str) -> str:
    return tag.rsplit("}", 1)[-1].lower()


def _text(element: ET.Element | None) -> str | None:
    if element is None or element.text is None:
        return None
    value = element.text.strip()
    return value or None


def _append_query(url: str, values: dict[str, str]) -> str:
    parsed = urllib.parse.urlsplit(url)
    query = urllib.parse.parse_qs(parsed.query, keep_blank_values=True)
    lowered = {key.lower() for key in query}
    for key, value in values.items():
        if key.lower() not in lowered:
            query[key] = [value]
    encoded = urllib.parse.urlencode(query, doseq=True)
    return urllib.parse.urlunsplit(
        (parsed.scheme, parsed.netloc, parsed.path, encoded, parsed.fragment)
    )


def normalize_probe_url(url: str) -> str:
    lower = url.lower()
    if "arcgis" in lower and ("/rest/services/" in lower or "/sharing/rest/" in lower):
        return _append_query(url, {"f": "pjson"})
    if "service=wfs" in lower or re.search(r"/wfs(?:/|$|\\?)", lower):
        return _append_query(url, {"service": "WFS", "request": "GetCapabilities"})
    if "service=wms" in lower or re.search(r"/wms(?:/|$|\\?)", lower):
        return _append_query(url, {"service": "WMS", "request": "GetCapabilities"})
    return url


def fetch_payload(url: str, timeout: float = 30.0) -> tuple[bytes, str | None, str]:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"} or not parsed.netloc:
        raise ProbeError("only absolute HTTP(S) URLs are allowed")
    request = urllib.request.Request(
        normalize_probe_url(url),
        headers={"User-Agent": USER_AGENT, "Accept-Encoding": "identity"},
    )
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            declared = response.headers.get("Content-Length")
            if declared:
                try:
                    if int(declared) > MAX_PAYLOAD_BYTES:
                        raise ProbeError(
                            f"declared payload {declared} bytes exceeds {MAX_PAYLOAD_BYTES}"
                        )
                except ValueError:
                    pass
            data = response.read(MAX_PAYLOAD_BYTES + 1)
            if len(data) > MAX_PAYLOAD_BYTES:
                raise ProbeError(f"payload exceeds {MAX_PAYLOAD_BYTES} bytes")
            content_type = (
                response.headers.get_content_type()
                if hasattr(response.headers, "get_content_type")
                else response.headers.get("Content-Type")
            )
            return data, content_type, response.geturl()
    except (urllib.error.URLError, socket.timeout, ssl.SSLError) as exc:
        raise ProbeError(f"{type(exc).__name__}: {exc}") from exc


def _xml_root(data: bytes) -> ET.Element:
    if re.search(br"<!\s*(DOCTYPE|ENTITY)\b", data, flags=re.IGNORECASE):
        raise ProbeError("DTD/entity declarations are forbidden")
    try:
        return ET.fromstring(data)
    except ET.ParseError as exc:
        raise ProbeError(f"malformed XML: {exc}") from exc


def _first_bbox(root: ET.Element) -> list[float] | None:
    for element in root.iter():
        name = _local(element.tag)
        if name == "ex_geographicboundingbox":
            values: dict[str, float] = {}
            for child in element:
                value = _text(child)
                if value is not None:
                    try:
                        values[_local(child.tag)] = float(value)
                    except ValueError:
                        pass
            keys = ("westboundlongitude", "southboundlatitude", "eastboundlongitude", "northboundlatitude")
            if all(key in values for key in keys):
                return [values[key] for key in keys]
        if name in {"boundingbox", "wgs84boundingbox"}:
            attrs = {key.lower(): value for key, value in element.attrib.items()}
            attr_keys = ("minx", "miny", "maxx", "maxy")
            if all(key in attrs for key in attr_keys):
                try:
                    return [float(attrs[key]) for key in attr_keys]
                except ValueError:
                    pass
            corners = [_text(child) for child in element]
            if len(corners) >= 2 and corners[0] and corners[1]:
                try:
                    low = [float(item) for item in corners[0].split()]
                    high = [float(item) for item in corners[1].split()]
                    return [low[0], low[1], high[0], high[1]]
                except (ValueError, IndexError):
                    pass
    return None


def _declared_update_xml(root: ET.Element) -> str | None:
    for key, value in root.attrib.items():
        if key.lower() in {"updatesequence", "updated", "lastmodified"}:
            return value
    for element in root.iter():
        if _local(element.tag) in {"updated", "modified", "date", "lastmodified"}:
            value = _text(element)
            if value:
                return value
    return None


def parse_wms(root: ET.Element) -> dict[str, Any]:
    layers: list[str] = []
    crs: list[str] = []
    formats: list[str] = []
    for element in root.iter():
        name = _local(element.tag)
        if name == "layer":
            for child in element:
                if _local(child.tag) == "name":
                    value = _text(child)
                    if value:
                        layers.append(value)
                    break
        elif name in {"crs", "srs"}:
            value = _text(element)
            if value:
                crs.extend(value.split())
        elif name == "format":
            value = _text(element)
            if value and "/" in value:
                formats.append(value)
    return _result("wms", layers, crs, formats, _first_bbox(root), _declared_update_xml(root))


def parse_wfs(root: ET.Element) -> dict[str, Any]:
    layers: list[str] = []
    crs: list[str] = []
    formats: list[str] = []
    for element in root.iter():
        name = _local(element.tag)
        if name == "featuretype":
            for child in element:
                if _local(child.tag) == "name":
                    value = _text(child)
                    if value:
                        layers.append(value)
                elif _local(child.tag) in {"defaultcrs", "defaultsrs", "othercrs", "othersrs"}:
                    value = _text(child)
                    if value:
                        crs.append(value)
        elif name in {"outputformat", "value"}:
            value = _text(element)
            if value and ("/" in value or value.lower() in {"gml2", "gml3", "json"}):
                formats.append(value)
    return _result("wfs", layers, crs, formats, _first_bbox(root), _declared_update_xml(root))


def parse_atom(root: ET.Element) -> dict[str, Any]:
    layers: list[str] = []
    formats: list[str] = []
    for entry in root.iter():
        if _local(entry.tag) != "entry":
            continue
        title = next((_text(child) for child in entry if _local(child.tag) == "title"), None)
        if title:
            layers.append(title)
        for child in entry:
            if _local(child.tag) == "link":
                content_type = child.attrib.get("type")
                if content_type:
                    formats.append(content_type)
    return _result("atom", layers, [], formats, None, _declared_update_xml(root))


def _epoch_ms(value: Any) -> str | None:
    if not isinstance(value, (int, float)):
        return None
    try:
        return (
            datetime.fromtimestamp(value / 1000, tz=timezone.utc)
            .replace(microsecond=0)
            .isoformat()
            .replace("+00:00", "Z")
        )
    except (ValueError, OSError, OverflowError):
        return None


def parse_arcgis(payload: dict[str, Any]) -> dict[str, Any]:
    layers = [
        str(layer.get("name") or layer.get("id"))
        for layer in payload.get("layers", [])
        if isinstance(layer, dict) and (layer.get("name") is not None or layer.get("id") is not None)
    ]
    spatial = payload.get("spatialReference") or payload.get("fullExtent", {}).get("spatialReference", {})
    crs = []
    if isinstance(spatial, dict):
        wkid = spatial.get("latestWkid") or spatial.get("wkid")
        if wkid:
            crs.append(f"EPSG:{wkid}")
    formats = []
    supported = payload.get("supportedImageFormatTypes")
    if isinstance(supported, str):
        formats.extend(item.strip() for item in supported.split(",") if item.strip())
    bbox = None
    extent = payload.get("fullExtent")
    if isinstance(extent, dict) and all(key in extent for key in ("xmin", "ymin", "xmax", "ymax")):
        bbox = [extent[key] for key in ("xmin", "ymin", "xmax", "ymax")]
    updated = _epoch_ms((payload.get("editingInfo") or {}).get("lastEditDate"))
    return _result("arcgis_rest", layers, crs, formats, bbox, updated)


def parse_ckan(payload: dict[str, Any]) -> dict[str, Any]:
    result = payload.get("result") if isinstance(payload.get("result"), dict) else payload
    resources = result.get("resources", []) if isinstance(result, dict) else []
    layers = []
    formats = []
    for resource in resources:
        if not isinstance(resource, dict):
            continue
        label = resource.get("name") or resource.get("id") or resource.get("url")
        if label:
            layers.append(str(label))
        if resource.get("format"):
            formats.append(str(resource["format"]))
    updated = result.get("metadata_modified") or result.get("revision_timestamp")
    return _result("ckan", layers, [], formats, None, updated)


def parse_ogc_api(payload: dict[str, Any]) -> dict[str, Any]:
    collections = payload.get("collections", [])
    layers = []
    for collection in collections:
        if isinstance(collection, dict):
            label = collection.get("id") or collection.get("title")
            if label:
                layers.append(str(label))
    formats = []
    for link in payload.get("links", []):
        if isinstance(link, dict) and link.get("type"):
            formats.append(str(link["type"]))
    bbox = None
    if collections:
        extent = collections[0].get("extent", {}).get("spatial", {}).get("bbox")
        if isinstance(extent, list) and extent:
            bbox = extent[0]
    updated = payload.get("updated") or payload.get("timeStamp")
    return _result("ogc_api", layers, [], formats, bbox, updated)


def _result(
    service_type: str,
    layers: list[str],
    crs: list[str],
    formats: list[str],
    bbox: Any,
    declared_update: Any,
) -> dict[str, Any]:
    unique_layers = list(dict.fromkeys(layers))
    result = {
        "service_type": service_type,
        "layers": unique_layers[:MAX_LAYERS],
        "layer_count": len(unique_layers),
        "layers_truncated": len(unique_layers) > MAX_LAYERS,
        "crs": list(dict.fromkeys(crs))[:100],
        "formats": list(dict.fromkeys(formats))[:100],
        "bbox": bbox,
        "declared_update": declared_update,
    }
    return _bound_output(result)


def _bound_output(result: dict[str, Any]) -> dict[str, Any]:
    while len(json.dumps(result, ensure_ascii=False).encode("utf-8")) > MAX_OUTPUT_BYTES:
        if result["layers"]:
            result["layers"] = result["layers"][: max(0, len(result["layers"]) // 2)]
            result["layers_truncated"] = True
        elif result["formats"]:
            result["formats"] = result["formats"][: max(0, len(result["formats"]) // 2)]
        elif result["crs"]:
            result["crs"] = result["crs"][: max(0, len(result["crs"]) // 2)]
        else:
            raise ProbeError("distilled output exceeds 50 KiB")
    return result


def probe_payload(data: bytes, content_type: str | None = None, url: str = "") -> dict[str, Any]:
    stripped = data.lstrip()
    lower_type = (content_type or "").lower()
    if stripped.startswith(b"<") or "xml" in lower_type:
        root = _xml_root(data)
        root_name = _local(root.tag)
        if "wms" in root_name or root_name in {"wmt_ms_capabilities"}:
            return parse_wms(root)
        if "wfs" in root_name:
            return parse_wfs(root)
        if root_name == "feed":
            return parse_atom(root)
        raise ProbeError(f"unsupported XML root: {root_name}")

    try:
        payload = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ProbeError(f"unsupported non-JSON payload: {exc}") from exc
    if not isinstance(payload, dict):
        raise ProbeError("JSON service payload must be an object")
    if "layers" in payload and (
        "currentVersion" in payload
        or "serviceDescription" in payload
        or "supportedImageFormatTypes" in payload
    ):
        return parse_arcgis(payload)
    if "result" in payload and ("success" in payload or "help" in payload):
        return parse_ckan(payload)
    if "collections" in payload or "conformsTo" in payload:
        return parse_ogc_api(payload)
    if "/api/3/action/" in url.lower() and "result" in payload:
        return parse_ckan(payload)
    raise ProbeError("unrecognized JSON service payload")


def probe_url(url: str, timeout: float = 30.0) -> dict[str, Any]:
    data, content_type, final_url = fetch_payload(url, timeout)
    result = probe_payload(data, content_type, final_url)
    result["final_url"] = final_url
    result["content_type"] = content_type
    return _bound_output(result)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url")
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--actor", choices=["codex", "claude_code"])
    parser.add_argument("--iso2")
    parser.add_argument("--source-id")
    args = parser.parse_args()
    try:
        result = probe_url(args.url, args.timeout)
    except ProbeError as exc:
        print(json.dumps({"error": str(exc)}, ensure_ascii=False), file=sys.stderr)
        return 1
    if args.actor:
        log_event(
            args.actor,
            "verification" if args.actor == "claude_code" else "discovery",
            "Distilled a bounded service capability response.",
            iso2=args.iso2,
            source_id=args.source_id,
            details={
                key: result.get(key)
                for key in (
                    "service_type",
                    "layer_count",
                    "layers_truncated",
                    "crs",
                    "formats",
                    "bbox",
                    "declared_update",
                    "final_url",
                )
            },
        )
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

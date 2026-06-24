from __future__ import annotations

import copy
import json
import sys
import tempfile
import threading
import unittest
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

from apply_delta import apply_delta
from build_doc import (
    build_markdown,
    lint_country,
    portal_search_glosses,
    portal_search_terms,
    website_directory,
    website_root,
)
from candidate_guard import guard_country
from common import ContractError, load_json, validate_artifact
from lab_notebook import NotebookError, log_event, read_events, render_notebook
from probe_capabilities import MAX_LAYERS, ProbeError, probe_payload
from score_country import derive_score, enforce_evidence_caps, evidence_subscores
from update_findings import apply_findings_delta
from update_manifest import transition_manifest
from validate_url import MAX_BYTES, validate_url
from verify_pending import verify_source

FIXTURES = ROOT / "tests" / "fixtures"


def fixture_bytes(name: str) -> bytes:
    return (FIXTURES / name).read_bytes()


def source_fixture(iso2: str = "BR") -> dict:
    return {
        "id": f"{iso2}-ANA-001",
        "jurisdiction": "National",
        "agency": "Synthetic National Agency",
        "native_name": "Synthetic Flood Hazard Dataset",
        "english_name": "Synthetic Flood Hazard Dataset",
        "product_type": "national_hazard_map",
        "flood_types": ["fluvial", "coastal", "surface_water"],
        "scenarios": ["10-year", "100-year", "extreme"],
        "coverage": "National",
        "resolution_scale": "10 m",
        "formats": ["WMS", "GeoTIFF"],
        "license": "Open licence",
        "delivery_mode": "viewer+service",
        "access_constraints": [],
        "links": {
            "primary": "https://example.test/flood",
            "service": "https://example.test/wms?service=WMS&request=GetCapabilities",
            "download": None,
        },
        "last_update": None,
        "is_fallback": False,
        "is_material": True,
        "supersedes_id": None,
        "verification": {
            "status": "unverified",
            "http_status": None,
            "content_type": None,
            "final_url": None,
            "evidence": None,
            "checked_at": None,
            "checked_by": None,
        },
        "provenance": {"produced_by": "codex", "round": 1},
        "notes": "Synthetic test source.",
    }


def unverified_country(iso2: str = "BR") -> dict:
    return {
        "artifact_type": "country",
        "schema_version": "1.0.0",
        "report_scope": "final",
        "iso2": iso2,
        "country_name": "Brazil",
        "coverage_model": "nationally_unified",
        "fragmentation_summary": "Synthetic country with all required families.",
        "top_regions": [],
        "deferred_regions": [],
        "score": None,
        "confidence": None,
        "score_provisional": False,
        "subscores": None,
        "sources": [source_fixture(iso2)],
        "discovery_metrics": {
            "searches": 1,
            "page_reads": 1,
            "capability_probes": 1,
            "consecutive_empty_searches": 0,
            "stop_reason": "Synthetic fixture complete.",
        },
        "provenance": {
            "discovered_by": "codex",
            "discovered_at": "2026-06-24T15:00:00Z",
        },
    }


def strict_evidence(
    *,
    access_class: str = "service",
    outcome: str = "confirmed",
    selected_role: str | None = "service",
    selected_url: str | None = "https://example.test/wms",
    reason: str = "Authoritative flood layers confirmed.",
) -> dict:
    return {
        "standard": "dataset_resolved_v1",
        "outcome": outcome,
        "access_class": access_class,
        "authority_confirmed": outcome == "confirmed",
        "dataset_identity_confirmed": outcome == "confirmed",
        "human_usable": outcome == "confirmed",
        "selected_role": selected_role,
        "selected_url": selected_url,
        "confirmed": {
            "flood_types": ["fluvial", "coastal", "surface_water"],
            "scenarios": [
                "10-year",
                "100-year",
                "extreme depth and velocity",
                "climate future",
                "historic",
            ],
            "coverage": "National",
            "formats": ["WMS", "GeoTIFF"],
            "license": "Open licence",
            "last_update": "2026-06-01",
        },
        "reason": reason,
        "links": {},
        "capabilities": {
            "service_type": "wms",
            "layer_count": 2,
            "layers": ["flood_extent", "flood_depth"],
            "formats": ["image/png"],
            "crs": ["EPSG:4326"],
            "bbox": [-10, 49, 2, 61],
            "declared_update": "2026-06-01",
            "layers_truncated": False,
        },
    }


def verified_country(iso2: str = "BR") -> dict:
    country = unverified_country(iso2)
    country["subscores"] = {
        "geographic_completeness": 4,
        "scenario_richness": 4,
        "technical_accessibility": 5,
        "documentation_currency": 4,
        "licensing": 4,
        "integration_effort": 4,
    }
    country["score"] = 4
    country["confidence"] = "high"
    country["score_provisional"] = False
    source = country["sources"][0]
    source["verification"] = {
        "status": "verified",
        "http_status": 200,
        "content_type": "application/xml",
        "final_url": "https://example.test/wms",
        "evidence": strict_evidence(),
        "checked_at": "2026-06-24T15:00:00Z",
        "checked_by": "claude_code",
    }
    validate_artifact(country)
    return country


def manifest_fixture(iso2: str = "BR", status: str = "planned") -> dict:
    return {
        "artifact_type": "manifest",
        "schema_version": "1.0.0",
        "countries": [
            {
                "iso2": iso2,
                "report_scope": "final",
                "status": status,
                "score": None,
                "confidence": None,
                "source_count": 0,
                "updated_at": "2026-06-24T15:00:00Z",
            }
        ],
    }


class ContractTests(unittest.TestCase):
    def test_fixture_is_valid_and_unverified(self):
        country = unverified_country()
        validate_artifact(country)
        self.assertTrue(
            all(source["verification"]["status"] == "unverified" for source in country["sources"])
        )

    def test_version_rejection(self):
        country = unverified_country()
        country["schema_version"] = "2.0.0"
        with self.assertRaises(ContractError):
            validate_artifact(country)

    def test_unverified_record_cannot_contain_evidence(self):
        country = unverified_country()
        country["sources"][0]["verification"]["http_status"] = 200
        with self.assertRaises(ContractError):
            validate_artifact(country)

    def test_duplicate_source_id_rejected(self):
        country = unverified_country()
        country["sources"].append(copy.deepcopy(country["sources"][0]))
        with self.assertRaises(ContractError):
            validate_artifact(country)

    def test_legacy_reachability_only_verification_is_rejected(self):
        country = unverified_country()
        country["sources"][0]["verification"] = {
            "status": "verified",
            "http_status": 200,
            "content_type": "text/html",
            "final_url": country["sources"][0]["links"]["primary"],
            "evidence": {"sample_ok": True},
            "checked_at": "2026-06-24T15:00:00Z",
            "checked_by": "claude_code",
        }
        with self.assertRaises(ContractError):
            validate_artifact(country)


class DeltaOwnershipTests(unittest.TestCase):
    def test_existing_candidate_cannot_be_rewritten(self):
        country = unverified_country("GB")
        replacement = copy.deepcopy(country["sources"][0])
        replacement["links"]["primary"] = "https://example.test/new"
        delta = {
            "schema_version": "1.0.0",
            "actor": "codex",
            "iso2": "GB",
            "append_sources": [replacement],
        }
        with self.assertRaises(ContractError):
            apply_delta(country, delta, "codex")

    def test_codex_cannot_write_score(self):
        country = unverified_country("GB")
        delta = {
            "schema_version": "1.0.0",
            "actor": "codex",
            "iso2": "GB",
            "country_updates": {"score": 5},
        }
        with self.assertRaises(ContractError):
            apply_delta(country, delta, "codex")

    def test_claude_can_append_owned_replacement(self):
        country = unverified_country("GB")
        replacement = copy.deepcopy(country["sources"][0])
        replacement["id"] = "GB-EA-099"
        replacement["supersedes_id"] = country["sources"][0]["id"]
        replacement["provenance"] = {"produced_by": "claude_code", "round": 1}
        replacement["notes"] = "Replacement for a renamed endpoint."
        replacement["links"]["primary"] = "https://example.test/replacement"
        delta = {
            "schema_version": "1.0.0",
            "actor": "claude_code",
            "iso2": "GB",
            "append_sources": [replacement],
        }
        updated = apply_delta(country, delta, "claude_code")
        self.assertEqual(
            updated["sources"][-1]["supersedes_id"], country["sources"][0]["id"]
        )

    def test_only_claude_can_write_findings(self):
        findings = {"artifact_type": "findings", "schema_version": "1.0.0", "round": 1, "items": []}
        delta = {
            "schema_version": "1.0.0",
            "actor": "codex",
            "append_items": [],
            "status_updates": {},
        }
        with self.assertRaises(ContractError):
            apply_findings_delta(findings, delta, "codex")

    def test_round_two_findings_cannot_remain_unresolved(self):
        findings = {"artifact_type": "findings", "schema_version": "1.0.0", "round": 1, "items": []}
        delta = {
            "schema_version": "1.0.0",
            "actor": "claude_code",
            "round": 2,
            "append_items": [
                {
                    "iso2": "GB",
                    "id": "GB-EA-001",
                    "problem": "Still unavailable",
                    "evidence": {"http_status": 404},
                    "request": "Human review",
                    "status": "unresolved",
                }
            ],
            "status_updates": {},
        }
        with self.assertRaises(ContractError):
            apply_findings_delta(findings, delta, "claude_code")


class CandidateGuardTests(unittest.TestCase):
    def test_candidate_mutation_and_deletion_are_rejected(self):
        country = unverified_country("GB")
        with tempfile.TemporaryDirectory() as temporary:
            index = Path(temporary) / "candidate_fingerprints.json"
            guard_country(country, actor="codex", sync=True, index_path=index)
            mutated = copy.deepcopy(country)
            mutated["sources"][0]["links"]["primary"] = "https://example.test/rewritten"
            with self.assertRaises(ContractError):
                guard_country(mutated, index_path=index)
            deleted = copy.deepcopy(country)
            deleted["sources"].pop()
            with self.assertRaises(ContractError):
                guard_country(deleted, index_path=index)

    def test_owned_append_can_be_frozen(self):
        country = unverified_country("GB")
        with tempfile.TemporaryDirectory() as temporary:
            index = Path(temporary) / "candidate_fingerprints.json"
            guard_country(country, actor="codex", sync=True, index_path=index)
            appended = copy.deepcopy(country)
            source = copy.deepcopy(country["sources"][0])
            source["id"] = "GB-EA-099"
            source["links"]["primary"] = "https://example.test/replacement"
            source["supersedes_id"] = "GB-EA-001"
            source["provenance"] = {"produced_by": "claude_code", "round": 1}
            source["notes"] = "Replacement for a renamed endpoint."
            appended["sources"].append(source)
            guard_country(
                appended, actor="claude_code", sync=True, index_path=index
            )
            guard_country(appended, index_path=index)


class ScoreTests(unittest.TestCase):
    def test_equal_mean_rounds_half_up(self):
        result = derive_score(
            {
                "geographic_completeness": 4,
                "scenario_richness": 4,
                "technical_accessibility": 4,
                "documentation_currency": 4,
                "licensing": 4,
                "integration_effort": 5,
            }
        )
        self.assertEqual(result["score"], 4)

    def test_critical_factor_caps_at_three(self):
        result = derive_score(
            {
                "geographic_completeness": 2,
                "scenario_richness": 5,
                "technical_accessibility": 5,
                "documentation_currency": 5,
                "licensing": 5,
                "integration_effort": 5,
            }
        )
        self.assertEqual(result["score"], 3)
        self.assertIn("critical_factor_cap_3", result["gates"])

    def test_five_gate(self):
        result = derive_score(
            {
                "geographic_completeness": 5,
                "scenario_richness": 5,
                "technical_accessibility": 5,
                "documentation_currency": 3,
                "licensing": 5,
                "integration_effort": 5,
            }
        )
        self.assertEqual(result["score"], 4)

    def test_evidence_scores_use_confirmed_access(self):
        country = verified_country()
        subscores, confidence, details = evidence_subscores(country)
        self.assertEqual(subscores["technical_accessibility"], 5)
        self.assertEqual(subscores["geographic_completeness"], 5)
        self.assertEqual(details["missing_families"], [])
        self.assertEqual(confidence, "high")

    def test_subscores_cannot_exceed_evidence_caps(self):
        country = unverified_country()
        with self.assertRaises(ContractError):
            enforce_evidence_caps(
                country,
                {
                    "geographic_completeness": 5,
                    "scenario_richness": 5,
                    "technical_accessibility": 5,
                    "documentation_currency": 5,
                    "licensing": 5,
                    "integration_effort": 5,
                },
            )


class ManifestTests(unittest.TestCase):
    def test_codex_can_mark_discovered(self):
        manifest = manifest_fixture()
        country = verified_country("BR")
        transitioned = transition_manifest(
            manifest, country, "discovered", "codex", "2026-06-24T15:00:00Z"
        )
        entry = next(item for item in transitioned["countries"] if item["iso2"] == "BR")
        self.assertEqual(entry["status"], "discovered")

    def test_codex_cannot_mark_verified(self):
        manifest = manifest_fixture(status="discovered")
        country = verified_country()
        with self.assertRaises(ContractError):
            transition_manifest(manifest, country, "verified", "codex")

    def test_cannot_build_unscored_country(self):
        manifest = manifest_fixture(status="verified")
        country = unverified_country()
        for source in country["sources"]:
            source["verification"] = {
                "status": "verified",
                "http_status": 200,
                "content_type": "application/xml",
                "final_url": source["links"]["service"],
                "evidence": strict_evidence(),
                "checked_at": "2026-06-24T15:00:00Z",
                "checked_by": "claude_code",
            }
        with self.assertRaises(ContractError):
            transition_manifest(manifest, country, "built", "claude_code")

    def test_built_can_be_invalidated_for_reaudit(self):
        manifest = manifest_fixture(status="built")
        manifest["countries"][0]["score"] = 4
        manifest["countries"][0]["confidence"] = "high"
        country = verified_country()
        transitioned = transition_manifest(
            manifest, country, "failed", "claude_code", "2026-06-24T16:00:00Z"
        )
        self.assertEqual(transitioned["countries"][0]["status"], "failed")


class ProbeTests(unittest.TestCase):
    def test_wms(self):
        result = probe_payload(fixture_bytes("wms.xml"), "application/xml")
        self.assertEqual(result["service_type"], "wms")
        self.assertEqual(result["layers"], ["flood_extent", "flood_depth"])
        self.assertEqual(result["bbox"], [-10.0, 49.0, 2.0, 61.0])

    def test_wfs(self):
        result = probe_payload(fixture_bytes("wfs.xml"), "application/xml")
        self.assertEqual(result["service_type"], "wfs")
        self.assertEqual(result["layers"], ["flood:extent"])
        self.assertIn("application/json", result["formats"])

    def test_atom(self):
        result = probe_payload(fixture_bytes("atom.xml"), "application/atom+xml")
        self.assertEqual(result["service_type"], "atom")
        self.assertEqual(result["layer_count"], 1)

    def test_arcgis(self):
        result = probe_payload(fixture_bytes("arcgis.json"), "application/json")
        self.assertEqual(result["service_type"], "arcgis_rest")
        self.assertEqual(result["crs"], ["EPSG:4326"])

    def test_ckan(self):
        result = probe_payload(
            fixture_bytes("ckan.json"),
            "application/json",
            "https://example.test/api/3/action/package_show",
        )
        self.assertEqual(result["service_type"], "ckan")
        self.assertEqual(result["formats"], ["GeoJSON", "GeoTIFF"])

    def test_ogc_api(self):
        result = probe_payload(fixture_bytes("ogc_api.json"), "application/json")
        self.assertEqual(result["service_type"], "ogc_api")
        self.assertEqual(result["bbox"], [-10, 49, 2, 61])

    def test_dtd_rejected(self):
        with self.assertRaises(ProbeError):
            probe_payload(fixture_bytes("malicious.xml"), "application/xml")

    def test_layer_list_is_truncated(self):
        layers = "".join(f"<Layer><Name>layer_{index}</Name></Layer>" for index in range(250))
        payload = f"<WMS_Capabilities><Capability><Layer>{layers}</Layer></Capability></WMS_Capabilities>".encode()
        result = probe_payload(payload, "application/xml")
        self.assertEqual(len(result["layers"]), MAX_LAYERS)
        self.assertEqual(result["layer_count"], 250)
        self.assertTrue(result["layers_truncated"])


class _Handler(BaseHTTPRequestHandler):
    protocol_version = "HTTP/1.1"

    def log_message(self, format, *args):
        pass

    def do_HEAD(self):
        if self.path == "/head405":
            self.send_response(405)
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        if self.path == "/redirect":
            self.send_response(302)
            self.send_header("Location", "/range")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        self.send_response(200 if self.path != "/bad" else 404)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Length", str(MAX_BYTES * 2))
        self.end_headers()

    def do_GET(self):
        if self.path == "/redirect":
            self.send_response(302)
            self.send_header("Location", "/range")
            self.send_header("Content-Length", "0")
            self.end_headers()
            return
        if self.path == "/bad":
            payload = b"missing"
            self.send_response(404)
        elif self.path == "/range":
            payload = b"x" * 128
            self.send_response(206)
            self.send_header("Content-Range", "bytes 0-127/100000")
        elif self.path in {"/ignore", "/head405"}:
            payload = b"x" * (MAX_BYTES * 2)
            self.send_response(200)
        else:
            payload = b"ok"
            self.send_response(200)
        self.send_header("Content-Type", "application/octet-stream")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)


class UrlValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        try:
            cls.server = ThreadingHTTPServer(("127.0.0.1", 0), _Handler)
        except PermissionError as exc:
            raise unittest.SkipTest("local sockets are unavailable in this sandbox") from exc
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f"http://127.0.0.1:{cls.server.server_port}"

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def test_redirect(self):
        result = validate_url(f"{self.base}/redirect")
        self.assertEqual(result["http_status"], 206)
        self.assertTrue(result["final_url"].endswith("/range"))

    def test_blocked_head_still_gets(self):
        result = validate_url(f"{self.base}/head405")
        self.assertEqual(result["head_status"], 405)
        self.assertEqual(result["http_status"], 200)

    def test_ignored_range_is_bounded(self):
        result = validate_url(f"{self.base}/ignore")
        self.assertEqual(result["bytes"], MAX_BYTES)
        self.assertFalse(result["range_honored"])

    def test_http_error(self):
        result = validate_url(f"{self.base}/bad")
        self.assertEqual(result["http_status"], 404)

    def test_non_http_scheme_is_rejected(self):
        result = validate_url("file:///etc/passwd")
        self.assertIsNone(result["http_status"])
        self.assertIn("HTTP(S)", result["error"])


class VerificationTests(unittest.TestCase):
    def test_dead_delivery_link_fails_even_when_primary_is_live(self):
        source = source_fixture()

        def result_for(url, timeout):
            live = url == source["links"]["primary"]
            return {
                "http_status": 200 if live else 404,
                "content_type": "text/html",
                "final_url": url,
                "bytes": 100,
                "head_status": 200 if live else 404,
                "range_honored": False,
                "error": None if live else "HTTPError",
            }

        audit = {
            "outcome": "confirmed",
            "access_class": "service",
            "authority_confirmed": True,
            "dataset_identity_confirmed": True,
            "human_usable": True,
            "selected_role": "service",
            "confirmed": strict_evidence()["confirmed"],
            "reason": "Expected flood WMS.",
        }
        with patch("verify_pending.validate_url", side_effect=result_for):
            verification, _ = verify_source(source, audit=audit)
        self.assertEqual(verification["status"], "failed")
        self.assertEqual(verification["evidence"]["outcome"], "lead")

    def test_service_claim_requires_successful_capability_probe(self):
        source = source_fixture()
        link_result = {
            "http_status": 200,
            "content_type": "application/xml",
            "final_url": source["links"]["service"],
            "bytes": 100,
            "head_status": 200,
            "range_honored": True,
            "error": None,
        }
        with patch("verify_pending.validate_url", return_value=link_result), patch(
            "verify_pending.probe_url", side_effect=ProbeError("malformed capability response")
        ):
            verification, last_update = verify_source(
                source,
                audit={
                    "outcome": "confirmed",
                    "access_class": "service",
                    "authority_confirmed": True,
                    "dataset_identity_confirmed": True,
                    "human_usable": True,
                    "selected_role": "service",
                    "confirmed": strict_evidence()["confirmed"],
                    "reason": "Expected flood service.",
                },
            )
        self.assertEqual(verification["status"], "failed")
        self.assertEqual(verification["evidence"]["outcome"], "lead")
        self.assertIsNone(last_update)

    def test_probe_output_is_bounded_in_verification_evidence(self):
        source = source_fixture()
        link_result = {
            "http_status": 200,
            "content_type": "application/xml",
            "final_url": source["links"]["service"],
            "bytes": 100,
            "head_status": 200,
            "range_honored": True,
            "error": None,
        }
        probe_result = {
            "service_type": "wms",
            "layer_count": 250,
            "layers_truncated": True,
            "layers": [f"flood_layer_{index}" for index in range(200)],
            "crs": [f"EPSG:{index}" for index in range(100)],
            "formats": [f"format/{index}" for index in range(100)],
            "bbox": [-10, 49, 2, 61],
            "declared_update": "2026-06-01",
        }
        with patch("verify_pending.validate_url", return_value=link_result), patch(
            "verify_pending.probe_url", return_value=probe_result
        ):
            verification, last_update = verify_source(
                source,
                audit={
                    "outcome": "confirmed",
                    "access_class": "service",
                    "authority_confirmed": True,
                    "dataset_identity_confirmed": True,
                    "human_usable": True,
                    "selected_role": "service",
                    "confirmed": strict_evidence()["confirmed"],
                    "reason": "Flood layers confirmed.",
                },
            )
        self.assertEqual(verification["status"], "verified")
        self.assertEqual(len(verification["evidence"]["capabilities"]["layers"]), 25)
        self.assertEqual(len(verification["evidence"]["capabilities"]["crs"]), 20)
        self.assertEqual(last_update, "2026-06-01")

    def test_generic_homepage_returning_200_fails(self):
        source = source_fixture()
        source["links"]["service"] = None
        result = {
            "http_status": 200,
            "content_type": "text/html",
            "final_url": source["links"]["primary"],
            "bytes": 100,
            "range_honored": False,
            "error": None,
        }
        with patch("verify_pending.validate_url", return_value=result):
            verification, _ = verify_source(
                source,
                audit={
                    "outcome": "lead",
                    "access_class": "generic_portal",
                    "selected_role": "primary",
                    "reason": "Agency homepage; no dataset identified.",
                },
            )
        self.assertEqual(verification["status"], "failed")
        self.assertEqual(verification["evidence"]["access_class"], "generic_portal")

    def test_dataset_viewer_with_browser_evidence_passes(self):
        source = source_fixture()
        source["links"]["service"] = None
        result = {
            "http_status": 200,
            "content_type": "text/html",
            "final_url": source["links"]["primary"],
            "bytes": 100,
            "range_honored": False,
            "error": None,
        }
        with patch("verify_pending.validate_url", return_value=result):
            verification, _ = verify_source(
                source,
                audit={
                    "outcome": "confirmed",
                    "access_class": "viewer",
                    "authority_confirmed": True,
                    "dataset_identity_confirmed": True,
                    "human_usable": True,
                    "selected_role": "primary",
                    "confirmed": strict_evidence()["confirmed"],
                    "reason": "Flood depth layer is visible and selectable.",
                    "browser": {
                        "page_title": "Flood Hazard Viewer",
                        "observed_product": "Flood depth",
                        "access_action": "Opened map and selected flood layer",
                        "final_url": source["links"]["primary"],
                    },
                },
            )
        self.assertEqual(verification["status"], "verified")
        self.assertEqual(verification["evidence"]["access_class"], "viewer")

    def test_valid_wms_without_flood_layers_fails(self):
        source = source_fixture()
        result = {
            "http_status": 200,
            "content_type": "application/xml",
            "final_url": source["links"]["service"],
            "bytes": 100,
            "range_honored": True,
            "error": None,
        }
        with patch("verify_pending.validate_url", return_value=result), patch(
            "verify_pending.probe_url",
            return_value={
                "service_type": "wms",
                "layer_count": 1,
                "layers": ["administrative_boundaries"],
                "crs": ["EPSG:4326"],
                "formats": ["image/png"],
                "bbox": None,
                "declared_update": None,
            },
        ):
            verification, _ = verify_source(
                source,
                audit={
                    "outcome": "confirmed",
                    "access_class": "service",
                    "authority_confirmed": True,
                    "dataset_identity_confirmed": True,
                    "human_usable": True,
                    "selected_role": "service",
                    "confirmed": strict_evidence()["confirmed"],
                    "reason": "Expected flood service.",
                },
            )
        self.assertEqual(verification["status"], "failed")
        self.assertIn("no recognizably flood-related layers", verification["evidence"]["reason"])

    def test_html_download_fails(self):
        source = source_fixture()
        source["links"]["service"] = None
        source["links"]["download"] = "https://example.test/download"

        def result_for(url, timeout):
            return {
                "http_status": 200,
                "content_type": "text/html",
                "final_url": url,
                "bytes": 100,
                "range_honored": False,
                "error": None,
            }

        with patch("verify_pending.validate_url", side_effect=result_for):
            verification, _ = verify_source(
                source,
                audit={
                    "outcome": "confirmed",
                    "access_class": "download",
                    "authority_confirmed": True,
                    "dataset_identity_confirmed": True,
                    "human_usable": True,
                    "selected_role": "download",
                    "confirmed": strict_evidence()["confirmed"],
                    "reason": "Expected download.",
                },
            )
        self.assertEqual(verification["status"], "failed")
        self.assertIn("non-data response", verification["evidence"]["reason"])


class BuildTests(unittest.TestCase):
    def test_build_is_deterministic_and_excludes_gb(self):
        brazil = verified_country()
        first = build_markdown([brazil])
        second = build_markdown([copy.deepcopy(brazil)])
        self.assertEqual(first, second)
        self.assertIn("Brazil", first)
        self.assertNotIn("United Kingdom", first)

    def test_human_review_findings_are_rendered(self):
        brazil = verified_country()
        findings = {
            "items": [
                {
                    "iso2": "BR",
                    "id": "BR-ANA-001",
                    "problem": "Endpoint remains unavailable",
                    "request": "Confirm source with the publisher",
                    "status": "human_review",
                }
            ]
        }
        rendered = build_markdown([brazil], findings)
        self.assertIn("Human review required", rendered)
        self.assertIn("Confirm source with the publisher", rendered)

    def test_unverified_material_record_fails_lint(self):
        country = verified_country()
        country["sources"][0]["verification"] = {
            "status": "unverified",
            "http_status": None,
            "content_type": None,
            "final_url": None,
            "evidence": None,
            "checked_at": None,
            "checked_by": None,
        }
        self.assertTrue(any("unverified" in error for error in lint_country(country)))

    def test_restricted_label_must_be_explicit(self):
        country = verified_country()
        country["sources"][0]["notes"] = "Restricted access."
        self.assertTrue(any("restricted" in error for error in lint_country(country)))

    def test_leads_are_clickable_and_unavailable_urls_are_plain_text(self):
        country = verified_country()
        lead = copy.deepcopy(country["sources"][0])
        lead["id"] = "BR-LEAD-001"
        lead["links"]["service"] = None
        lead["verification"] = {
            "status": "failed",
            "http_status": 200,
            "content_type": "text/html",
            "final_url": lead["links"]["primary"],
            "evidence": {
                **strict_evidence(
                    access_class="generic_portal",
                    outcome="lead",
                    selected_role="primary",
                    selected_url=lead["links"]["primary"],
                    reason="Generic portal.",
                ),
                "authority_confirmed": True,
                "dataset_identity_confirmed": False,
                "human_usable": False,
            },
            "checked_at": "2026-06-24T15:00:00Z",
            "checked_by": "claude_code",
        }
        dead = copy.deepcopy(country["sources"][0])
        dead["id"] = "BR-DEAD-001"
        dead_url = "https://example.test/missing"
        dead["links"] = {"primary": dead_url, "service": None, "download": None}
        dead["verification"] = {
            "status": "failed",
            "http_status": 404,
            "content_type": "text/html",
            "final_url": dead_url,
            "evidence": {
                **strict_evidence(
                    access_class="unavailable",
                    outcome="unavailable",
                    selected_role=None,
                    selected_url=None,
                    reason="HTTP 404.",
                ),
                "authority_confirmed": False,
                "dataset_identity_confirmed": False,
                "human_usable": False,
            },
            "checked_at": "2026-06-24T15:00:00Z",
            "checked_by": "claude_code",
        }
        country["sources"].extend([lead, dead])
        rendered = build_markdown([country])
        self.assertIn("Reachable investigation leads", rendered)
        self.assertIn(f"[Open]({lead['links']['primary']})", rendered)
        self.assertIn("Unavailable candidates", rendered)
        self.assertIn(f"`{dead_url}`", rendered)
        self.assertNotIn(f"]({dead_url})", rendered)

    def test_confirmed_table_uses_evidence_not_candidate_claims(self):
        country = verified_country()
        country["sources"][0]["formats"] = ["Imaginary format"]
        rendered = build_markdown([country])
        self.assertIn("WMS, GeoTIFF", rendered)
        self.assertNotIn("Imaginary format", rendered)

    def test_website_root_strips_path_query_and_fragment(self):
        self.assertEqual(
            website_root("https://example.test/maps/view?id=7#layers"),
            "https://example.test/",
        )

    def test_website_directory_keeps_all_sources_and_deduplicates_roots(self):
        country = verified_country()
        second = copy.deepcopy(country["sources"][0])
        second["id"] = "BR-ANA-002"
        second["native_name"] = "Second Flood Dataset"
        second["links"] = {
            "primary": "https://example.test/catalogue/flood",
            "service": None,
            "download": None,
        }
        country["sources"].append(second)
        directory = website_directory(country)
        example = next(
            entry for entry in directory if entry["root"] == "https://example.test/"
        )
        self.assertEqual(example["source_ids"], ["BR-ANA-001", "BR-ANA-002"])
        self.assertEqual(
            example["titles"],
            ["Synthetic Flood Hazard Dataset", "Second Flood Dataset"],
        )
        self.assertIn("primary", example["roles"])
        self.assertIn("service", example["roles"])

    def test_portal_guide_preserves_existing_rows_and_all_country_terms(self):
        country = verified_country()
        rendered = build_markdown([country])
        self.assertIn("Portal search guide and website roots", rendered)
        self.assertIn("[example.test](https://example.test/)", rendered)
        self.assertIn("Synthetic Flood Hazard Dataset", rendered)
        for term in portal_search_terms("BR"):
            self.assertIn(f"`{term}`", rendered)
        self.assertIn("### Confirmed dataset access", rendered)

    def test_non_english_countries_have_native_term_glosses(self):
        for iso2 in (
            "BR",
            "IN",
            "DE",
            "CN",
            "CA",
            "FR",
            "MX",
            "MY",
            "PL",
            "JP",
            "BE",
            "IT",
            "CH",
            "IE",
            "TH",
            "SE",
            "AT",
            "AE",
            "ZA",
            "KR",
        ):
            self.assertTrue(portal_search_glosses(iso2), iso2)

    def test_native_terms_render_with_english_meanings(self):
        country = verified_country()
        rendered = build_markdown([country])
        self.assertIn("Native-language term guide", rendered)
        self.assertIn("`mapa de inundação` — flood / inundation map", rendered)
        self.assertIn("Paste the native term into the portal", rendered)


class NotebookTests(unittest.TestCase):
    def test_append_and_render(self):
        with tempfile.TemporaryDirectory() as temporary:
            log_path = Path(temporary) / "events.jsonl"
            notebook_path = Path(temporary) / "LAB_NOTEBOOK.md"
            log_event(
                "codex",
                "test",
                "Recorded a test.",
                details={"passed": True},
                timestamp="2026-06-24T15:00:00Z",
                log_path=log_path,
                notebook_path=notebook_path,
            )
            events = read_events(log_path)
            self.assertEqual(len(events), 1)
            self.assertEqual(notebook_path.read_text(), render_notebook(events))

    def test_raw_payload_fields_are_rejected(self):
        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaises(NotebookError):
                log_event(
                    "codex",
                    "test",
                    "Bad log event.",
                    details={"raw_payload": "<xml/>"},
                    log_path=Path(temporary) / "events.jsonl",
                    notebook_path=Path(temporary) / "LAB_NOTEBOOK.md",
                )


if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""Deterministically build the human-readable readiness report."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit, urlunsplit

from common import CONFIG_PATH, ContractError, DATA_DIR, is_http_url, load_json, validate_path
from lab_notebook import log_event
from verification_evidence import (
    access_class,
    confirmed_metadata,
    evidence_for,
    reachable_lead,
    strict_verified,
    unavailable,
)

COUNTRY_CONFIG = load_json(CONFIG_PATH)["countries"]

# Short English glosses help a reviewer understand what native-language terms
# to paste into portal search boxes. The source-language text remains unchanged.
SEARCH_TERM_GLOSSES = {
    "map llifogydd": "flood map",
    "perygl llifogydd": "flood hazard",
    "mapa de inundação": "flood / inundation map",
    "perigo de inundação": "flood hazard",
    "mancha de inundação": "inundation extent",
    "profundidade": "depth",
    "velocidade": "velocity",
    "tempo de retorno": "return period",
    "inundação costeira": "coastal flooding",
    "cota de inundação litoral": "coastal flood elevation",
    "mapa de risco costeiro": "coastal risk map",
    "बाढ़ मानचित्र": "flood map",
    "बाढ़ जोखिम": "flood risk",
    "Hochwassergefahrenkarte": "flood-hazard map",
    "Überschwemmungsgebiet": "flood / inundation zone",
    "Überflutungstiefe": "inundation depth",
    "Fließgeschwindigkeit": "flow velocity",
    "Wiederkehrintervall": "return interval",
    "Starkregengefahrenkarte": "heavy-rain hazard map",
    "Starkregen Hinweiskarte": "heavy-rain advisory map",
    "Oberflächenwasser Überflutung": "surface-water flooding",
    "洪水风险图": "flood-risk map",
    "洪水淹没图": "flood-inundation map",
    "淹没深度": "inundation depth",
    "流速": "flow velocity",
    "重现期": "return period",
    "城市内涝风险图": "urban-waterlogging risk map",
    "内涝": "urban waterlogging",
    "carte des zones inondables": "flood-zone map",
    "profondeur d'inondation": "inundation depth",
    "période de retour": "return period",
    "carte aléa inondation": "flood-hazard map",
    "zone inondable": "flood-prone zone",
    "hauteur d'eau": "water depth",
    "vitesse d'écoulement": "flow velocity",
    "mapa de peligro de inundación": "flood-hazard map",
    "zona inundable": "flood-prone zone",
    "profundidad de inundación": "inundation depth",
    "velocidad": "velocity",
    "periodo de retorno": "return period",
    "peta bahaya banjir": "flood-hazard map",
    "peta genangan banjir": "flood-inundation map",
    "kedalaman banjir": "flood depth",
    "halaju banjir": "flood velocity",
    "tempoh ulangan": "return period",
    "mapa zagrożenia powodziowego": "flood-hazard map",
    "obszar zalewowy": "inundation area",
    "głębokość wody": "water depth",
    "prędkość przepływu": "flow velocity",
    "okres powtarzalności": "return period",
    "mapa zagrożenia powodzią opadową": "rainfall-flood hazard map",
    "powódź miejska": "urban flooding",
    "洪水ハザードマップ": "flood-hazard map",
    "浸水想定区域": "designated inundation area",
    "浸水深": "inundation depth",
    "再現期間": "return period",
    "overstromingsgevaarkaart": "flood-hazard map",
    "overstromingsdiepte": "flood depth",
    "mappa pericolosità alluvioni": "flood-hazard map",
    "area allagabile": "floodable area",
    "tirante idrico": "water depth",
    "velocità": "velocity",
    "tempo di ritorno": "return period",
    "allagamento urbano": "urban flooding",
    "pericolosità da pioggia intensa": "heavy-rain hazard",
    "rischio allagamenti": "flooding risk",
    "carte des dangers crues": "river-flood hazard map",
    "mappa pericolo alluvione": "flood-hazard map",
    "Wiederkehrperiode": "return period",
    "léarscáil tuilte": "flood map",
    "แผนที่เสี่ยงน้ำท่วม": "flood-risk map",
    "พื้นที่น้ำท่วม": "flooded / inundation area",
    "ความลึกน้ำท่วม": "flood depth",
    "ความเร็วการไหล": "flow velocity",
    "คาบอุบัติซ้ำ": "return period",
    "แผนที่น้ำท่วมชายฝั่ง": "coastal-flood map",
    "översvämningskarta": "flood map",
    "översvämningsrisk": "flood risk",
    "vattendjup": "water depth",
    "flödeshastighet": "flow velocity",
    "återkomsttid": "return period",
    "skyfallskartering": "cloudburst mapping",
    "skyfall översvämning": "cloudburst flooding",
    "Überflutungsfläche": "inundation extent",
    "Wassertiefe": "water depth",
    "Jährlichkeit": "annual exceedance / return frequency",
    "خريطة مخاطر الفيضانات": "flood-risk map",
    "مناطق الغمر": "inundation zones",
    "عمق الفيضان": "flood depth",
    "سرعة الجريان": "flow velocity",
    "فترة التكرار": "return period",
    "oorstromingskaart": "flood map",
    "vloedlyn": "floodline",
    "홍수위험지도": "flood-risk map",
    "침수예상도": "expected-inundation map",
    "침수심": "inundation depth",
    "유속": "flow velocity",
    "재현기간": "return period",
}


def md(value: Any) -> str:
    if value is None:
        return "—"
    return str(value).replace("|", "\\|").replace("\n", " ")


def link(label: str, url: str | None) -> str:
    return f"[{md(label)}]({url})" if url else "—"


# Internal pipeline actor names are an implementation detail and are neutralized
# in the public report. Ordered so multi-word phrases resolve before bare tokens.
_ACTOR_REPLACEMENTS = (
    ("automated Codex rediscovery round", "automated rediscovery round"),
    ("permitted Codex rediscovery round", "permitted rediscovery round"),
    ("Codex rediscovery", "automated rediscovery"),
    ("Codex discovery", "automated discovery"),
    ("Codex", "the automated discovery agent"),
    ("Claude Code", "the automated verification agent"),
    ("Claude", "the agent"),
)


def sanitize(text: str) -> str:
    for old, new in _ACTOR_REPLACEMENTS:
        text = text.replace(old, new)
    return text


def lint_country(country: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for source in country["sources"]:
        prefix = f"{country['iso2']}:{source['id']}"
        verification = source["verification"]
        if source["is_material"] and verification["status"] == "unverified":
            errors.append(f"{prefix}: material source is unverified")
        if verification["status"] != "unverified" and not verification["checked_at"]:
            errors.append(f"{prefix}: terminal source lacks verification date")
        if verification["status"] != "unverified" and not evidence_for(source).get(
            "standard"
        ):
            errors.append(f"{prefix}: terminal source lacks dataset-resolved evidence")
        if verification["status"] == "verified" and not strict_verified(source):
            errors.append(
                f"{prefix}: verified source lacks confirmed dataset-specific access"
            )
        for role, url in source["links"].items():
            if url and not is_http_url(url):
                errors.append(f"{prefix}: malformed {role} URL")
        normalized = " ".join(
            [
                source["delivery_mode"],
                source["license"] or "",
                source["notes"],
            ]
        ).lower()
        required_flags = {
            "viewer only": "viewer_only",
            "pdf only": "pdf_only",
            "address only": "address_only",
            "request only": "request_only",
            "paid": "paid",
            "restricted": "restricted",
        }
        for phrase, flag in required_flags.items():
            if phrase in normalized and flag not in source["access_constraints"]:
                errors.append(f"{prefix}: access condition {flag} is not explicitly flagged")
        if verification["status"] == "superseded":
            evidence = verification["evidence"] or {}
            if not (evidence.get("replacement_id") or evidence.get("superseded_by")):
                errors.append(f"{prefix}: superseded source lacks evidence.replacement_id")
        if source["supersedes_id"] and "replacement" not in source["notes"].lower():
            errors.append(f"{prefix}: replacement source must explain supersession in notes")
    return errors


def load_inputs(
    data_dir: Path, allow_partial: bool
) -> tuple[list[dict[str, Any]], dict[str, Any], dict[str, Any]]:
    config = load_json(CONFIG_PATH)
    manifest = validate_path(data_dir / "manifest.json")
    findings = validate_path(data_dir / "findings.json")
    entries = {entry["iso2"]: entry for entry in manifest["countries"]}
    countries: list[dict[str, Any]] = []
    failures: list[str] = []

    for iso2 in config["final_order"]:
        path = data_dir / f"{iso2}.json"
        if not path.exists():
            if not allow_partial:
                failures.append(f"missing final country artifact: {path}")
            continue
        country = validate_path(path)
        if country["report_scope"] != "final":
            failures.append(f"{iso2}: final-order artifact must have report_scope=final")
            continue
        entry = entries.get(iso2)
        if not entry:
            failures.append(f"{iso2}: missing manifest entry")
        elif not allow_partial and entry["status"] not in {"verified", "built"}:
            failures.append(
                f"{iso2}: manifest status must be verified or built, got {entry['status']}"
            )
        failures.extend(lint_country(country))
        countries.append(country)

    unresolved = [item for item in findings["items"] if item["status"] == "unresolved"]
    if unresolved and not allow_partial:
        failures.append(
            "unresolved findings remain: "
            + ", ".join(f"{item['iso2']}:{item['id']}" for item in unresolved)
        )
    human_review_keys = {
        (item["iso2"], item["id"])
        for item in findings["items"]
        if item["status"] == "human_review"
    }
    for country in countries:
        for source in country["sources"]:
            if (
                source["is_material"]
                and source["verification"]["status"] == "failed"
                and (country["iso2"], source["id"]) not in human_review_keys
                and not allow_partial
            ):
                failures.append(
                    f"{country['iso2']}:{source['id']}: failed material source must "
                    "be represented by a human_review finding"
                )
    if not countries:
        failures.append("no final-scope country artifacts are available")
    if failures:
        raise ContractError("\n".join(failures))
    return countries, manifest, findings


def coverage_summary(country: dict[str, Any]) -> str:
    return country["coverage_model"].replace("_", " ")


def best_delivery(country: dict[str, Any]) -> str:
    verified = [
        source
        for source in country["sources"]
        if strict_verified(source) and not source["is_fallback"]
    ]
    if not verified:
        return "No confirmed dataset access"
    modes = list(dict.fromkeys(access_label(source) for source in verified))
    return ", ".join(modes[:3])


def source_flags(source: dict[str, Any]) -> str:
    flags = list(source["access_constraints"])
    if source["is_fallback"]:
        flags.append("fallback")
    if not source["is_material"]:
        flags.append("non-material")
    if source["supersedes_id"]:
        flags.append(f"replaces {source['supersedes_id']}")
    flags.append(source["verification"]["status"])
    return ", ".join(flags)


ACCESS_LABELS = {
    "service": "Service (OGC)",
    "api": "API",
    "download": "Direct download",
    "viewer": "Interactive viewer",
    "document": "Map document",
    "dataset_page": "Dataset page",
    "request_only": "Request only",
    "generic_portal": "Generic portal",
    "catalogue_search": "Catalogue search",
    "restricted": "Restricted",
    "ambiguous": "Ambiguous",
    "wrong_product": "Wrong product",
    "unavailable": "Unavailable",
}


def access_label(source: dict[str, Any]) -> str:
    return ACCESS_LABELS.get(access_class(source), "Ambiguous")


def is_direct(source: dict[str, Any]) -> bool:
    return access_class(source) in {"service", "api", "download"}


HAZARD_FAMILIES = ("fluvial", "coastal", "surface_water")
HAZARD_LABELS = {
    "fluvial": "Fluvial (river)",
    "coastal": "Coastal",
    "surface_water": "Surface water (pluvial)",
}


def source_tiers(
    country: dict[str, Any],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[dict[str, Any]]]:
    confirmed = [s for s in country["sources"] if strict_verified(s)]
    leads = [s for s in country["sources"] if reachable_lead(s)]
    unavail = [s for s in country["sources"] if unavailable(s)]
    return confirmed, leads, unavail


def hazard_coverage(country: dict[str, Any]) -> dict[str, str]:
    """Per family: 'confirmed' (in a confirmed source), 'unconfirmed' (only in a
    lead/broken source), or 'none' (absent from every candidate)."""
    status: dict[str, str] = {}
    for family in HAZARD_FAMILIES:
        confirmed = any(
            family in s["flood_types"] for s in country["sources"] if strict_verified(s)
        )
        present = any(family in s["flood_types"] for s in country["sources"])
        status[family] = "confirmed" if confirmed else ("unconfirmed" if present else "none")
    return status


def needs_review_count(country: dict[str, Any]) -> int:
    return sum(1 for s in country["sources"] if s["is_material"] and not strict_verified(s))


def failure_detail(source: dict[str, Any]) -> str:
    """Short, human-readable reason a candidate link is unavailable."""
    reason = evidence_for(source).get("reason")
    http = source["verification"].get("http_status")
    if http:
        return f"failed (HTTP {http})" + (f": {reason}" if reason else "")
    return "failed (unreachable)" + (f": {reason}" if reason else "")


def confirmed_list(source: dict[str, Any], key: str) -> str:
    values = confirmed_metadata(source).get(key) or []
    return md(", ".join(str(value) for value in values)) if values else "unknown"


def confirmed_text(source: dict[str, Any], key: str) -> str:
    value = confirmed_metadata(source).get(key)
    return md(value) if value not in {None, ""} else "unknown"


def website_root(url: str) -> str:
    """Return a scheme-and-host root suitable for portal navigation."""
    parsed = urlsplit(url)
    return urlunsplit((parsed.scheme, parsed.netloc, "/", "", ""))


def directory_status(source: dict[str, Any]) -> str:
    if strict_verified(source):
        return "confirmed dataset access"
    if reachable_lead(source):
        return "investigation lead"
    if source["verification"]["status"] == "superseded":
        return "superseded"
    return "unavailable candidate"


def website_directory(country: dict[str, Any]) -> list[dict[str, Any]]:
    """Group every report URL by website root without removing full links."""
    grouped: dict[str, dict[str, Any]] = {}

    def add_url(
        url: str,
        *,
        source_id: str,
        agency: str,
        title: str,
        role: str,
        status: str,
    ) -> None:
        root = website_root(url)
        entry = grouped.setdefault(
            root,
            {
                "root": root,
                "source_ids": [],
                "agencies": [],
                "titles": [],
                "roles": [],
                "statuses": [],
            },
        )
        for key, value in (
            ("source_ids", source_id),
            ("agencies", agency),
            ("titles", title),
            ("roles", role),
            ("statuses", status),
        ):
            if value not in entry[key]:
                entry[key].append(value)

    for source in country["sources"]:
        for role, url in source["links"].items():
            if not url:
                continue
            add_url(
                url,
                source_id=source["id"],
                agency=source["agency"],
                title=source["native_name"],
                role=role,
                status=directory_status(source),
            )
        verification = source["verification"]
        for role, url in (
            ("verification final", verification.get("final_url")),
            ("selected access", evidence_for(source).get("selected_url")),
        ):
            if url:
                add_url(
                    url,
                    source_id=source["id"],
                    agency=source["agency"],
                    title=source["native_name"],
                    role=role,
                    status=directory_status(source),
                )
    for region in country["top_regions"]:
        add_url(
            region["pop_source_url"],
            source_id=f"population: {region['name']}",
            agency=region["pop_source"],
            title=f"{region['name']} population",
            role="population source",
            status="supporting citation",
        )
    return [grouped[root] for root in sorted(grouped)]


def portal_search_terms(iso2: str) -> list[str]:
    return list(COUNTRY_CONFIG[iso2]["search_terms"])


def portal_search_glosses(iso2: str) -> list[tuple[str, str]]:
    return [
        (term, SEARCH_TERM_GLOSSES[term])
        for term in portal_search_terms(iso2)
        if term in SEARCH_TERM_GLOSSES
    ]


def render_portal_guide(country: dict[str, Any]) -> list[str]:
    general_terms = portal_search_terms(country["iso2"])
    glosses = portal_search_glosses(country["iso2"])
    languages = ", ".join(COUNTRY_CONFIG[country["iso2"]]["official_languages"])
    lines = [
        "",
        "### Portal search guide and website roots",
        "",
        "Use the exact dataset names in the directory first. If that fails, try "
        "the local-language flood terms below in the site's search box, map-layer "
        "catalogue, or metadata search. Website-root links are navigation aids; "
        "they are not themselves confirmation that a dataset is available.",
        "",
        f"**Portal languages:** {md(languages)}",
        "",
        "**Country search phrases:** "
        + " · ".join(f"`{md(term)}`" for term in general_terms),
    ]
    if glosses:
        lines.extend(
            [
                "",
                "**Native-language term guide:** "
                + " · ".join(
                    f"`{md(term)}` — {md(gloss)}" for term, gloss in glosses
                )
                + ". Paste the native term into the portal; the English text is "
                "only a meaning guide.",
            ]
        )
    lines.extend(
        [
            "",
            "| Website root | Related source IDs | Publisher(s) | Search this site for | Link roles | Current classification |",
            "|---|---|---|---|---|---|",
        ]
    )
    for entry in website_directory(country):
        search_titles = "<br>".join(f"`{md(title)}`" for title in entry["titles"])
        lines.append(
            "| "
            + " | ".join(
                [
                    link(urlsplit(entry["root"]).netloc, entry["root"]),
                    md(", ".join(entry["source_ids"])),
                    md("; ".join(entry["agencies"])),
                    search_titles,
                    md(", ".join(entry["roles"])),
                    md(", ".join(entry["statuses"])),
                ]
            )
            + " |"
        )
    return lines


def render_snapshot(country: dict[str, Any]) -> list[str]:
    confirmed, leads, unavail = source_tiers(country)
    direct = sum(is_direct(s) for s in confirmed)
    coverage = hazard_coverage(country)
    confirmed_fams = [HAZARD_LABELS[f] for f, st in coverage.items() if st == "confirmed"]
    open_fams = [HAZARD_LABELS[f] for f, st in coverage.items() if st != "confirmed"]
    hazard_line = "**Hazard families confirmed:** " + (", ".join(confirmed_fams) or "none")
    if open_fams:
        hazard_line += f". **Not yet confirmed:** {', '.join(open_fams)}"
    return [
        "### What we have",
        "",
        f"- **Confirmed dataset access:** {len(confirmed)} source(s) "
        f"({direct} direct service/API/download, "
        f"{len(confirmed) - direct} viewer / map document / dataset page).",
        f"- **Investigation leads:** {len(leads)} reachable portal(s) that still "
        "need the dataset located by hand.",
        f"- **Unavailable:** {len(unavail)} broken or unreachable candidate(s).",
        f"- {hazard_line}.",
        f"- **Best confirmed access:** {md(best_delivery(country))}.",
        "",
    ]


def render_next_steps(country: dict[str, Any]) -> list[str]:
    confirmed, leads, unavail = source_tiers(country)
    coverage = hazard_coverage(country)
    unconfirmed_fams = [HAZARD_LABELS[f] for f, st in coverage.items() if st == "unconfirmed"]
    missing_fams = [HAZARD_LABELS[f] for f, st in coverage.items() if st == "none"]
    steps: list[str] = []
    if unconfirmed_fams:
        steps.append(
            f"Confirm {', '.join(unconfirmed_fams)} coverage — a candidate exists "
            "but its dataset is not yet confirmed."
        )
    if missing_fams:
        steps.append(
            f"Find {', '.join(missing_fams)} coverage, or document in the summary "
            "above why the family does not apply."
        )
    if leads:
        steps.append(
            f"Work the {len(leads)} investigation lead(s): use the portal search "
            "guide below to locate the dataset behind each portal, then confirm a "
            "usable service, download, viewer, or dataset page."
        )
    material_unavail = sum(1 for s in unavail if s["is_material"])
    if material_unavail:
        steps.append(
            f"Resolve {material_unavail} broken or unreachable material source(s) "
            "flagged for human review (see the Unavailable table and the "
            "Human review required section)."
        )
    if country["deferred_regions"]:
        steps.append(
            f"Extend beyond the {len(country['top_regions'])}-region pilot to the "
            f"{len(country['deferred_regions'])} deferred region(s)."
        )
    verify_licences = sum(
        1
        for s in confirmed
        if s.get("license") and "verify" in s["license"].lower()
    )
    if verify_licences:
        steps.append(
            f"Confirm licensing for {verify_licences} confirmed source(s) whose "
            "licence is still marked \"verify\"."
        )
    if not steps:
        steps.append(
            "No outstanding gaps identified; spot-check the confirmed sources "
            "before relying on them."
        )
    lines = ["### What comes next", ""]
    lines.extend(f"{index}. {step}" for index, step in enumerate(steps, 1))
    lines.append("")
    return lines


def render_country(country: dict[str, Any]) -> list[str]:
    status_bits = [f"**Coverage model:** {md(coverage_summary(country))}"]
    if country["score_provisional"]:
        status_bits.append("**Scope:** provisional — top-five-region pilot")
    status_bits.append(f"**Confidence in completeness:** {country['confidence']}")
    lines = [
        f"## {country['country_name']} ({country['iso2']})",
        "",
        " · ".join(status_bits),
        "",
        country["fragmentation_summary"],
        "",
    ]
    lines.extend(render_snapshot(country))

    if country["top_regions"]:
        lines.extend(
            [
                "",
                "### Population-priority regions",
                "",
                "| Rank | Region | Population | Year | Source |",
                "|---:|---|---:|---:|---|",
            ]
        )
        for region in country["top_regions"]:
            lines.append(
                f"| {region['rank']} | {md(region['name'])} | "
                f"{region['population']:,} | {region['pop_year']} | "
                f"{link(region['pop_source'], region['pop_source_url'])} |"
            )
    if country["deferred_regions"]:
        lines.extend(
            [
                "",
                f"**Deferred regions:** {', '.join(md(item) for item in country['deferred_regions'])}",
            ]
        )

    lines.extend(render_portal_guide(country))

    verified = [source for source in country["sources"] if strict_verified(source)]
    leads = [source for source in country["sources"] if reachable_lead(source)]
    unavailable_sources = [
        source for source in country["sources"] if unavailable(source)
    ]
    verified.sort(key=lambda source: (not is_direct(source), source["id"]))

    lines.extend(
        [
            "",
            "### Confirmed dataset access",
            "",
            "Each clickable link below was confirmed to identify an authoritative "
            "flood dataset and provide a usable service, download, viewer, map "
            "document, or dataset-specific page.",
            "",
            "| ID | Jurisdiction / agency | Dataset | Confirmed flood type | Confirmed scenarios | Confirmed coverage | Confirmed formats | Confirmed licence | Access | Link | Verified | Flags | Evidence |",
            "|---|---|---|---|---|---|---|---|---|---|---|---|---|",
        ]
    )
    if not verified:
        lines.append("| _none_ | — | — | — | — | — | — | — | — | — | — | — | — |")
    for source in verified:
        evidence = evidence_for(source)
        selected_url = evidence["selected_url"]
        selected_role = evidence["selected_role"] or "primary"
        links = link(selected_role.title(), selected_url)
        dataset = md(source["native_name"])
        if source["native_name"] != source["english_name"]:
            dataset += f"<br>_{md(source['english_name'])}_"
        verification = source["verification"]
        verified_text = md(verification["checked_at"][:10]) if verification["checked_at"] else "—"
        lines.append(
            "| "
            + " | ".join(
                [
                    md(source["id"]),
                    f"{md(source['jurisdiction'])}<br>{md(source['agency'])}",
                    dataset,
                    confirmed_list(source, "flood_types"),
                    confirmed_list(source, "scenarios"),
                    confirmed_text(source, "coverage"),
                    confirmed_list(source, "formats"),
                    confirmed_text(source, "license"),
                    md(access_label(source)),
                    links or "—",
                    verified_text,
                    md(source_flags(source)),
                    md(evidence.get("reason")),
                ]
            )
            + " |"
        )

    if leads:
        lines.extend(
            [
                "",
                "### Reachable investigation leads",
                "",
                "These links resolve, but they are generic portals, catalogue "
                "searches, restricted/request-only paths, ambiguous products, or "
                "otherwise lack confirmed dataset-specific access. They are "
                "clickable for investigation but excluded from scoring.",
                "",
                "| ID | Jurisdiction / agency | Candidate | Access | Link | Reason | Tracking |",
                "|---|---|---|---|---|---|---|",
            ]
        )
        for source in leads:
            evidence = evidence_for(source)
            selected_url = (
                evidence.get("selected_url")
                or source["verification"].get("final_url")
                or source["links"].get("primary")
            )
            tracking = "human review" if source["is_material"] else "non-material candidate"
            lines.append(
                "| "
                + " | ".join(
                    [
                        md(source["id"]),
                        f"{md(source['jurisdiction'])}<br>{md(source['agency'])}",
                        md(source["native_name"]),
                        md(access_label(source)),
                        link("Open", selected_url),
                        md(evidence.get("reason")),
                        tracking,
                    ]
                )
                + " |"
            )
    if unavailable_sources:
        lines.extend(
            [
                "",
                "### Unavailable candidates",
                "",
                "These links did not resolve. URLs are plain text and non-clickable.",
                "",
                "| ID | Jurisdiction / agency | Candidate | Status | Candidate URL | Tracking |",
                "|---|---|---|---|---|---|",
            ]
        )
        for source in unavailable_sources:
            primary = source["links"].get("primary")
            url_text = f"`{md(primary)}`" if primary else "—"
            tracking = "human review" if source["is_material"] else "non-material candidate"
            lines.append(
                "| "
                + " | ".join(
                    [
                        md(source["id"]),
                        f"{md(source['jurisdiction'])}<br>{md(source['agency'])}",
                        md(source["native_name"]),
                        md(failure_detail(source)),
                        url_text,
                        tracking,
                    ]
                )
                + " |"
            )
    lines.append("")
    lines.extend(render_next_steps(country))
    return lines


def link_coverage_stats(countries: list[dict[str, Any]]) -> dict[str, int]:
    stats = {
        "total": 0,
        "confirmed": 0,
        "leads": 0,
        "unavailable": 0,
        "http_404": 0,
        "direct": 0,
        "human_access": 0,
    }
    for country in countries:
        for source in country["sources"]:
            stats["total"] += 1
            if strict_verified(source):
                stats["confirmed"] += 1
                if is_direct(source):
                    stats["direct"] += 1
                else:
                    stats["human_access"] += 1
            elif reachable_lead(source):
                stats["leads"] += 1
            else:
                stats["unavailable"] += 1
                if source["verification"].get("http_status") == 404:
                    stats["http_404"] += 1
    return stats


def build_markdown(
    countries: list[dict[str, Any]], findings: dict[str, Any] | None = None
) -> str:
    lines = [
        "# Twenty-Country Flood Data Readiness Review",
        "",
        "This document is generated from verified, versioned JSON artifacts. "
        "Do not edit it directly.",
        "",
        "> **Dataset-resolved links.** A source is confirmed only when the "
        "authoritative flood dataset is identifiable and usable through a working "
        "service, download, viewer, map document, or dataset-specific page. "
        "Generic portals and agency homepages are retained only as investigation "
        "leads. This report describes what exists and how usable it is; it does "
        "not assign an overall readiness grade.",
        "",
        "## How to use this report",
        "",
        "Every country section has the same shape. Work through it top to bottom:",
        "",
        "1. **What we have** — a snapshot of how many sources have confirmed "
        "dataset access, how many are leads, and which flood-hazard families "
        "(fluvial, coastal, surface water) are actually confirmed.",
        "2. **Source tables**, which sort every candidate into three tiers:",
        "   - **Confirmed dataset access** — the link reaches a usable flood "
        "dataset (service, API, download, viewer, map document, or dataset page). "
        "Start here.",
        "   - **Reachable investigation leads** — the link works but lands on a "
        "generic portal, catalogue, or ambiguous/restricted product; the dataset "
        "still has to be located by hand.",
        "   - **Unavailable candidates** — the link did not resolve (shown as "
        "non-clickable text).",
        "3. **Access column** — distinguishes machine-readable endpoints "
        "(Service / API / Direct download) from things that need a person "
        "(Interactive viewer, Map document, Dataset page).",
        "4. **Portal search guide** — website roots plus the exact native-language "
        "search terms to paste into each portal to turn a lead into a confirmed "
        "source.",
        "5. **What comes next** — the concrete actions still outstanding for that "
        "country.",
        "",
        "**Evaluating a source further.** When you open a candidate, judge it on "
        "the same factors used throughout:",
        "",
        "- **Geographic completeness** — national, or only some regions?",
        "- **Scenario richness** — multiple return periods (e.g., 10 / 100 / "
        "500-year) and depth/velocity, or a single layer?",
        "- **Technical accessibility** — a service or download you can pull, or a "
        "viewer you can only look at?",
        "- **Documentation currency** — when was it last updated?",
        "- **Licensing** — is reuse permitted? Many licences are still marked "
        "\"verify\".",
        "- **Integration effort** — format, coordinate system, and language "
        "barriers to actually using it.",
        "",
        "## Country overview",
        "",
        "One row per country. The hazard columns show whether a **confirmed** "
        "dataset exists for each family (confirmed / unconfirmed / none); "
        "\"unconfirmed\" means a candidate exists but its dataset is not yet "
        "confirmed. \"Needs review\" counts material sources that are not yet "
        "confirmed (leads plus broken links). Provisional pilots cover only the "
        "top five regions and are flagged in each country section.",
        "",
        "| Country | Fluvial | Coastal | Surface water | Confirmed sources | Leads | Needs review | Coverage model |",
        "|---|---|---|---|---:|---:|---:|---|",
    ]
    for country in countries:
        confirmed, leads, _ = source_tiers(country)
        coverage = hazard_coverage(country)
        name = md(country["country_name"])
        if country["score_provisional"]:
            name += " *"
        lines.append(
            f"| {name} | {coverage['fluvial']} | {coverage['coastal']} | "
            f"{coverage['surface_water']} | {len(confirmed)} | {len(leads)} | "
            f"{needs_review_count(country)} | {md(coverage_summary(country))} |"
        )
    stats = link_coverage_stats(countries)
    lines.extend(
        [
            "",
            "\\* Provisional — coverage assessed on a top-five-region pilot.",
            "",
            "## Link coverage and caveats",
            "",
            f"Across the {len(countries)} countries, **{stats['total']} "
            f"candidate sources** were audited: **{stats['confirmed']} have "
            f"confirmed dataset access**, **{stats['leads']} are reachable "
            f"investigation leads**, and **{stats['unavailable']} are unavailable** "
            f"(including {stats['http_404']} confirmed HTTP 404s). Confirmed access "
            f"includes **{stats['direct']} service/API/download endpoint(s)** and "
            f"**{stats['human_access']} usable viewers, map documents, or "
            "dataset-specific pages**.",
            "",
        ]
    )
    for country in countries:
        lines.extend(render_country(country))
    human_review = [
        item
        for item in (findings or {}).get("items", [])
        if item["status"] == "human_review"
    ]
    if human_review:
        lines.extend(
            [
                "## Human review required",
                "",
                "These items remained unresolved after the single permitted "
                "Codex rediscovery round.",
                "",
                "| Country | Source | Problem | Requested review |",
                "|---|---|---|---|",
            ]
        )
        for item in human_review:
            lines.append(
                f"| {item['iso2']} | {md(item['id'])} | {md(item['problem'])} | "
                f"{md(item['request'])} |"
            )
        lines.append("")
    lines.extend(methodology_section())
    return sanitize("\n".join(lines).rstrip() + "\n")


def methodology_section() -> list[str]:
    return [
        "## How this table was generated (AI agentic search)",
        "",
        "This review was produced by an AI agentic-search pipeline, not by manual "
        "literature review. The working brief given to the agents was:",
        "",
        "> For each of twenty priority countries, identify the authoritative "
        "government (or official intergovernmental) sources that publish flood "
        "**hazard** mapping, prioritizing jurisdictions by population. Every "
        "country's source set must cover each applicable flood-hazard family — "
        "**fluvial** (river), **coastal**, and **surface water** (pluvial / "
        "stormwater) — or explicitly record why a family does not apply. For each "
        "source capture the publishing agency, dataset, flood types, scenarios "
        "(return periods), spatial coverage and resolution, formats, licence, and "
        "access/delivery mode, with a working link. Describe each country's data "
        "readiness and flag every source whose dataset cannot be confirmed.",
        "",
        "The pipeline runs as two independent agent roles with a strict separation "
        "of duties, so that the agent making claims is never the agent that "
        "confirms them:",
        "",
        "1. **Discovery.** A discovery agent runs bounded web search per country "
        "(capped numbers of searches, page reads, and service-capability probes) "
        "and emits *unverified* candidate sources covering the required hazard "
        "families. It may not assign scores or verification status.",
        "2. **Verification.** A separate verification agent checks reachability, "
        "publisher authority, dataset identity, and human usability. Services are "
        "capability-probed for relevant flood layers; downloads must return a data "
        "response rather than HTML; dynamic viewers and dataset pages require a "
        "bounded browser audit. Generic portals, catalogue searches, restricted "
        "or request-only paths, and ambiguous products are retained as leads but "
        "are not verified. Raw service payloads are read only by dedicated "
        "validation tools and never enter model reasoning.",
        "3. **Assessment.** Each country is described across six explicit factors "
        "— geographic completeness, scenario richness, technical accessibility, "
        "documentation currency, licensing, and integration effort — used as "
        "evaluation lenses (see \"How to use this report\") rather than collapsed "
        "into a single grade. The emphasis is on what exists and how usable it is.",
        "4. **Findings and human review.** Any material source that fails "
        "verification generates a structured finding. One automated rediscovery "
        "round is permitted to find a replacement; anything still unresolved is "
        "escalated to the **Human review required** section rather than dropped or "
        "silently guessed.",
        "5. **Build.** This report is rendered deterministically from versioned, "
        "schema-validated JSON artifacts; the prose is generated, the underlying "
        "facts are not.",
        "",
        "Because discovery is automated and the live web changes, links can break "
        "between verification and reading. The **Verification** columns and the "
        "human-review section are the authoritative record of what was confirmed "
        "and when.",
        "",
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", default=str(DATA_DIR))
    parser.add_argument("--output", default="global_flood_data_readiness.md")
    parser.add_argument("--allow-partial", action="store_true")
    parser.add_argument("--check", action="store_true", help="Check output is current")
    args = parser.parse_args()
    try:
        countries, _, findings = load_inputs(Path(args.data_dir), args.allow_partial)
        content = build_markdown(countries, findings)
        output = Path(args.output)
        if args.check:
            existing = output.read_text(encoding="utf-8") if output.exists() else ""
            if existing != content:
                raise ContractError(f"{output} is missing or out of date")
        else:
            output.write_text(content, encoding="utf-8")
            log_event(
                "claude_code",
                "build",
                "Built the deterministic Markdown readiness report.",
                details={
                    "country_count": len(countries),
                    "output": str(output),
                    "bytes": len(content.encode("utf-8")),
                },
            )
        print(f"built {output} from {len(countries)} final country artifact(s)")
        return 0
    except (ContractError, OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())

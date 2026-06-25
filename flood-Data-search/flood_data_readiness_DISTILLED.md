# Flood Data Readiness — Distilled, Actionable Read (20 countries)

**Companion to** `global_flood_data_readiness.md`. That report is deliberately conservative:
a source counts only when the exact flood dataset is confirmed reachable, and everything
else is held at "unconfirmed." This distilled version keeps the same verified evidence but
gives an **actionable confidence call** — it treats a strong, reachable national flood
portal as *probably usable* rather than unproven, and tells you where to start.

> **Read this as engineering judgment, not pipeline verification.** Anywhere this file says
> "workable" off a lead that the strict report left unconfirmed, that is a human call about
> likelihood, made to be useful. The strict report remains the system of record. Open
> questions that would change the call are flagged inline with **⚠**.

Excludes the GB fixture. Based on 154 audited candidates across 20 countries
(44 confirmed, 53 reachable leads, 57 unavailable as of 2026-06-24).

---

## Bottom line

- **13 of 20 countries are usable today or within one verification pass.** Western/Central
  Europe, Japan, and Korea give you confirmed national or near-national flood hazard maps.
- **The hard limit is delivery, not existence.** Of 44 confirmed sources, **only 1 is a true
  service/API/download endpoint** — the other 43 are interactive viewers, map documents, or
  dataset pages. (Spot-checking added **one more real API — France's Géorisques `gaspar/azi`
  JSON endpoint**.) If your use case needs a layer you can *pull and process*, almost everywhere
  you will be screen-scraping a viewer or filing a data request, not hitting an API. **⚠ This
  is the single biggest open question for any integration project.**
- **Every license reads "verify."** Not one source has confirmed reuse terms. Assume nothing
  is open until checked. **⚠**
- **There is a universal floor: JRC Global River Flood Hazard Maps** (EU JRC, `id-0054`)
  is reachable for every country here and is genuinely downloadable. For the 5 weakest
  countries it is effectively the baseline fluvial dataset until a national source is run down.

---

## Tiered country list

### Tier A — Use today (confirmed, national or near-national)

| Country | Best entry point | What you actually get | Open question |
|---|---|---|---|
| **Germany** | LAWA / state flood hazard & risk maps (+ NRW, Bavaria, BW) | Fluvial + coastal + surface water, multiple return periods, strong technical access | ⚠ Licensing "verify"; federal — confirmed on top-5 states, not all 16 |
| **Japan** | MLIT Hazard Map Portal (`disaportal`) | Fluvial + coastal + surface water + tsunami nationwide viewer | ⚠ Scenario richness thin (score 2/5); download path unclear, viewer-first |
| **Austria** | HORA national hazard map + WISA | Fluvial + surface water, full national coverage, HQ30/100/300 | ⚠ Address-only lookup on HORA; no bulk download confirmed |
| **Sweden** | MSB Swedish Flood Portal + cloudburst mapping | Fluvial + coastal + surface water, national | ⚠ Documentation currency low (2/5) |
| **Ireland** | OPW CFRAM maps + National Flood Hazard Archive + pluvial | Fluvial + coastal + surface water + historic, national | ⚠ Pluvial WMS may be CC-BY-NC-ND (non-commercial) |
| **Poland** | ISOK Hydroportal flood hazard maps | Fluvial + coastal, national | ⚠ No surface-water product; geographic completeness 3/5 |

### Tier B — Workable within one verification pass (confirmed for part of the country; national completeness is the open item)

| Country | Best entry point | What you actually get | Open question |
|---|---|---|---|
| **Belgium** | Flanders Flood Maps + Wallonia portal | Fluvial + coastal + surface water, but split by region | ⚠ Two separate regional systems; integration effort high (2/5) |
| **Canada** | Quebec Geo-Floods, Alberta, Manitoba maps | Fluvial (+coastal QC, +surface water MB), province-by-province | ⚠ No national layer; only 3 provinces confirmed, 4 candidates broken |
| **France** | **Géorisques REST API** (`api/v1/gaspar/azi`) + Nouvelle-Aquitaine | **Confirmed machine-readable flood-zone API** (spot-checked 2026-06-25, returns JSON per commune) + regional maps | ⚠ API covers flood-zone atlas (AZI/TRI), not depth grids; scenario richness still 2/5 |
| **Italy** | ISPRA IdroGEO national platform | Fluvial + coastal national viewer; Po district detail | ⚠ Surface water unconfirmed; viewer-first |
| **Switzerland** | Surface-runoff hazard map + cantonal maps (ZH/VD/AG/SG) | Surface water national; fluvial via cantons | ⚠ No national coastal (landlocked, expected); fluvial is cantonal patchwork |
| **Korea** | Flood Risk Map Information System + **National Safety Map (SafeMap) viewer** | Fluvial + surface water, nationally unified; SafeMap viewer spot-checked reachable (2026-06-25) | ⚠ Coastal unconfirmed; SafeMap OpenAPI exists but is **service-key-gated** (registration required) |
| **India** | ISRO Bhuvan Flood Services + Bihar FMIS | Fluvial + surface water national viewer; Bihar detail | ⚠ Bhuvan is viewer/event-based, not a static hazard layer; 5 broken candidates |
| **Mexico** | CDMX Risk Atlas (confirmed) | Mexico City solid; no confirmed national hazard layer | ⚠ Spot-checked 2026-06-25: CONAGUA **SINA is reservoir-storage monitoring, not hazard maps** — drop as a hazard source; lean on JRC global for national fluvial |

### Tier C — Fallback-first (no confirmed national dataset; named leads worth chasing)

| Country | Realistic plan | Strongest lead to run down | Open question |
|---|---|---|---|
| **China** | Beijing waterlogging map confirmed; else JRC global | MWR National Flood Risk Map Programme; Shandong/Sichuan provincial | ⚠ Access likely restricted; national programme may not be public |
| **Malaysia** | JRC global baseline; hazard layer still unlocated | **NAHRIM** flood/climate products (publicinfobanjir is *monitoring only*) | ⚠ Spot-checked 2026-06-25: publicinfobanjir is real-time rainfall/river-level nowcasting (WordPress, no hazard service), **not** return-period hazard maps. Strict caution held — chase NAHRIM/JPS instead |
| **Thailand** | JRC global baseline; hazard layer still unlocated | DWR Mekhala GIS; DMCR coastal DB (thaiwater.net is *monitoring only*) | ⚠ Spot-checked 2026-06-25: thaiwater.net is a real-time monitoring SPA, **not** return-period hazard maps. Chase DWR/DMCR instead |
| **Brazil** | JRC global baseline + state geoportals | SP DataGEO, MG IDE-Sisema, SGB GeoSGB | ⚠ National hazard mapping is fragmented to states; no federal layer |
| **South Africa** | JRC global baseline + provincial DM | SARVA atlas; KZN / Eastern Cape / Limpopo floodlines | ⚠ Provincial sites reachable but dataset access unconfirmed |
| **UAE** | JRC global baseline (genuinely thin nationally) | Ras Al Khaimah municipal geodata; NCM warnings | ⚠ Weakest of the set — no flood *hazard* dataset surfaced, only warnings/municipal |

---

## Cross-cutting open questions (decide these before committing)

1. **Pull vs. look.** ⚠ Only 1 of 44 confirmed sources is a machine-readable endpoint. If you
   need rasters/vectors in a pipeline, budget for WMS scraping, manual export, or formal data
   requests almost everywhere. The "confirmed" countries are confirmed as *viewable*, not
   *downloadable*.
2. **Licensing is uniformly unresolved.** ⚠ Every license is "verify." Several EU sources lean
   on the EEA reuse policy (open) via WISE Floods Directive — that is your safest open-data
   path for fluvial+coastal across the EU members here (AT, SE, IE, PL, BE, FR, IT, DE).
3. **Federal-country scope is provisional.** ⚠ DE, JP, CA, IT, CH, FR, MX, IN, CN, BR, MY, ZA
   were assessed on a **top-five-region pilot**. A confirmed source in those countries proves
   the *region*, not the whole nation. Tier A/B placement assumes the pattern extends; verify
   for regions outside the pilot.
4. **Coastal and surface-water gaps.** ⚠ Coastal is unconfirmed for KR, CH(expected), and most
   Tier C; surface water is missing for PL and unconfirmed for FR/IT. Don't assume all three
   hazard families exist just because fluvial does.
5. **The strict report's "leads" are not noise — but half are the wrong product class.** ⚠
   Spot-checking 5 leads (2026-06-25) promoted **2** (France Géorisques JSON API, Korea SafeMap
   viewer) and rejected **3** — publicinfobanjir, ThaiWater, and CONAGUA SINA all turned out to
   be **real-time monitoring / nowcasting portals (water levels, rainfall, reservoir storage),
   not return-period hazard maps**. Lesson: a reachable "national flood portal" is often live
   gauge data, not a hazard dataset. Verify product *type*, not just reachability, before
   promoting a lead.

---

## Suggested next actions (ranked by ROI)

1. **Chase hazard-map sources, not monitoring portals.** 5 leads spot-checked: ✓ France
   Géorisques API and ✓ Korea SafeMap viewer confirmed; ✗ Malaysia publicinfobanjir, ✗ Thailand
   thaiwater.net, ✗ Mexico SINA are all monitoring-only. Remaining real targets to run down:
   Malaysia NAHRIM/JPS, Thailand DWR Mekhala + DMCR coastal, Mexico national hazard layer.
2. **Resolve licensing for the EU bloc via WISE/EEA** — one decision unlocks open fluvial+coastal
   for 8 countries.
3. **Decide the delivery requirement.** If APIs are mandatory, re-scope: the current evidence
   says you are mostly getting viewers, and that changes which countries are truly "ready."
4. **For Tier C, default to JRC global now**, treat national sources as enrichment rather than
   blockers.

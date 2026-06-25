# Flood Data Readiness Lab Notebook

Append-only audit history shared by Codex, Claude Code, and human reviewers.
The structured source is `logs/lab_notebook.jsonl`; regenerate this view
with `python3 tools/lab_notebook.py render`.

Raw service payloads are deliberately excluded.

## 2026-06-24T14:43:38Z — decision

**Actor:** codex

Frozen the two-pass contract and stage gate. GB is an end-to-end fixture and is excluded from the final ranking.

- contract version: 1.0.0
- final country count: 20
- fixture: GB
- pipeline: Codex discovery -> Claude Code verification

## 2026-06-24T14:55:26Z — implementation

**Actor:** codex

Implemented the contract validator, bounded URL validator, capability prober, append-only delta application, manifest transitions, scoring, verification, and deterministic document builder.

- capability payload limit bytes: 20971520
- dependencies: Python standard library only
- url sample limit bytes: 65536

## 2026-06-24T14:55:26Z — discovery · GB

**Actor:** codex

Produced the unverified GB fixture from the existing catalogue plus focused official-page inspection. No link is marked verified.

- capability probes: 0
- page reads: 4
- searches: 0
- source count: 12
- stop reason: Good-enough fixture coverage across the four devolved publishers

## 2026-06-24T14:55:26Z — handoff · GB

**Actor:** codex

Stopped at the GB pilot gate as required. The twenty-country discovery run has not started.

- next actor: claude_code
- required actions: ["verify every GB candidate", "score the fixture", "profile budget and token use", "human review before final-country discovery"]

## 2026-06-24T15:01:49Z — test

**Actor:** toolkit

Completed the local acceptance suite successfully.

- contract validation: passed
- network fixture: loopback-only HTTP server
- result: passed
- tests: 34

## 2026-06-24T15:03:34Z — test

**Actor:** toolkit

Completed the hardened acceptance suite successfully.

- contract version: 1.0.0
- coverage: ["contract", "ownership", "manifest", "findings", "scoring", "WMS", "WFS", "ArcGIS REST", "CKAN", "ATOM", "OGC API", "bounded URL behavior", "document build", "lab notebook"]
- result: passed
- tests: 37

## 2026-06-24T15:05:29Z — test

**Actor:** toolkit

Completed the final acceptance suite successfully.

- candidate immutability: fingerprinted and enforced
- contract validation: passed
- result: passed
- tests: 39

## 2026-06-24T15:05:29Z — handoff · GB

**Actor:** codex

Toolkit and GB discovery fixture are ready for the independent Claude Code pilot.

- final country discovery started: False
- manifest status: discovered
- next step: Run Claude Code verification, scoring, budget profiling, and human review
- source count: 12
- verification status: all unverified

## 2026-06-24T15:34:08Z — decision · GB

**Actor:** claude_code

Starting independent Pass 2 verification pilot for the GB fixture. Treating all 12 candidates as unproven; verifying only via the bounded toolkit (validate_url + probe_capabilities) and never ingesting raw payloads. Failure-investigation budget: <=3 targeted searches per failed record, <=12 total for GB.

- candidates: 12
- scope: GB fixture only; final 20 countries remain blocked
- search budget per record: 3
- search budget total: 12
- toolkit: ["validate_url.py", "probe_capabilities.py"]

## 2026-06-24T15:34:08Z — test

**Actor:** claude_code

Pre-flight gate passed: contract validation, lab-notebook sync check, candidate guard, and full unit suite all green before any verification.

- candidate guard GB: passed
- contract validation: passed (3 artifacts)
- notebook check: in_sync
- unit result: OK
- unit tests: 39

## 2026-06-24T15:36:47Z — verification · GB · GB-EA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:35:50Z
- content type: text/xml
- final url: https://environment.data.gov.uk/spatialdata/flood-map-for-planning-flood-zones/wms
- http status: 200

## 2026-06-24T15:36:47Z — verification · GB · GB-EA-002

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T15:35:58Z
- content type: text/html
- final url: https://environment.data.gov.uk/spatialdata/risk-of-flooding-from-rivers-and-sea/wms
- http status: 404

## 2026-06-24T15:36:47Z — verification · GB · GB-EA-003

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T15:36:04Z
- content type: text/html
- final url: https://environment.data.gov.uk/spatialdata/risk-of-flooding-from-surface-water/wms
- http status: 404

## 2026-06-24T15:36:47Z — verification · GB · GB-EA-004

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:09Z
- content type: text/html
- final url: https://environment.data.gov.uk/dataset/e5b38de2-99b3-44ee-b10c-b244926878ef
- http status: 200

## 2026-06-24T15:36:47Z — verification · GB · GB-SEPA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:12Z
- content type: application/x-zip-compressed
- final url: https://map.sepa.org.uk/atom/flood/SEPA_River_Flood_Maps_v3_0.zip
- http status: 206

## 2026-06-24T15:36:47Z — verification · GB · GB-SEPA-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:14Z
- content type: application/x-zip-compressed
- final url: https://map.sepa.org.uk/atom/flood/SEPA_Coastal_Flood_Maps_v3_0.zip
- http status: 206

## 2026-06-24T15:36:47Z — verification · GB · GB-SEPA-003

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:16Z
- content type: application/x-zip-compressed
- final url: https://map.sepa.org.uk/atom/flood/SEPA_Surface_Water_Flood_Maps_EXTENT_v3_0.zip
- http status: 206

## 2026-06-24T15:36:47Z — verification · GB · GB-SEPA-004

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:19Z
- content type: application/x-zip-compressed
- final url: https://map.sepa.org.uk/atom/flood/SEPA_Surface_Water_Flood_Maps_DEPTH_M_v3_0.zip
- http status: 206

## 2026-06-24T15:36:47Z — verification · GB · GB-NRW-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:26Z
- content type: text/xml
- final url: https://datamap.gov.wales/capabilities/layer/2355/?ows_service=wms
- http status: 200

## 2026-06-24T15:36:47Z — verification · GB · GB-NRW-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:34Z
- content type: text/xml
- final url: https://datamap.gov.wales/capabilities/layer/2066/?ows_service=wms
- http status: 200

## 2026-06-24T15:36:47Z — verification · GB · GB-NRW-003

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:44Z
- content type: text/xml
- final url: https://datamap.gov.wales/capabilities/layergroup/889/?ows_service=wms
- http status: 200

## 2026-06-24T15:36:47Z — verification · GB · GB-DFI-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:36:47Z
- content type: text/html
- final url: https://dfi-ni.maps.arcgis.com/apps/webappviewer/index.html?id=fd6c0a01b07840269a50a2f596b3daf6
- http status: 206

## 2026-06-24T15:41:46Z — verification · GB

**Actor:** claude_code

Verification pass complete: 10/12 candidates verified, 2 failed. Both failures are England EA records whose WMS service slug returns HTTP 404 while the catalogue primary page is live (200). Root cause: EA decommissioned legacy RoFRS/RoFSW WMS slugs and migrated to NaFRA2 (Flood Zones produced under NaFRA2 from 25 March 2025).

- failed: 2
- failed ids: ["GB-EA-002", "GB-EA-003"]
- failure mode: service WMS slug 404; primary 200
- verified: 10

## 2026-06-24T15:41:46Z — decision · GB

**Actor:** claude_code

Failure investigation used bounded toolkit + targeted searches. 3 of 12 total searches used (GB-EA-002: 2, GB-EA-003: 1). Confirmed via bounded validate_url/probe_capabilities that legacy slugs 404 and the NaFRA2 rivers-and-sea and surface-water WMS endpoints are live valid WMS (6 layers, EPSG:4326/4258/27700). Appending Claude Code-owned round-2 replacements GB-EA-005 (supersedes GB-EA-002) and GB-EA-006 (supersedes GB-EA-003); originals marked superseded. No candidate fields rewritten.

- legacy slug status: 404
- nafra2 wms status: 200
- replacements: [{"new": "GB-EA-005", "supersedes": "GB-EA-002"}, {"new": "GB-EA-006", "supersedes": "GB-EA-003"}]
- search budget per record: 3
- search budget total: 12
- searches used GB-EA-002: 2
- searches used GB-EA-003: 1
- searches used total: 3

## 2026-06-24T15:42:29Z — verification · GB

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: ["GB-EA-005", "GB-EA-006"]
- country fields: []
- verification source ids: ["GB-EA-002", "GB-EA-003"]

## 2026-06-24T15:42:50Z — verification · GB · GB-EA-005

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:42:44Z
- content type: text/xml
- final url: https://environment.data.gov.uk/spatialdata/nafra2-risk-of-flooding-from-rivers-and-sea/wms
- http status: 200

## 2026-06-24T15:42:50Z — verification · GB · GB-EA-006

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T15:42:50Z
- content type: text/xml
- final url: https://environment.data.gov.uk/spatialdata/nafra2-risk-of-flooding-from-surface-water/wms
- http status: 200

## 2026-06-24T15:43:38Z — finding · GB · GB-EA-002

**Actor:** claude_code

WMS service endpoint spatialdata/risk-of-flooding-from-rivers-and-sea/wms returns HTTP 404 while the catalogue primary page is live (200). Legacy RoFRS WMS slug was decommissioned when the EA migrated the product to NaFRA2.

- evidence: {"failed_role": "service", "primary_http_status": 200, "probe": "wms/6 layers/EPSG:4326,4258,27700", "replacement_id": "GB-EA-005", "replacement_service": "https://environment.data.gov.uk/spatialdata/nafra2-risk-of-flooding-from-rivers-and-sea/wms", "replacement_verification": "verified", "searches_used": 2, "service_http_status": 404}
- request: Replacement GB-EA-005 points at the live NaFRA2 rivers-and-sea WMS (bounded-probe verified). Human review: confirm NaFRA2 is the accepted successor product for RoFRS in the readiness ranking.
- status: resolved

## 2026-06-24T15:43:38Z — finding · GB · GB-EA-003

**Actor:** claude_code

WMS service endpoint spatialdata/risk-of-flooding-from-surface-water/wms returns HTTP 404 while the catalogue primary page is live (200). Legacy RoFSW WMS slug was decommissioned under the NaFRA2 migration.

- evidence: {"failed_role": "service", "primary_http_status": 200, "probe": "wms/6 layers/EPSG:4326,4258,27700", "replacement_id": "GB-EA-006", "replacement_service": "https://environment.data.gov.uk/spatialdata/nafra2-risk-of-flooding-from-surface-water/wms", "replacement_verification": "verified", "searches_used": 1, "service_http_status": 404}
- request: Replacement GB-EA-006 points at the live NaFRA2 surface-water WMS (bounded-probe verified). Human review: confirm NaFRA2 surface-water service as successor to the decommissioned RoFSW endpoint.
- status: resolved

## 2026-06-24T15:43:55Z — decision · GB

**Actor:** claude_code

Assigned six explicit subscores for GB with rationale. geographic_completeness=5 (national products across all four devolved nations). scenario_richness=5 (multiple AEP/return-period bands, present-day + 2050s/2080s climate change, extent/depth/velocity via SEPA). technical_accessibility=4 (England/Scotland/Wales expose WMS/WFS/OGC API + geodatabase downloads; Northern Ireland is viewer/PDF only, no machine-readable feed). documentation_currency=4 (NaFRA2 current to 25 Mar 2025, SEPA v3.0, WMS declared updateSequence present; some downloads lack explicit dates). licensing=4 (OGL v3.0 for E/S/W; NI is Crown/OSNI restricted and may require paid commercial licence). integration_effort=3 (four separate publishers and delivery stacks require per-jurisdiction integration).

- confidence: high
- confidence rationale: 12/12 material sources verified by bounded machine evidence; only the NI machine-readability gap remains, which is a documented limitation not an unknown.
- subscores: {"documentation_currency": 4, "geographic_completeness": 5, "integration_effort": 3, "licensing": 4, "scenario_richness": 5, "technical_accessibility": 4}

## 2026-06-24T15:43:55Z — score · GB

**Actor:** claude_code

Derived country score 4/5 from explicit subscores.

- confidence: high
- gates: []
- mean: 4.166666666666667
- score provisional: False
- subscores: {"documentation_currency": 4, "geographic_completeness": 5, "integration_effort": 3, "licensing": 4, "scenario_richness": 5, "technical_accessibility": 4}

## 2026-06-24T15:44:04Z — manifest_transition · GB

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: high
- score: 4
- source count: 14
- status: verified

## 2026-06-24T15:45:23Z — test · GB

**Actor:** claude_code

Post-pilot test re-run: 33 pass, 6 fail (4 failures, 2 errors). All six are coupled to the pristine pre-pilot fixture snapshot, not toolkit regressions: they load the live data/GB.json and manifest and assert GB is still all-unverified, unscored, and discovered. The pilot intentionally advanced GB to verified/scored, so those preconditions no longer hold. Toolkit source code is unchanged; the pre-flight run before any mutation was 39/39 green. Recommendation for human review: the acceptance suite should load an immutable fixture copy rather than the live GB artifact so it stays runnable after the pilot.

- coupled tests: ["test_fixture_is_valid_and_unverified", "test_unverified_record_cannot_contain_evidence", "test_codex_cannot_mark_verified", "test_cannot_build_unscored_country", "test_candidate_mutation_and_deletion_are_rejected", "test_owned_append_can_be_frozen"]
- postpilot error: 2
- postpilot fail: 4
- postpilot pass: 33
- preflight: 39/39 pass
- root cause: tests assert pristine GB state on the live artifact; pilot advanced it
- toolkit code changed: False

## 2026-06-24T15:45:43Z — decision · GB

**Actor:** claude_code

Budget/token observations for the GB pilot. Targeted web searches: 3 of 12 total (cap respected; <=3/record). Bounded network calls: initial verify_pending ran HEAD+ranged-GET over 12 records (16 link checks) and auto-probed 4 live WMS services; failure investigation added 6 validate_url checks and 2 probe_capabilities probes; re-verify of the 2 replacements added 2 link checks + 2 probes. No raw service payloads entered model context (only distilled probe fields). Token cost concentrated in the upfront read of the 8-tool toolkit + 21KB GB.json; verification/scoring/manifest phases were cheap deterministic tool calls.

- bounded probes: ~8
- bounded validate url calls: ~24
- cost drivers: ["toolkit+schema read", "GB.json read", "3 web searches"]
- raw payloads into context: 0
- search cap total: 12
- searches used: 3

## 2026-06-24T15:45:43Z — handoff · GB

**Actor:** claude_code

GB Pass-2 verification pilot complete and ready for human review. 12/12 material sources verified by bounded machine evidence (10 original + 2 replacements); 2 legacy EA WMS records superseded by NaFRA2 replacements GB-EA-005/GB-EA-006. Score 4/5, confidence high, not provisional. Manifest GB -> verified. Two findings recorded (resolved) for the NaFRA2 migration. Final-twenty discovery and report build remain blocked pending human review.

- blocked: ["final_20_discovery", "report_build"]
- confidence: high
- findings open: 0
- findings resolved: 2
- manifest status: verified
- next actor: human
- review items: ["accept NaFRA2 as RoFRS/RoFSW successor", "acceptance suite couples to live GB fixture"]
- score: 4
- superseded: 2
- verified: 12

## 2026-06-24T15:51:07Z — decision · GB

**Actor:** human

Human delegated the NaFRA2 vs legacy RoFRS/RoFSW successor judgment to Claude Code (to be logged as a judgment call) and accepted Claude Code's recommendation to decouple the acceptance suite from the live GB fixture.

- accepted: decouple acceptance suite from live GB fixture
- authority: human
- delegated: NaFRA2 successor call

## 2026-06-24T15:51:07Z — decision · GB

**Actor:** claude_code

Judgment call (human-delegated): ACCEPT NaFRA2 as the authoritative current successor to the legacy RoFRS/RoFSW products. Basis: the legacy EA WMS slugs are decommissioned (HTTP 404); NaFRA2 is the Environment Agency national flood risk assessment that replaced them (Flood Zones produced under NaFRA2 from 25 Mar 2025); the NaFRA2 rivers-and-sea and surface-water WMS endpoints are live, valid WMS confirmed by bounded probe; product semantics (rivers/sea risk bands; surface-water risk bands) and OGL v3.0 licensing are preserved. Replacements GB-EA-005/GB-EA-006 stand; findings remain resolved. No further action needed for GB.

- call: accept NaFRA2 as RoFRS/RoFSW successor
- delegated by: human
- findings status: resolved
- legacy status: 404
- replacements: ["GB-EA-005", "GB-EA-006"]

## 2026-06-24T15:53:32Z — decision

**Actor:** claude_code

Human review of the GB pilot complete; pilot accepted. Parameters set for the final-twenty pass: (1) Claude Code verification failure-investigation budget is <=3 targeted web searches per failed record with NO per-country cap (bounded toolkit must still confirm any replacement). (2) Acceptance-suite decoupling from the live GB fixture is DEFERRED until after the twenty-country run. (3) Confirmed Codex has NOT yet run discovery for the 20 (data/ holds only GB; all 20 are planned/0 sources). Discovery is Codex's pass and must run before Claude Code verification can begin.

- codex discovery for 20: not started
- data files present: ["GB.json", "manifest.json", "findings.json"]
- next actor: codex
- test decoupling: deferred until after the 20
- verify search budget: <=3 per record, no country cap

## 2026-06-24T16:01:59Z — manifest_transition · BR

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 8
- status: discovered

## 2026-06-24T16:01:59Z — discovery · BR

**Actor:** codex

Completed bounded official-source discovery for Brazil.

- candidate count: 8
- capability probes: 0
- page reads: 4
- searches: 4
- top region pilot: True
- verification performed: False

## 2026-06-24T16:01:59Z — handoff · BR

**Actor:** codex

Brazil candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 22
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:02:07Z — manifest_transition · IN

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 9
- status: discovered

## 2026-06-24T16:02:07Z — discovery · IN

**Actor:** codex

Completed bounded official-source discovery for India.

- candidate count: 9
- capability probes: 0
- page reads: 3
- searches: 4
- top region pilot: True
- verification performed: False

## 2026-06-24T16:02:07Z — handoff · IN

**Actor:** codex

India candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 28
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:02:20Z — manifest_transition · DE

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 8
- status: discovered

## 2026-06-24T16:02:20Z — discovery · DE

**Actor:** codex

Completed bounded official-source discovery for Germany.

- candidate count: 8
- capability probes: 0
- page reads: 4
- searches: 4
- top region pilot: True
- verification performed: False

## 2026-06-24T16:02:20Z — handoff · DE

**Actor:** codex

Germany candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 11
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:02:33Z — manifest_transition · CN

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 8
- status: discovered

## 2026-06-24T16:02:33Z — discovery · CN

**Actor:** codex

Completed bounded official-source discovery for China.

- candidate count: 8
- capability probes: 0
- page reads: 3
- searches: 4
- top region pilot: True
- verification performed: False

## 2026-06-24T16:02:33Z — handoff · CN

**Actor:** codex

China candidate artifact is frozen and ready for Claude Code verification.

- access uncertainty: high
- deferred regions: 26
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:05:18Z — manifest_transition · CA

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 8
- status: discovered

## 2026-06-24T16:05:18Z — discovery · CA

**Actor:** codex

Completed bounded official-source discovery for Canada.

- candidate count: 8
- capability probes: 0
- page reads: 4
- searches: 4
- top region pilot: True
- verification performed: False

## 2026-06-24T16:05:18Z — handoff · CA

**Actor:** codex

Canada candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 8
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:05:25Z — manifest_transition · FR

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 8
- status: discovered

## 2026-06-24T16:05:25Z — discovery · FR

**Actor:** codex

Completed bounded official-source discovery for France.

- candidate count: 8
- capability probes: 0
- page reads: 4
- searches: 3
- top region pilot: True
- verification performed: False

## 2026-06-24T16:05:25Z — handoff · FR

**Actor:** codex

France candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 13
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:05:32Z — manifest_transition · MX

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 9
- status: discovered

## 2026-06-24T16:05:32Z — discovery · MX

**Actor:** codex

Completed bounded official-source discovery for Mexico.

- candidate count: 9
- capability probes: 0
- page reads: 4
- searches: 3
- top region pilot: True
- verification performed: False

## 2026-06-24T16:05:32Z — handoff · MX

**Actor:** codex

Mexico candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 27
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:05:40Z — manifest_transition · MY

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 9
- status: discovered

## 2026-06-24T16:05:41Z — discovery · MY

**Actor:** codex

Completed bounded official-source discovery for Malaysia.

- candidate count: 9
- capability probes: 0
- page reads: 3
- searches: 2
- top region pilot: True
- verification performed: False

## 2026-06-24T16:05:41Z — handoff · MY

**Actor:** codex

Malaysia candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 9
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:07:56Z — manifest_transition · PL

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 5
- status: discovered

## 2026-06-24T16:07:56Z — discovery · PL

**Actor:** codex

Completed bounded official-source discovery for Poland.

- candidate count: 5
- capability probes: 0
- page reads: 3
- searches: 2
- top region pilot: False
- verification performed: False

## 2026-06-24T16:07:56Z — handoff · PL

**Actor:** codex

Poland candidate artifact is frozen and ready for Claude Code verification.

- coverage model: nationally_unified
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:08:05Z — manifest_transition · JP

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 8
- status: discovered

## 2026-06-24T16:08:06Z — discovery · JP

**Actor:** codex

Completed bounded official-source discovery for Japan.

- candidate count: 8
- capability probes: 0
- page reads: 4
- searches: 2
- top region pilot: True
- verification performed: False

## 2026-06-24T16:08:06Z — handoff · JP

**Actor:** codex

Japan candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 42
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:08:16Z — manifest_transition · BE

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 6
- status: discovered

## 2026-06-24T16:08:16Z — discovery · BE

**Actor:** codex

Completed bounded official-source discovery for Belgium.

- candidate count: 6
- capability probes: 0
- page reads: 4
- searches: 2
- top region pilot: True
- verification performed: False

## 2026-06-24T16:08:16Z — handoff · BE

**Actor:** codex

Belgium candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 0
- manifest status: discovered
- regions covered: 3
- verification status: all unverified

## 2026-06-24T16:08:24Z — manifest_transition · IT

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 7
- status: discovered

## 2026-06-24T16:08:24Z — discovery · IT

**Actor:** codex

Completed bounded official-source discovery for Italy.

- basin authorities identified: 5
- candidate count: 7
- capability probes: 0
- page reads: 4
- searches: 2
- top region pilot: True
- verification performed: False

## 2026-06-24T16:08:24Z — handoff · IT

**Actor:** codex

Italy candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 15
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:10:31Z — manifest_transition · CH

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 7
- status: discovered

## 2026-06-24T16:10:31Z — discovery · CH

**Actor:** codex

Completed bounded official-source discovery for Switzerland.

- candidate count: 7
- capability probes: 0
- page reads: 4
- searches: 2
- top region pilot: True
- verification performed: False

## 2026-06-24T16:10:31Z — handoff · CH

**Actor:** codex

Switzerland candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 21
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:10:39Z — manifest_transition · IE

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 5
- status: discovered

## 2026-06-24T16:10:39Z — discovery · IE

**Actor:** codex

Completed bounded official-source discovery for Ireland.

- candidate count: 5
- capability probes: 0
- page reads: 3
- searches: 2
- top region pilot: False
- verification performed: False

## 2026-06-24T16:10:39Z — handoff · IE

**Actor:** codex

Ireland candidate artifact is frozen and ready for Claude Code verification.

- coverage model: nationally_unified
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:10:46Z — manifest_transition · TH

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 9
- status: discovered

## 2026-06-24T16:10:46Z — discovery · TH

**Actor:** codex

Completed bounded official-source discovery for Thailand.

- candidate count: 9
- capability probes: 0
- page reads: 3
- searches: 2
- top region pilot: True
- verification performed: False

## 2026-06-24T16:10:47Z — handoff · TH

**Actor:** codex

Thailand candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: remaining provinces
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:10:55Z — manifest_transition · SE

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 5
- status: discovered

## 2026-06-24T16:10:55Z — discovery · SE

**Actor:** codex

Completed bounded official-source discovery for Sweden.

- candidate count: 5
- capability probes: 0
- page reads: 3
- searches: 2
- top region pilot: False
- verification performed: False

## 2026-06-24T16:10:55Z — handoff · SE

**Actor:** codex

Sweden candidate artifact is frozen and ready for Claude Code verification.

- coverage model: nationally_unified
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:13:14Z — manifest_transition · AT

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 5
- status: discovered

## 2026-06-24T16:13:14Z — discovery · AT

**Actor:** codex

Completed bounded official-source discovery for Austria.

- candidate count: 5
- capability probes: 0
- page reads: 3
- searches: 2
- top region pilot: False
- verification performed: False

## 2026-06-24T16:13:14Z — handoff · AT

**Actor:** codex

Austria candidate artifact is frozen and ready for Claude Code verification.

- coverage model: nationally_unified
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:13:27Z — manifest_transition · AE

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 8
- status: discovered

## 2026-06-24T16:13:28Z — discovery · AE

**Actor:** codex

Completed bounded official-source discovery for the United Arab Emirates.

- candidate count: 8
- capability probes: 0
- page reads: 3
- public access uncertainty: high
- searches: 2
- top region pilot: True
- verification performed: False

## 2026-06-24T16:13:28Z — handoff · AE

**Actor:** codex

United Arab Emirates candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 2
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:13:36Z — manifest_transition · ZA

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 9
- status: discovered

## 2026-06-24T16:13:36Z — discovery · ZA

**Actor:** codex

Completed bounded official-source discovery for South Africa.

- candidate count: 9
- capability probes: 0
- page reads: 3
- searches: 2
- top region pilot: True
- verification performed: False

## 2026-06-24T16:13:36Z — handoff · ZA

**Actor:** codex

South Africa candidate artifact is frozen and ready for Claude Code verification.

- deferred regions: 4
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:13:51Z — manifest_transition · KR

**Actor:** codex

Transitioned manifest status to discovered.

- confidence: None
- score: None
- source count: 6
- status: discovered

## 2026-06-24T16:13:51Z — discovery · KR

**Actor:** codex

Completed bounded official-source discovery for the Republic of Korea.

- candidate count: 6
- capability probes: 0
- page reads: 3
- searches: 2
- top region pilot: False
- verification performed: False

## 2026-06-24T16:13:51Z — handoff · KR

**Actor:** codex

Republic of Korea candidate artifact is frozen and ready for Claude Code verification.

- coverage model: nationally_unified
- manifest status: discovered
- verification status: all unverified

## 2026-06-24T16:14:34Z — decision · IN

**Actor:** codex

Corrected the India handoff count: the artifact contains 24 deferred region or territory groups, not 28.

- artifact changed: False
- artifact count: 24
- previous notebook count: 28

## 2026-06-24T16:14:34Z — handoff

**Actor:** codex

Completed the Codex discovery pass for all twenty final countries.

- candidate sources: 147
- capability probes: 0
- countries: 20
- countries with top region pilots: 14
- manifest status: all final countries discovered
- next actor: claude_code
- page reads: 69
- report built: False
- scoring performed: False
- searches: 54
- verification performed: False

## 2026-06-24T16:14:43Z — decision

**Actor:** codex

Corrected aggregate discovery metrics in the final handoff entry.

- artifacts changed: False
- candidate sources: 147
- capability probes: 0
- correct searches: 52
- correct top region pilots: 15
- page reads: 69
- previous searches: 54
- previous top region pilots: 14

## 2026-06-24T16:18:16Z — verification · BR · BR-ANA-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:17:07Z
- content type: text/html
- final url: https://www.snirh.gov.br/portal/snirh/snirh-1/atlas-de-vulnerabilidade-a-inundacoes
- http status: 404

## 2026-06-24T16:18:16Z — verification · BR · BR-SGB-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:17:13Z
- content type: text/html
- final url: https://geoportal.sgb.gov.br/portal/home/
- http status: 206

## 2026-06-24T16:18:16Z — verification · BR · BR-SP-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:17:14Z
- content type: text/html
- final url: https://datageo.ambiente.sp.gov.br/
- http status: 200

## 2026-06-24T16:18:16Z — verification · BR · BR-MG-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:17:18Z
- content type: text/html
- final url: https://geoportal.meioambiente.mg.gov.br/
- http status: 200

## 2026-06-24T16:18:16Z — verification · BR · BR-RJ-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:18:09Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:18:16Z — verification · BR · BR-BA-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:18:14Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:18:16Z — verification · BR · BR-PR-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:18:14Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:18:16Z — verification · BR · BR-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:18:16Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:26:18Z — verification · AT · AT-HORA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:06Z
- content type: text/html
- final url: https://hora.gv.at/
- http status: 206

## 2026-06-24T16:26:18Z — verification · AT · AT-WISA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:10Z
- content type: text/html
- final url: https://maps.wisa.bmluk.gv.at/hochwasser
- http status: 206

## 2026-06-24T16:26:18Z — verification · AT · AT-BML-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:14Z
- content type: text/html
- final url: https://www.bmluk.gv.at/themen/wasser/wisa/hochwasserrisiko.html
- http status: 206

## 2026-06-24T16:26:18Z — verification · AT · AT-EHYD-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:15Z
- content type: text/html
- final url: https://ehyd.gv.at/
- http status: 206

## 2026-06-24T16:26:18Z — verification · AT · AT-EEA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:18Z
- content type: text/html
- final url: https://water.europa.eu/freshwater/europe-freshwater/floods-directive
- http status: 206

## 2026-06-24T16:26:31Z — verification · BE · BE-VLG-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:21Z
- content type: text/html
- final url: https://waterinfo.vlaanderen.be/overstromingsrichtlijn
- http status: 200

## 2026-06-24T16:26:31Z — verification · BE · BE-VLG-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:22Z
- content type: text/html
- final url: https://www.geopunt.be/
- http status: 206

## 2026-06-24T16:26:31Z — verification · BE · BE-WAL-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:24Z
- content type: text/html
- final url: https://geoportail.wallonie.be/walonmap
- http status: 200

## 2026-06-24T16:26:31Z — verification · BE · BE-WAL-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:28Z
- content type: text/html
- final url: https://environnement.wallonie.be/home/gestion-environnementale/risques-climatiques/inondations.html
- http status: 200

## 2026-06-24T16:26:31Z — verification · BE · BE-BRU-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:26:29Z
- content type: text/html
- final url: https://environnement.brussels/citoyen/outils-et-donnees/cartes/les-cartes-relatives-aux-inondations-pour-la-region-bruxelloise
- http status: 404

## 2026-06-24T16:26:31Z — verification · BE · BE-EEA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:31Z
- content type: text/html
- final url: https://water.europa.eu/freshwater/europe-freshwater/floods-directive
- http status: 206

## 2026-06-24T16:26:59Z — verification · CA · CA-NRCAN-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:26:32Z
- content type: text/html
- final url: https://natural-resources.canada.ca/science-and-data/science-and-research/natural-hazards/flood-hazard-identification-and-mapping-program
- http status: 404

## 2026-06-24T16:26:59Z — verification · CA · CA-OPENMAPS-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:49Z
- content type: text/html
- final url: https://search.open.canada.ca/openmap/
- http status: 200

## 2026-06-24T16:26:59Z — verification · CA · CA-ON-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:26:51Z
- content type: text/html
- final url: https://www.ontario.ca/page/floodplain-mapping
- http status: 404

## 2026-06-24T16:26:59Z — verification · CA · CA-QC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:52Z
- content type: text/html
- final url: https://zonesinondables.mrnf.gouv.qc.ca:443/
- http status: 206

## 2026-06-24T16:26:59Z — verification · CA · CA-BC-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:26:53Z
- content type: text/html
- final url: https://www2.gov.bc.ca/gov/content/environment/air-land-water/water/drought-flooding-dikes-dams/integrated-flood-hazard-management/flood-hazard-land-use-management/floodplain-mapping
- http status: 404

## 2026-06-24T16:26:59Z — verification · CA · CA-AB-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:56Z
- content type: text/html
- final url: https://floods.alberta.ca/
- http status: 200

## 2026-06-24T16:26:59Z — verification · CA · CA-MB-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:58Z
- content type: text/html
- final url: https://www.gov.mb.ca/mti/
- http status: 206

## 2026-06-24T16:26:59Z — verification · CA · CA-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:26:59Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:27:13Z — verification · CH · CH-BAFU-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:00Z
- content type: text/html
- final url: https://map.geo.admin.ch/?layers=ch.bafu.gefaehrdungskarte-oberflaechenabfluss
- http status: 206

## 2026-06-24T16:27:13Z — verification · CH · CH-BAFU-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:03Z
- content type: text/html
- final url: https://www.bafu.admin.ch/de/naturgefahren
- http status: 200

## 2026-06-24T16:27:13Z — verification · CH · CH-ZH-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:04Z
- content type: text/html
- final url: https://maps.zh.ch/
- http status: 200

## 2026-06-24T16:27:13Z — verification · CH · CH-BE-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:27:05Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:27:13Z — verification · CH · CH-VD-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:06Z
- content type: text/html
- final url: https://www.geo.vd.ch/
- http status: 206

## 2026-06-24T16:27:13Z — verification · CH · CH-AG-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:11Z
- content type: text/html
- final url: https://www.ag.ch/geoportal/apps/onlinekarten/?welcome
- http status: 200

## 2026-06-24T16:27:13Z — verification · CH · CH-SG-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:13Z
- content type: text/html
- final url: https://www.geoportal.ch/
- http status: 200

## 2026-06-24T16:28:20Z — verification · CN · CN-MWR-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:18Z
- content type: text/html
- final url: http://www.mwr.gov.cn/
- http status: 206

## 2026-06-24T16:28:20Z — verification · CN · CN-MEM-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:20Z
- content type: text/html
- final url: https://www.mem.gov.cn/
- http status: 200

## 2026-06-24T16:28:20Z — verification · CN · CN-GD-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:27:28Z
- content type: text/html
- final url: https://slt.gd.gov.cn/
- http status: 500

## 2026-06-24T16:28:20Z — verification · CN · CN-SD-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:27:34Z
- content type: text/html
- final url: http://wr.shandong.gov.cn/
- http status: 206

## 2026-06-24T16:28:20Z — verification · CN · CN-HA-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:27:36Z
- content type: text/html
- final url: https://slt.henan.gov.cn/
- http status: 403

## 2026-06-24T16:28:20Z — verification · CN · CN-JS-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:28:16Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:28:20Z — verification · CN · CN-SC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:19Z
- content type: text/html
- final url: http://slt.sc.gov.cn/
- http status: 200

## 2026-06-24T16:28:20Z — verification · CN · CN-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:20Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:28:34Z — verification · DE · DE-BFG-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:22Z
- content type: text/html
- final url: https://geoportal.bafg.de/
- http status: 206

## 2026-06-24T16:28:34Z — verification · DE · DE-WBL-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:23Z
- content type: text/html
- final url: https://www.wasserblick.net/servlet/is/1/
- http status: 206

## 2026-06-24T16:28:34Z — verification · DE · DE-NW-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:25Z
- content type: text/html
- final url: https://www.flussgebiete.nrw.de/hochwassergefahrenkarten-und-hochwasserrisikokarten
- http status: 200

## 2026-06-24T16:28:34Z — verification · DE · DE-BY-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:27Z
- content type: text/html
- final url: https://www.umweltatlas.bayern.de/mapapps/resources/apps/umweltatlas/index.html?lang=de
- http status: 206

## 2026-06-24T16:28:34Z — verification · DE · DE-BW-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:28Z
- content type: text/html
- final url: https://udo.lubw.baden-wuerttemberg.de/public/
- http status: 200

## 2026-06-24T16:28:34Z — verification · DE · DE-NI-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:29Z
- content type: text/html
- final url: https://www.umweltkarten-niedersachsen.de/
- http status: 206

## 2026-06-24T16:28:34Z — verification · DE · DE-HE-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:31Z
- content type: text/html
- final url: https://hochwasser.hessen.de/
- http status: 200

## 2026-06-24T16:28:34Z — verification · DE · DE-EEA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:34Z
- content type: text/html
- final url: https://water.europa.eu/freshwater/europe-freshwater/floods-directive
- http status: 206

## 2026-06-24T16:28:52Z — verification · FR · FR-GEORISQUES-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:36Z
- content type: text/html
- final url: https://www.georisques.gouv.fr/donnees/bases-de-donnees
- http status: 200

## 2026-06-24T16:28:52Z — verification · FR · FR-GPU-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:37Z
- content type: text/html
- final url: https://www.geoportail-urbanisme.gouv.fr/
- http status: 200

## 2026-06-24T16:28:52Z — verification · FR · FR-IDF-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:28:41Z
- content type: text/html
- final url: https://www.drieat.ile-de-france.developpement-durable.gouv.fr/cartographie-des-risques-d-inondation-r677.html
- http status: 404

## 2026-06-24T16:28:52Z — verification · FR · FR-ARA-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:28:43Z
- content type: text/html
- final url: https://www.auvergne-rhone-alpes.developpement-durable.gouv.fr/directive-inondation-r3414.html
- http status: 404

## 2026-06-24T16:28:52Z — verification · FR · FR-NAQ-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:45Z
- content type: text/html
- final url: https://www.nouvelle-aquitaine.developpement-durable.gouv.fr/directive-inondation-r740.html
- http status: 206

## 2026-06-24T16:28:52Z — verification · FR · FR-OCC-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:28:47Z
- content type: text/html
- final url: https://www.occitanie.developpement-durable.gouv.fr/la-directive-inondation-r7214.html
- http status: 404

## 2026-06-24T16:28:52Z — verification · FR · FR-HDF-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:28:49Z
- content type: text/html
- final url: https://www.hauts-de-france.developpement-durable.gouv.fr/?Cartographie-des-risques-d-inondation
- http status: 404

## 2026-06-24T16:28:52Z — verification · FR · FR-EEA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:52Z
- content type: text/html
- final url: https://water.europa.eu/freshwater/europe-freshwater/floods-directive
- http status: 206

## 2026-06-24T16:29:02Z — verification · IE · IE-OPW-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:54Z
- content type: text/html
- final url: https://www.floodinfo.ie/map/floodmaps/
- http status: 200

## 2026-06-24T16:29:02Z — verification · IE · IE-OPW-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:56Z
- content type: text/html
- final url: https://www.floodinfo.ie/map/floodmaps/
- http status: 200

## 2026-06-24T16:29:02Z — verification · IE · IE-DATA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:28:58Z
- content type: text/html
- final url: https://data.gov.ie/dataset/?q=flood+maps
- http status: 200

## 2026-06-24T16:29:02Z — verification · IE · IE-EPA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:29:00Z
- content type: text/html
- final url: https://gis.epa.ie/EPAMaps/
- http status: 206

## 2026-06-24T16:29:02Z — verification · IE · IE-EEA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:29:02Z
- content type: text/html
- final url: https://water.europa.eu/freshwater/europe-freshwater/floods-directive
- http status: 206

## 2026-06-24T16:32:03Z — verification · IN · IN-NRSC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:29:08Z
- content type: text/html
- final url: https://bhuvan-app1.nrsc.gov.in/disaster/disaster.php
- http status: 206

## 2026-06-24T16:32:03Z — verification · IN · IN-CWC-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:29:49Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:32:03Z — verification · IN · IN-WRIS-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:30:29Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:32:03Z — verification · IN · IN-UP-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:30:31Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:32:03Z — verification · IN · IN-MH-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:30:35Z
- content type: text/html
- final url: https://sdma.maharashtra.gov.in/
- http status: 200

## 2026-06-24T16:32:03Z — verification · IN · IN-BR-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:30:40Z
- content type: text/html
- final url: https://www.fmiscwrdbihar.gov.in/
- http status: 206

## 2026-06-24T16:32:03Z — verification · IN · IN-WB-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:31:21Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:32:03Z — verification · IN · IN-MP-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:32:01Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:32:03Z — verification · IN · IN-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:03Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:32:20Z — verification · IT · IT-ISPRA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:04Z
- content type: text/html
- final url: https://idrogeo.isprambiente.it/app/
- http status: 206

## 2026-06-24T16:32:20Z — verification · IT · IT-ADBPO-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:08Z
- content type: text/html
- final url: https://www.adbpo.it/
- http status: 206

## 2026-06-24T16:32:20Z — verification · IT · IT-AC-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:32:08Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:32:20Z — verification · IT · IT-AM-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:32:12Z
- content type: text/html
- final url: https://www.distrettoappenninomeridionale.it/pgra
- http status: 404

## 2026-06-24T16:32:20Z — verification · IT · IT-AO-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:32:13Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:32:20Z — verification · IT · IT-SIC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:18Z
- content type: text/html
- final url: https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/presidenza-regione/autorita-bacino-distretto-idrografico-sicilia
- http status: 200

## 2026-06-24T16:32:20Z — verification · IT · IT-EEA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:20Z
- content type: text/html
- final url: https://water.europa.eu/freshwater/europe-freshwater/floods-directive
- http status: 206

## 2026-06-24T16:32:40Z — verification · JP · JP-MLIT-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:21Z
- content type: text/html
- final url: https://disaportal.gsi.go.jp/
- http status: 206

## 2026-06-24T16:32:40Z — verification · JP · JP-MLIT-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:24Z
- content type: text/html
- final url: https://nlftp.mlit.go.jp/ksj/gml/datalist/KsjTmplt-A31-v3_0.html
- http status: 200

## 2026-06-24T16:32:40Z — verification · JP · JP-MLIT-003

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:25Z
- content type: text/html
- final url: https://www.river.go.jp/
- http status: 200

## 2026-06-24T16:32:40Z — verification · JP · JP-TKY-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:32:27Z
- content type: text/html
- final url: https://www.kensetsu.metro.tokyo.lg.jp/jigyo/river/chusho_seibi/index/menu03-01.html
- http status: 404

## 2026-06-24T16:32:40Z — verification · JP · JP-KNG-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:32:31Z
- content type: text/html
- final url: https://www.pref.kanagawa.jp/docs/f4i/cnt/f3747/
- http status: 206

## 2026-06-24T16:32:40Z — verification · JP · JP-OSK-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:32:35Z
- content type: text/html
- final url: https://www.pref.osaka.lg.jp/o130350/kasenkankyo/hazardmap/index.html
- http status: 404

## 2026-06-24T16:32:40Z — verification · JP · JP-AIC-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:32:37Z
- content type: text/html
- final url: https://www.pref.aichi.jp/soshiki/kasen/shinsuisoutei.html
- http status: 404

## 2026-06-24T16:32:40Z — verification · JP · JP-SAI-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:32:40Z
- content type: text/html
- final url: https://www.pref.saitama.lg.jp/a1007/kouzui-sinsuisouteikuiki.html
- http status: 404

## 2026-06-24T16:35:23Z — verification · MX · MX-CENAPRED-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:34:13Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:35:23Z — verification · MX · MX-CONAGUA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:34:15Z
- content type: text/html
- final url: https://www.gob.mx/conagua
- http status: 206

## 2026-06-24T16:35:23Z — verification · MX · MX-INEGI-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:34:17Z
- content type: text/html
- final url: https://antares.inegi.org.mx/analisis/red_hidro/siatl/
- http status: 206

## 2026-06-24T16:35:23Z — verification · MX · MX-EM-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:34:37Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:35:23Z — verification · MX · MX-CMX-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:34:39Z
- content type: text/html
- final url: https://www.atlas.cdmx.gob.mx/
- http status: 206

## 2026-06-24T16:35:23Z — verification · MX · MX-JAL-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:34:41Z
- content type: text/html
- final url: https://proteccioncivil.jalisco.gob.mx/
- http status: 206

## 2026-06-24T16:35:23Z — verification · MX · MX-VER-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:35:21Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:35:23Z — verification · MX · MX-PUE-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:35:21Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:35:23Z — verification · MX · MX-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:35:23Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:36:31Z — verification · MY · MY-JPS-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:35:27Z
- content type: text/html
- final url: https://publicinfobanjir.water.gov.my/
- http status: 206

## 2026-06-24T16:36:31Z — verification · MY · MY-JPS-002

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:35:27Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:36:31Z — verification · MY · MY-NAHRIM-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:15Z
- content type: text/html
- final url: https://www.nahrim.gov.my/
- http status: 200

## 2026-06-24T16:36:31Z — verification · MY · MY-SEL-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:36:15Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:36:31Z — verification · MY · MY-JHR-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:36:15Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:36:31Z — verification · MY · MY-SBH-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:20Z
- content type: text/html
- final url: https://did.sabah.gov.my/
- http status: 200

## 2026-06-24T16:36:31Z — verification · MY · MY-PRK-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:36:20Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:36:31Z — verification · MY · MY-SWK-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:30Z
- content type: text/html
- final url: https://did.sarawak.gov.my/web/home/index/
- http status: 200

## 2026-06-24T16:36:31Z — verification · MY · MY-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:31Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:36:41Z — verification · PL · PL-WP-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:33Z
- content type: text/html
- final url: https://wody.isok.gov.pl/imap_kzgw/?gpmap=gpMZP
- http status: 206

## 2026-06-24T16:36:41Z — verification · PL · PL-WP-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:35Z
- content type: text/html
- final url: https://www.gov.pl/web/wody-polskie/mapy-zagrozenia-powodziowego-i-mapy-ryzyka-powodziowego
- http status: 200

## 2026-06-24T16:36:41Z — verification · PL · PL-GUGIK-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:36Z
- content type: text/html
- final url: https://mapy.geoportal.gov.pl/imap/Imgp_2.html
- http status: 206

## 2026-06-24T16:36:41Z — verification · PL · PL-IMGW-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:38Z
- content type: text/html
- final url: https://hydro.imgw.pl/
- http status: 206

## 2026-06-24T16:36:41Z — verification · PL · PL-EEA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:41Z
- content type: text/html
- final url: https://water.europa.eu/freshwater/europe-freshwater/floods-directive
- http status: 206

## 2026-06-24T16:36:52Z — verification · SE · SE-MSB-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:44Z
- content type: text/html
- final url: https://gisapp.msb.se/apps/oversvamningsportal/index.html
- http status: 206

## 2026-06-24T16:36:52Z — verification · SE · SE-MSB-002

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:36:46Z
- content type: text/html
- final url: https://www.mcf.se/sv/verktyg--tjanster/oversvamningsportalen/oversvamningskarteringar/
- http status: 404

## 2026-06-24T16:36:52Z — verification · SE · SE-MSB-003

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:48Z
- content type: text/html
- final url: https://www.mcf.se/sv/amnesomraden/skydd-mot-olyckor-och-farliga-amnen/naturolyckor-och-klimat/oversvamning/oversvamningsdirektivet/
- http status: 200

## 2026-06-24T16:36:52Z — verification · SE · SE-LANT-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:36:51Z
- content type: text/html
- final url: https://www.lantmateriet.se/sv/geodata/vara-produkter/produktlista/markhojdmodell-nedladdning-grid-1/
- http status: 404

## 2026-06-24T16:36:52Z — verification · SE · SE-EEA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:36:52Z
- content type: text/html
- final url: https://water.europa.eu/freshwater/europe-freshwater/floods-directive
- http status: 206

## 2026-06-24T16:38:28Z — verification · TH · TH-DWR-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:37:36Z
- content type: text/html
- final url: https://mekhala.dwr.go.th/
- http status: 200

## 2026-06-24T16:38:28Z — verification · TH · TH-GISTDA-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:38:00Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:38:28Z — verification · TH · TH-THAIWATER-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:38:03Z
- content type: text/html
- final url: https://www.thaiwater.net/
- http status: 200

## 2026-06-24T16:38:28Z — verification · TH · TH-BKK-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:38:25Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:38:28Z — verification · TH · TH-NMA-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:38:26Z
- content type: text/html
- final url: https://www.disaster.go.th/
- http status: 403

## 2026-06-24T16:38:28Z — verification · TH · TH-UBN-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:38:26Z
- content type: text/html
- final url: https://www.disaster.go.th/
- http status: 403

## 2026-06-24T16:38:28Z — verification · TH · TH-CMI-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:38:26Z
- content type: text/html
- final url: https://www.disaster.go.th/
- http status: 403

## 2026-06-24T16:38:28Z — verification · TH · TH-KKN-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:38:27Z
- content type: text/html
- final url: https://www.disaster.go.th/
- http status: 403

## 2026-06-24T16:38:28Z — verification · TH · TH-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:38:28Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:39:09Z — verification · ZA · ZA-SARVA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:38:31Z
- content type: text/html
- final url: https://sarva.saeon.ac.za/
- http status: 200

## 2026-06-24T16:39:09Z — verification · ZA · ZA-DWS-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:38:34Z
- content type: text/html
- final url: https://www.dws.gov.za/Hydrology/
- http status: 403

## 2026-06-24T16:39:09Z — verification · ZA · ZA-NDMC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:38:38Z
- content type: text/html
- final url: https://www.ndmc.gov.za/
- http status: 200

## 2026-06-24T16:39:09Z — verification · ZA · ZA-GP-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:38:38Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:39:09Z — verification · ZA · ZA-KZN-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:38:54Z
- content type: text/html
- final url: https://www.kzncogta.gov.za/
- http status: 200

## 2026-06-24T16:39:09Z — verification · ZA · ZA-WC-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:39:00Z
- content type: text/html
- final url: https://www.westerncape.gov.za/general-publication/disaster-management
- http status: 404

## 2026-06-24T16:39:09Z — verification · ZA · ZA-EC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:39:05Z
- content type: text/html
- final url: https://www.eccogta.gov.za/
- http status: 200

## 2026-06-24T16:39:09Z — verification · ZA · ZA-LP-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:39:08Z
- content type: text/html
- final url: https://www.coghsta.limpopo.gov.za/
- http status: 200

## 2026-06-24T16:39:09Z — verification · ZA · ZA-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:39:09Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:43:42Z — implementation

**Actor:** claude_code

Fixed validate_url.py to record connection-level failures instead of crashing. RemoteDisconnected (server drops the bounded HEAD/ranged-GET) is a ConnectionResetError/OSError not caught by the prior (URLError, ValueError, socket.timeout, ssl.SSLError) clause, so it propagated out of verify_country and aborted the whole-country write for AE and KR. Broadened both except clauses to (URLError, ValueError, OSError, http.client.HTTPException), which subsumes timeout/SSL/DNS and now records a server reset as a failed check, consistent with existing failure handling. No behavior change for sources that already succeed or fail with a recorded error.

- affected countries: ["AE", "KR"]
- file: tools/validate_url.py
- root cause: http.client.RemoteDisconnected uncaught

## 2026-06-24T16:45:16Z — verification · AE · AE-MOEI-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:44:10Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:45:16Z — verification · AE · AE-NCM-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:44:15Z
- content type: text/html
- final url: https://www.ncm.gov.ae/
- http status: 200

## 2026-06-24T16:45:16Z — verification · AE · AE-AUH-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:44:16Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:45:16Z — verification · AE · AE-DXB-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:45:10Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:45:16Z — verification · AE · AE-SHJ-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:45:11Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:45:16Z — verification · AE · AE-AJM-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:45:12Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:45:16Z — verification · AE · AE-RAK-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:45:15Z
- content type: text/html
- final url: https://mun.rak.ae/
- http status: 200

## 2026-06-24T16:45:16Z — verification · AE · AE-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:45:16Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:46:22Z — verification · KR · KR-MOE-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:45:22Z
- content type: text/html
- final url: https://floodmap.go.kr/intro
- http status: 200

## 2026-06-24T16:46:22Z — verification · KR · KR-WAMIS-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:46:13Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T16:46:22Z — verification · KR · KR-SAFEMAP-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:46:15Z
- content type: text/html
- final url: https://www.safemap.go.kr/
- http status: 200

## 2026-06-24T16:46:22Z — verification · KR · KR-VWORLD-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:46:18Z
- content type: text/html
- final url: https://www.vworld.kr/
- http status: 502

## 2026-06-24T16:46:22Z — verification · KR · KR-DATA-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:46:21Z
- content type: text/html
- final url: https://www.data.go.kr/
- http status: 200

## 2026-06-24T16:46:22Z — verification · KR · KR-JRC-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T16:46:22Z
- content type: text/html
- final url: https://data.jrc.ec.europa.eu/collection/id-0054
- http status: 200

## 2026-06-24T16:51:09Z — decision

**Actor:** claude_code

Scoring rubric for the 20 final countries, calibrated against the GB fixture (score 4: probe-verified WMS/WFS, confirmed OGL, dated NaFRA2). Pass-2 evidence here is portal-load-only: every source exposes just a primary link verified at HTTP 200/206; no bounded capability probe confirmed any machine service, and verification captured no last_update dates. Consequences applied uniformly: (1) technical_accessibility capped at 3 (no probe confirmation) -> 3 where a verified national source advertises services/API/download/WMS, 2 for viewer/PDF/portal/request-only; (2) documentation_currency=2 for all (no dates captured - currency cannot be asserted from metadata); (3) licensing=3 only where a recognized open-gov licence is named (OGL Canada, Licence Ouverte/Etalab, Datenlizenz Deutschland, Korea OGL, EU public-sector etc., all still 'verify'), else 2; (4) geographic_completeness 4 for nationally-unified or national+>=4/5-region pilots, 3 for national-verified-but-partial-region, 2 where the authoritative national source failed or coverage is sparse; (5) scenario_richness 4 for multiple probability/return bands plus depth/climate, 3 for a few bands/classes, 2 for susceptibility-only/event-based/'varies'; (6) integration_effort 3 for single unified national systems, 2 for federal/regional-publisher fragmentation. No final country reaches 4 because services, licences, and currency are all unconfirmed at Pass-2; this keeps the fully probe-verified GB fixture as the only 4. Confidence medium for the score-3 tier, low for the score-2 tier (flagship failures / sparse coverage).

- doc currency: 2 uniformly - no last_update captured
- tech cap: 3 - no capability probes at Pass-2
- tier 2 low: ["BR", "IN", "CN", "MX", "MY", "TH", "ZA", "AE"]
- tier 3 medium: ["DE", "CA", "FR", "PL", "JP", "BE", "IT", "CH", "IE", "SE", "AT", "KR"]

## 2026-06-24T16:51:23Z — score · BR

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 2}

## 2026-06-24T16:51:23Z — score · IN

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 2}

## 2026-06-24T16:51:23Z — score · CN

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 2}

## 2026-06-24T16:51:23Z — score · MX

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 2}

## 2026-06-24T16:51:23Z — score · MY

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 2}

## 2026-06-24T16:51:23Z — score · TH

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 2}

## 2026-06-24T16:51:23Z — score · AE

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 2}

## 2026-06-24T16:51:23Z — score · ZA

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.1666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 2}

## 2026-06-24T16:51:23Z — score · DE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 3.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 2, "licensing": 3, "scenario_richness": 4, "technical_accessibility": 3}

## 2026-06-24T16:51:23Z — score · CA

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 2.6666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 3, "scenario_richness": 3, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · FR

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 2.8333333333333335
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 3, "scenario_richness": 4, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · PL

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 3.1666666666666665
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 3, "licensing": 3, "scenario_richness": 4, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · JP

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 2.6666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 3, "scenario_richness": 3, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · BE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 2.8333333333333335
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 3, "scenario_richness": 4, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · IT

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 2.8333333333333335
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 3, "scenario_richness": 4, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · CH

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 2.6666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 3, "scenario_richness": 3, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · IE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 3.1666666666666665
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 3, "licensing": 3, "scenario_richness": 4, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · SE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 3.1666666666666665
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 3, "licensing": 3, "scenario_richness": 4, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · AT

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 3.0
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 3, "licensing": 3, "scenario_richness": 3, "technical_accessibility": 3}

## 2026-06-24T16:51:24Z — score · KR

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 3.0
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 3, "licensing": 3, "scenario_richness": 3, "technical_accessibility": 3}

## 2026-06-24T16:51:39Z — manifest_transition · BR

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 8
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · IN

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 9
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · DE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 8
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · CN

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 8
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · CA

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 8
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · FR

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 8
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · MX

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 9
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · MY

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 9
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · PL

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 5
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · JP

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 8
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · BE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 6
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · IT

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 7
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · CH

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 7
- status: verified

## 2026-06-24T16:51:39Z — manifest_transition · IE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 5
- status: verified

## 2026-06-24T16:51:40Z — manifest_transition · TH

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 9
- status: verified

## 2026-06-24T16:51:40Z — manifest_transition · SE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 5
- status: verified

## 2026-06-24T16:51:40Z — manifest_transition · AT

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 5
- status: verified

## 2026-06-24T16:51:40Z — manifest_transition · AE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 8
- status: verified

## 2026-06-24T16:51:40Z — manifest_transition · ZA

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 9
- status: verified

## 2026-06-24T16:51:40Z — manifest_transition · KR

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 6
- status: verified

## 2026-06-24T16:55:00Z — verification · BR · BR-RJ-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:55:00Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:00:24Z — verification · IN · IN-CWC-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:56:23Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:00:24Z — verification · IN · IN-WRIS-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:57:44Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:00:24Z — verification · IN · IN-WB-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T16:59:04Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:00:24Z — verification · IN · IN-MP-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:00:24Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:03:05Z — verification · MX · MX-CENAPRED-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:01:45Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:03:05Z — verification · MX · MX-VER-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:03:05Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:06:04Z — verification · AE · AE-MOEI-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:04:26Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:06:04Z — verification · AE · AE-DXB-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:06:04Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:07:27Z — verification · KR · KR-WAMIS-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:07:25Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:07:27Z — verification · KR · KR-VWORLD-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:07:27Z
- content type: text/html
- final url: https://www.vworld.kr/
- http status: 502

## 2026-06-24T17:08:12Z — verification · TH · TH-GISTDA-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:07:50Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:08:12Z — verification · TH · TH-BKK-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:08:12Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:09:37Z — verification · CN · CN-GD-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:08:16Z
- content type: text/html
- final url: https://slt.gd.gov.cn/
- http status: 500

## 2026-06-24T17:09:37Z — verification · CN · CN-JS-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T17:09:37Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T17:10:12Z — finding · BR · BR-ANA-001

**Actor:** claude_code

Material source BR-ANA-001 (Agência Nacional de Águas e Saneamento Básico (ANA) - Flood Vulnerability Atlas) failed bounded verification. Primary link https://www.snirh.gov.br/portal/snirh/snirh-1/atlas-de-vulnerabilidade-a-inundacoes returned HTTP 404. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:17:07Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.snirh.gov.br/portal/snirh/snirh-1/atlas-de-vulnerabilidade-a-inundacoes", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · BR · BR-RJ-001

**Actor:** claude_code

Material source BR-RJ-001 (Instituto Estadual do Ambiente (INEA) - GeoINEA Flood-Risk Mapping) failed bounded verification. Primary link https://geoportal.inea.rj.gov.br/portal/apps/sites/#/geoinea returned GET: URLError: <urlopen error timed out>. Coverage for Rio de Janeiro is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:55:00Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · BR · BR-BA-001

**Actor:** claude_code

Material source BR-BA-001 (Instituto do Meio Ambiente e Recursos Hídricos (INEMA) - GeoBahia Environmental Geoportal) failed bounded verification. Primary link https://geobahia.inema.ba.gov.br/ returned GET: URLError: <urlopen error [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name (_ssl.c:1010)>. Coverage for Bahia is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:18:14Z", "error": "GET: URLError: <urlopen error [SSL: TLSV1_UNRECOGNIZED_NAME] tlsv1 unrecognized name (_ssl.c:1010)>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · BR · BR-PR-001

**Actor:** claude_code

Material source BR-PR-001 (Governo do Paraná / GeoPR - GeoPR Flood and Risk Geodata) failed bounded verification. Primary link https://www.geopr.pr.gov.br/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Paraná is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:18:14Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · IN · IN-CWC-001

**Actor:** claude_code

Material source IN-CWC-001 (Central Water Commission - CWC Flood Forecasting Portal) failed bounded verification. Primary link https://aff.india-water.gov.in/ returned GET: URLError: <urlopen error timed out>. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:56:23Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · IN · IN-WRIS-001

**Actor:** claude_code

Material source IN-WRIS-001 (National Water Informatics Centre - India Water Resources Information System) failed bounded verification. Primary link https://indiawris.gov.in/wris/ returned GET: URLError: <urlopen error timed out>. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:57:44Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · IN · IN-UP-001

**Actor:** claude_code

Material source IN-UP-001 (Uttar Pradesh State Disaster Management Authority - Uttar Pradesh Flood Hazard Resources) failed bounded verification. Primary link https://upsdma.up.nic.in/ returned GET: URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>. Coverage for Uttar Pradesh is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:30:31Z", "error": "GET: URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · IN · IN-WB-001

**Actor:** claude_code

Material source IN-WB-001 (Irrigation & Waterways Department, West Bengal - West Bengal Flood Management and GIS Resources) failed bounded verification. Primary link https://wbiwd.gov.in/ returned GET: URLError: <urlopen error timed out>. Coverage for West Bengal is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:59:04Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · IN · IN-MP-001

**Actor:** claude_code

Material source IN-MP-001 (Water Resources Department, Madhya Pradesh - Madhya Pradesh Water Resources GIS and Flood Studies) failed bounded verification. Primary link https://mpwrd.gov.in/ returned GET: URLError: <urlopen error timed out>. Coverage for Madhya Pradesh is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:00:24Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · CN · CN-GD-001

**Actor:** claude_code

Material source CN-GD-001 (广东省水利厅 - Guangdong Flood and Flash-Flood Risk Maps) failed bounded verification. Primary link https://slt.gd.gov.cn/ returned HTTP 500. Coverage for Guangdong is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:08:16Z", "error": "HTTPError: Internal Server Error", "failed_role": "primary", "final_url": "https://slt.gd.gov.cn/", "http_status": 500, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · CN · CN-HA-001

**Actor:** claude_code

Material source CN-HA-001 (河南省水利厅 - Henan Flood Risk Maps) failed bounded verification. Primary link https://slt.henan.gov.cn/ returned HTTP 403. Coverage for Henan is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:27:36Z", "error": "HTTPError: Forbidden", "failed_role": "primary", "final_url": "https://slt.henan.gov.cn/", "http_status": 403, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · CN · CN-JS-001

**Actor:** claude_code

Material source CN-JS-001 (江苏省水利厅 - Jiangsu Flood Risk Maps) failed bounded verification. Primary link http://jssslt.jiangsu.gov.cn/ returned GET: URLError: <urlopen error timed out>. Coverage for Jiangsu is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:09:37Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · CA · CA-NRCAN-001

**Actor:** claude_code

Material source CA-NRCAN-001 (Natural Resources Canada - Flood Hazard Identification and Mapping Program) failed bounded verification. Primary link https://natural-resources.canada.ca/science-and-data/science-and-research/natural-hazards/flood-hazard-identification-and-mapping-program returned HTTP 404. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:26:32Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://natural-resources.canada.ca/science-and-data/science-and-research/natural-hazards/flood-hazard-identification-and-mapping-program", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · CA · CA-ON-001

**Actor:** claude_code

Material source CA-ON-001 (Government of Ontario / Ministry of Natural Resources - Ontario Floodplain Mapping) failed bounded verification. Primary link https://www.ontario.ca/page/floodplain-mapping returned HTTP 404. Coverage for Ontario is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:26:51Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.ontario.ca/page/floodplain-mapping", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · CA · CA-BC-001

**Actor:** claude_code

Material source CA-BC-001 (Government of British Columbia - British Columbia Floodplain Mapping) failed bounded verification. Primary link https://www2.gov.bc.ca/gov/content/environment/air-land-water/water/drought-flooding-dikes-dams/integrated-flood-hazard-management/flood-hazard-land-use-management/floodplain-mapping returned HTTP 404. Coverage for British Columbia is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:26:53Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www2.gov.bc.ca/gov/content/environment/air-land-water/water/drought-flooding-dikes-dams/integrated-flood-hazard-management/flood-hazard-land-use-management/floodplain-mapping", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · FR · FR-IDF-001

**Actor:** claude_code

Material source FR-IDF-001 (DRIEAT Île-de-France - Île-de-France TRI Flood Maps) failed bounded verification. Primary link https://www.drieat.ile-de-france.developpement-durable.gouv.fr/cartographie-des-risques-d-inondation-r677.html returned HTTP 404. Coverage for Île-de-France is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:28:41Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.drieat.ile-de-france.developpement-durable.gouv.fr/cartographie-des-risques-d-inondation-r677.html", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · FR · FR-ARA-001

**Actor:** claude_code

Material source FR-ARA-001 (DREAL Auvergne-Rhône-Alpes - Auvergne-Rhône-Alpes TRI Flood Maps) failed bounded verification. Primary link https://www.auvergne-rhone-alpes.developpement-durable.gouv.fr/directive-inondation-r3414.html returned HTTP 404. Coverage for Auvergne-Rhône-Alpes is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:28:43Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.auvergne-rhone-alpes.developpement-durable.gouv.fr/directive-inondation-r3414.html", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · FR · FR-OCC-001

**Actor:** claude_code

Material source FR-OCC-001 (DREAL Occitanie - Occitanie Flood Hazard and Risk Maps) failed bounded verification. Primary link https://www.occitanie.developpement-durable.gouv.fr/la-directive-inondation-r7214.html returned HTTP 404. Coverage for Occitanie is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:28:47Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.occitanie.developpement-durable.gouv.fr/la-directive-inondation-r7214.html", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · FR · FR-HDF-001

**Actor:** claude_code

Material source FR-HDF-001 (DREAL Hauts-de-France - Hauts-de-France TRI Flood Maps) failed bounded verification. Primary link https://www.hauts-de-france.developpement-durable.gouv.fr/?Cartographie-des-risques-d-inondation returned HTTP 404. Coverage for Hauts-de-France is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:28:49Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.hauts-de-france.developpement-durable.gouv.fr/?Cartographie-des-risques-d-inondation", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · MX · MX-CENAPRED-001

**Actor:** claude_code

Material source MX-CENAPRED-001 (Centro Nacional de Prevención de Desastres - National Risk Atlas) failed bounded verification. Primary link https://www.atlasnacionalderiesgos.gob.mx/ returned GET: URLError: <urlopen error timed out>. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:01:45Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · MX · MX-EM-001

**Actor:** claude_code

Material source MX-EM-001 (Coordinación General de Protección Civil del Estado de México - State of Mexico Risk Atlas) failed bounded verification. Primary link https://atlasderiesgo.edomex.gob.mx/ returned GET: URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>. Coverage for Estado de México is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:34:37Z", "error": "GET: URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · MX · MX-VER-001

**Actor:** claude_code

Material source MX-VER-001 (Secretaría de Protección Civil de Veracruz - Veracruz State Risk Atlas) failed bounded verification. Primary link http://www.veracruz.gob.mx/proteccioncivil/atlas-de-riesgos/ returned GET: URLError: <urlopen error timed out>. Coverage for Veracruz is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:03:05Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · MX · MX-PUE-001

**Actor:** claude_code

Material source MX-PUE-001 (Coordinación General de Protección Civil del Estado de Puebla - Puebla State Risk Atlas) failed bounded verification. Primary link https://atlasderiesgos.puebla.gob.mx/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Puebla is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:35:21Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · MY · MY-JPS-002

**Actor:** claude_code

Material source MY-JPS-002 (Jabatan Pengairan dan Saliran Malaysia - DID Geospatial Flood Hazard Maps) failed bounded verification. Primary link https://jpsgeo.water.gov.my/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:35:27Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · MY · MY-SEL-001

**Actor:** claude_code

Material source MY-SEL-001 (JPS Malaysia / JPS Selangor - Selangor Flood Hazard Maps) failed bounded verification. Primary link https://jpsgeo.water.gov.my/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Selangor is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:36:15Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · MY · MY-JHR-001

**Actor:** claude_code

Material source MY-JHR-001 (JPS Malaysia / JPS Johor - Johor Flood Hazard Maps) failed bounded verification. Primary link https://jpsgeo.water.gov.my/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Johor is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:36:15Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · MY · MY-PRK-001

**Actor:** claude_code

Material source MY-PRK-001 (JPS Malaysia / JPS Perak - Perak Flood Hazard Maps) failed bounded verification. Primary link https://jpsgeo.water.gov.my/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Perak is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:36:20Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · JP · JP-TKY-001

**Actor:** claude_code

Material source JP-TKY-001 (東京都建設局 - Tokyo Flood Inundation Assumption Maps) failed bounded verification. Primary link https://www.kensetsu.metro.tokyo.lg.jp/jigyo/river/chusho_seibi/index/menu03-01.html returned HTTP 404. Coverage for Tokyo is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:32:27Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.kensetsu.metro.tokyo.lg.jp/jigyo/river/chusho_seibi/index/menu03-01.html", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · JP · JP-OSK-001

**Actor:** claude_code

Material source JP-OSK-001 (大阪府 - Osaka Flood Inundation Assumption Maps) failed bounded verification. Primary link https://www.pref.osaka.lg.jp/o130350/kasenkankyo/hazardmap/index.html returned HTTP 404. Coverage for Osaka is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:32:35Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.pref.osaka.lg.jp/o130350/kasenkankyo/hazardmap/index.html", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · JP · JP-AIC-001

**Actor:** claude_code

Material source JP-AIC-001 (愛知県 - Aichi Flood Inundation Assumption Maps) failed bounded verification. Primary link https://www.pref.aichi.jp/soshiki/kasen/shinsuisoutei.html returned HTTP 404. Coverage for Aichi is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:32:37Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.pref.aichi.jp/soshiki/kasen/shinsuisoutei.html", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · JP · JP-SAI-001

**Actor:** claude_code

Material source JP-SAI-001 (埼玉県 - Saitama Flood Inundation Assumption Maps) failed bounded verification. Primary link https://www.pref.saitama.lg.jp/a1007/kouzui-sinsuisouteikuiki.html returned HTTP 404. Coverage for Saitama is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:32:40Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.pref.saitama.lg.jp/a1007/kouzui-sinsuisouteikuiki.html", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · BE · BE-BRU-001

**Actor:** claude_code

Material source BE-BRU-001 (Bruxelles Environnement - Brussels Flood Hazard and Risk Map) failed bounded verification. Primary link https://environnement.brussels/citoyen/outils-et-donnees/cartes/les-cartes-relatives-aux-inondations-pour-la-region-bruxelloise returned HTTP 404. Coverage for Brussels-Capital Region is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:26:29Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://environnement.brussels/citoyen/outils-et-donnees/cartes/les-cartes-relatives-aux-inondations-pour-la-region-bruxelloise", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · IT · IT-AC-001

**Actor:** claude_code

Material source IT-AC-001 (Autorità di bacino distrettuale dell'Appennino Centrale - Central Apennines Flood Hazard and Risk Maps) failed bounded verification. Primary link https://www.autoritadistrettoac.it/pianificazione/pianificazione-distrettuale/pgra/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Lazio / Central Apennines is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:32:08Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · IT · IT-AM-001

**Actor:** claude_code

Material source IT-AM-001 (Autorità di bacino distrettuale dell'Appennino Meridionale - Southern Apennines Flood Risk Management Maps) failed bounded verification. Primary link https://www.distrettoappenninomeridionale.it/index.php/pgra returned HTTP 404. Coverage for Campania / Southern Apennines is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:32:12Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.distrettoappenninomeridionale.it/pgra", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · IT · IT-AO-001

**Actor:** claude_code

Material source IT-AO-001 (Autorità di bacino distrettuale delle Alpi Orientali - Eastern Alps Flood Hazard and Risk Maps) failed bounded verification. Primary link https://distrettoalpiorientali.it/piano-gestione-rischio-alluvioni/ returned GET: URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>. Coverage for Veneto / Eastern Alps is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:32:13Z", "error": "GET: URLError: <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: unable to get local issuer certificate (_ssl.c:1010)>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · CH · CH-BE-001

**Actor:** claude_code

Material source CH-BE-001 (Kanton Bern - Bern Natural-Hazard Flood Map) failed bounded verification. Primary link https://www.geo.apps.be.ch/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Bern is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:27:05Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · TH · TH-GISTDA-001

**Actor:** claude_code

Material source TH-GISTDA-001 (สำนักงานพัฒนาเทคโนโลยีอวกาศและภูมิสารสนเทศ - GISTDA Disaster Flood Monitoring) failed bounded verification. Primary link https://disaster.gistda.or.th/ returned GET: URLError: <urlopen error [Errno 54] Connection reset by peer>. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:07:50Z", "error": "GET: URLError: <urlopen error [Errno 54] Connection reset by peer>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · TH · TH-BKK-001

**Actor:** claude_code

Material source TH-BKK-001 (Bangkok Metropolitan Administration - Bangkok Flood Monitoring and Risk Maps) failed bounded verification. Primary link https://weather.bangkok.go.th/ returned GET: URLError: <urlopen error [Errno 54] Connection reset by peer>. Coverage for Bangkok is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:08:12Z", "error": "GET: URLError: <urlopen error [Errno 54] Connection reset by peer>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · TH · TH-NMA-001

**Actor:** claude_code

Material source TH-NMA-001 (Department of Disaster Prevention and Mitigation / provincial authorities - Nakhon Ratchasima Flood-Risk Maps) failed bounded verification. Primary link https://www.disaster.go.th/ returned HTTP 403. Coverage for Nakhon Ratchasima is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:38:26Z", "error": "HTTPError: Forbidden", "failed_role": "primary", "final_url": "https://www.disaster.go.th/", "http_status": 403, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · TH · TH-UBN-001

**Actor:** claude_code

Material source TH-UBN-001 (Department of Disaster Prevention and Mitigation / provincial authorities - Ubon Ratchathani Flood-Risk Maps) failed bounded verification. Primary link https://www.disaster.go.th/ returned HTTP 403. Coverage for Ubon Ratchathani is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:38:26Z", "error": "HTTPError: Forbidden", "failed_role": "primary", "final_url": "https://www.disaster.go.th/", "http_status": 403, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · TH · TH-CMI-001

**Actor:** claude_code

Material source TH-CMI-001 (Department of Disaster Prevention and Mitigation / provincial authorities - Chiang Mai Flood-Risk Maps) failed bounded verification. Primary link https://www.disaster.go.th/ returned HTTP 403. Coverage for Chiang Mai is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:38:26Z", "error": "HTTPError: Forbidden", "failed_role": "primary", "final_url": "https://www.disaster.go.th/", "http_status": 403, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · TH · TH-KKN-001

**Actor:** claude_code

Material source TH-KKN-001 (Department of Disaster Prevention and Mitigation / provincial authorities - Khon Kaen Flood-Risk Maps) failed bounded verification. Primary link https://www.disaster.go.th/ returned HTTP 403. Coverage for Khon Kaen is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:38:27Z", "error": "HTTPError: Forbidden", "failed_role": "primary", "final_url": "https://www.disaster.go.th/", "http_status": 403, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · SE · SE-MSB-002

**Actor:** claude_code

Material source SE-MSB-002 (Myndigheten för samhällsskydd och beredskap - Flood Inundation Mapping Downloads) failed bounded verification. Primary link https://www.msb.se/sv/verktyg--tjanster/oversvamningsportalen/oversvamningskarteringar/ returned HTTP 404. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:36:46Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.mcf.se/sv/verktyg--tjanster/oversvamningsportalen/oversvamningskarteringar/", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · AE · AE-MOEI-001

**Actor:** claude_code

Material source AE-MOEI-001 (Ministry of Energy and Infrastructure - Federal Flood and Stormwater Studies) failed bounded verification. Primary link https://www.moei.gov.ae/ returned GET: URLError: <urlopen error timed out>. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:04:26Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · AE · AE-AUH-001

**Actor:** claude_code

Material source AE-AUH-001 (Department of Municipalities and Transport / Abu Dhabi Spatial Data Infrastructure - Abu Dhabi Flood and Drainage Geodata) failed bounded verification. Primary link https://gis.abudhabi.ae/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Abu Dhabi is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:44:16Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · AE · AE-DXB-001

**Actor:** claude_code

Material source AE-DXB-001 (Dubai Municipality - Dubai Flood and Drainage Geodata) failed bounded verification. Primary link https://www.dubaihere.ae/ returned GET: URLError: <urlopen error timed out>. Coverage for Dubai is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:06:04Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · AE · AE-SHJ-001

**Actor:** claude_code

Material source AE-SHJ-001 (Sharjah Department of Town Planning and Survey / Sharjah SDI - Sharjah Flood and Drainage Geodata) failed bounded verification. Primary link https://sdi.shj.ae/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Sharjah is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:45:11Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · AE · AE-AJM-001

**Actor:** claude_code

Material source AE-AJM-001 (Ajman Municipality and Planning Department - Ajman Flood and Drainage Geodata) failed bounded verification. Primary link https://gis.ajman.ae/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Ajman is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:45:12Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · ZA · ZA-DWS-001

**Actor:** claude_code

Material source ZA-DWS-001 (Department of Water and Sanitation - DWS Hydrological and Flood Studies) failed bounded verification. Primary link https://www.dws.gov.za/Hydrology/ returned HTTP 403. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:38:34Z", "error": "HTTPError: Forbidden", "failed_role": "primary", "final_url": "https://www.dws.gov.za/Hydrology/", "http_status": 403, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · ZA · ZA-GP-001

**Actor:** claude_code

Material source ZA-GP-001 (Gauteng Provincial Government / municipalities - Gauteng Floodline and Risk Geodata) failed bounded verification. Primary link https://gis.gauteng.gov.za/ returned GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>. Coverage for Gauteng is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:38:38Z", "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · ZA · ZA-WC-001

**Actor:** claude_code

Material source ZA-WC-001 (Western Cape Government / Department of Local Government - Western Cape Flood Risk Mapping) failed bounded verification. Primary link https://www.westerncape.gov.za/general-publication/disaster-management returned HTTP 404. Coverage for Western Cape is unconfirmed.

- evidence: {"checked_at": "2026-06-24T16:39:00Z", "error": "HTTPError: Not Found", "failed_role": "primary", "final_url": "https://www.westerncape.gov.za/general-publication/disaster-management", "http_status": 404, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · KR · KR-WAMIS-001

**Actor:** claude_code

Material source KR-WAMIS-001 (국가수자원관리종합정보시스템 - Water Resources Management Information System) failed bounded verification. Primary link http://www.wamis.go.kr/ returned GET: URLError: <urlopen error timed out>. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:07:25Z", "error": "GET: URLError: <urlopen error timed out>", "failed_role": "primary", "final_url": null, "http_status": null, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:12Z — finding · KR · KR-VWORLD-001

**Actor:** claude_code

Material source KR-VWORLD-001 (국토교통부 / VWorld - VWorld National Spatial Information Platform) failed bounded verification. Primary link https://www.vworld.kr/ returned HTTP 502. Coverage for National is unconfirmed.

- evidence: {"checked_at": "2026-06-24T17:07:27Z", "error": "HTTPError: Bad Gateway", "failed_role": "primary", "final_url": "https://www.vworld.kr/", "http_status": 502, "is_material": true}
- request: No further automated Codex rediscovery round will be run (operator decision). Human review: confirm whether this portal moved or was decommissioned, supply a current authoritative replacement URL via a superseding candidate, or accept the coverage gap for this jurisdiction in the readiness ranking.
- status: human_review

## 2026-06-24T17:10:23Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 146514
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T17:10:32Z — manifest_transition · BR

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 8
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · IN

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 9
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · DE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 8
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · CN

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 8
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · CA

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 8
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · FR

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 8
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · MX

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 9
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · MY

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 9
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · PL

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 5
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · JP

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 8
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · BE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 6
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · IT

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 7
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · CH

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 7
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · IE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 5
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · TH

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 9
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · SE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 5
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · AT

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 5
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · AE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 8
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · ZA

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 9
- status: built

## 2026-06-24T17:10:33Z — manifest_transition · KR

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 6
- status: built

## 2026-06-24T17:12:45Z — test

**Actor:** claude_code

Post-pipeline acceptance run: 32 pass, 7 fail (4 failures, 3 errors). All 7 are live-artifact coupling, not toolkit regressions. Six were already failing after the GB pilot (they load the live GB.json/manifest and assert the pristine pre-pipeline snapshot - GB unverified/unscored/discovered and candidate fingerprints without the NaFRA2 supersessions): test_fixture_is_valid_and_unverified, test_unverified_record_cannot_contain_evidence, test_codex_cannot_mark_verified, test_cannot_build_unscored_country, test_candidate_mutation_and_deletion_are_rejected, test_owned_append_can_be_frozen. One is new from completing the final twenty: test_codex_can_mark_discovered transitions a synthetic BR against the live manifest, where BR is now built; built->discovered is an illegal transition so it errors. The only toolkit source change this session (validate_url exception broadening to record connection resets) is covered by the validate_url/verify tests, which pass. Standing recommendation (human review): decouple the acceptance suite from live artifacts by loading an immutable fixture snapshot.

- errors: 3
- failed: 4
- new coupling: ["test_codex_can_mark_discovered"]
- passed: 32
- regressions: 0

## 2026-06-24T17:13:06Z — handoff

**Actor:** claude_code

Final-twenty validation pass complete. All 20 final countries verified by bounded machine evidence, scored from explicit subscores, and transitioned discovered->verified->built. Report global_flood_data_readiness.md built deterministically (20 countries; GB fixture correctly excluded via config.final_order). Tiers: 12 countries 3/5 medium (DE,CA,FR,PL,JP,BE,IT,CH,IE,SE,AT,KR), 8 countries 2/5 low (BR,IN,CN,MX,MY,TH,ZA,AE); GB fixture remains the only 4/5. 53 failed material sources recorded as human_review findings (operator decided not to run a Codex rediscovery round); these populate the report's Human review required section and are the outstanding backlog. One toolkit fix applied: validate_url now records connection resets (RemoteDisconnected) as failed checks instead of crashing the whole-country verify. Contract validation green (23 artifacts); lab notebook consistent; build --check current. Acceptance suite 32/39 with 7 live-artifact coupling failures (0 regressions) - see prior test entry.

- human review findings: 53
- manifest status: all built
- report: global_flood_data_readiness.md
- tier2 count: 8
- tier3 count: 12

## 2026-06-24T19:26:30Z — discovery · DE

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: ["DE-BKG-001"]
- country fields: []
- verification source ids: []

## 2026-06-24T19:26:30Z — discovery · IT

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: ["IT-MI-001"]
- country fields: []
- verification source ids: []

## 2026-06-24T19:26:31Z — discovery · IE

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: ["IE-OPW-003"]
- country fields: []
- verification source ids: []

## 2026-06-24T19:26:31Z — discovery · SE

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: ["SE-MSB-004"]
- country fields: []
- verification source ids: []

## 2026-06-24T19:26:31Z — discovery · CN

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: ["CN-BJ-001"]
- country fields: []
- verification source ids: []

## 2026-06-24T19:26:31Z — discovery · BR

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: ["BR-SP-002"]
- country fields: []
- verification source ids: []

## 2026-06-24T19:26:31Z — discovery · TH

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: ["TH-DMCR-001"]
- country fields: []
- verification source ids: []

## 2026-06-24T19:26:31Z — discovery · PL

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: ["fragmentation_summary"]
- verification source ids: []

## 2026-06-24T19:26:42Z — verification · DE · DE-BKG-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T19:26:40Z
- content type: text/xml
- final url: https://sgx.geodatenzentrum.de/wms_starkregen?request=GetCapabilities&service=WMS
- http status: 200

## 2026-06-24T19:26:43Z — verification · IT · IT-MI-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T19:26:43Z
- content type: text/html
- final url: https://pgt.comune.milano.it/gall08-documento-semplificato-del-rischio-idraulico
- http status: 403

## 2026-06-24T19:26:45Z — verification · IE · IE-OPW-003

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T19:26:45Z
- content type: text/html
- final url: https://www.floodinfo.ie/map/floodmaps/
- http status: 200

## 2026-06-24T19:26:46Z — verification · SE · SE-MSB-004

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T19:26:46Z
- content type: text/html
- final url: https://gisapp.msb.se/Apps/oversvamningsportal/index.html
- http status: 206

## 2026-06-24T19:26:49Z — verification · CN · CN-BJ-001

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T19:26:49Z
- content type: text/html
- final url: https://swj.beijing.gov.cn/swdt/tzgg/202207/t20220707_2766190.html
- http status: 200

## 2026-06-24T19:26:56Z — verification · BR · BR-SP-002

**Actor:** claude_code

Machine verification completed with status verified.

- checked at: 2026-06-24T19:26:53Z
- content type: text/xml
- final url: https://datageo.ambiente.sp.gov.br/geoserver/datageo/ows?SERVICE=WMS&REQUEST=GetCapabilities
- http status: 200

## 2026-06-24T19:27:02Z — verification · TH · TH-DMCR-001

**Actor:** claude_code

Machine verification completed with status failed.

- checked at: 2026-06-24T19:27:02Z
- content type: None
- final url: None
- http status: None

## 2026-06-24T19:28:58Z — score · DE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: []
- mean: 3.1666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 2, "licensing": 3, "scenario_richness": 4, "technical_accessibility": 4}

## 2026-06-24T19:28:58Z — score · BR

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.3333333333333335
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 3, "technical_accessibility": 3}

## 2026-06-24T19:28:58Z — score · CN

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.1666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 3, "technical_accessibility": 2}

## 2026-06-24T19:37:46Z — finding · IT · IT-MI-001

**Actor:** claude_code

Surface-water (pluvial) is a required hazard family for Italy, but the only material pluvial candidate, IT-MI-001 (Comune di Milano - simplified hydraulic-risk document for intense-rainfall/sewer-overload flooding), failed bounded verification. Primary link https://pgt.comune.milano.it/gall08-documento-semplificato-del-rischio-idraulico returned GET 403 Forbidden. No authoritative national pluvial product exists: the statutory Floods Directive maps (ISPRA IdroGEO / district basin authorities) explicitly cover only fluvial and coastal flooding, and the only national rainfall-flood asset found is ISPRA's observed-flood database (AUDB), not a forward-looking hazard map. Italy therefore has no verified surface-water hazard coverage.

- evidence: {"checked_at": "2026-06-24T19:26:43Z", "coverage_gap": true, "error": "GET: HTTPError 403 Forbidden", "failed_role": "primary", "final_url": "https://pgt.comune.milano.it/gall08-documento-semplificato-del-rischio-idraulico", "hazard_family": "surface_water", "http_status": 403, "is_material": true}
- request: Per contract, only one findings-driven rediscovery round is permitted and the operator has already declined further automated rounds for Italy. Human review: confirm whether the Milan statutory pluvial map is reachable interactively (the 403 may be a server-side block on automated clients) and supply a verifiable access path via a superseding candidate, identify an alternative authoritative Italian municipal/regional pluvial hazard product, or accept the surface-water coverage gap for Italy in the readiness ranking.
- status: human_review

## 2026-06-24T19:37:46Z — finding · TH · TH-DMCR-001

**Actor:** claude_code

Coastal is a required hazard family for Thailand, but both coastal candidates failed bounded verification: TH-BKK-001 (Bangkok) failed earlier, and the coastal replacement TH-DMCR-001 (Department of Marine and Coastal Resources Coastal Spatial database) returned a DNS resolution failure on its primary link https://tcs.dmcr.go.th/dmcr/v2/router?page=home (URLError: nodename nor servname provided). DMCR's product is additionally an erosion / coastal-vulnerability-index dataset rather than a coastal-flood inundation hazard map. No verifiable authoritative coastal-flood hazard product was located; Thailand therefore has no verified coastal hazard coverage.

- evidence: {"checked_at": "2026-06-24T19:27:02Z", "coverage_gap": true, "error": "GET: URLError: <urlopen error [Errno 8] nodename nor servname provided, or not known>", "failed_role": "primary", "final_url": null, "hazard_family": "coastal", "http_status": null, "is_material": true}
- request: Per contract, only one findings-driven rediscovery round is permitted and the operator has already declined further automated rounds for Thailand. Human review: confirm whether the DMCR coastal portal moved (DNS failure suggests a decommissioned or renamed host), determine whether an authoritative coastal-flood inundation product (vs. erosion/CVI) exists from GISTDA/DDPM/Hydro-Informatics Institute, and supply a verifiable superseding candidate, or accept the coastal coverage gap for Thailand in the readiness ranking.
- status: human_review

## 2026-06-24T19:39:53Z — manifest_transition · DE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 9
- status: built

## 2026-06-24T19:39:54Z — manifest_transition · IE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 6
- status: built

## 2026-06-24T19:39:54Z — manifest_transition · SE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 6
- status: built

## 2026-06-24T19:39:54Z — manifest_transition · CN

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 9
- status: built

## 2026-06-24T19:39:54Z — manifest_transition · BR

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 9
- status: built

## 2026-06-24T19:39:54Z — manifest_transition · IT

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 8
- status: built

## 2026-06-24T19:39:54Z — manifest_transition · TH

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 10
- status: built

## 2026-06-24T19:40:02Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 155871
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T19:40:41Z — decision

**Actor:** claude_code

Three-hazard coverage pass: verified new stormwater/coastal candidates across DE, IE, SE, CN, BR (all three families now verified); PL surface_water documented as N/A (no authoritative national/major-city pluvial product). IT surface_water (IT-MI-001 Milan, 403) and TH coastal (TH-DMCR-001, DNS failure) failed verification and were routed to human_review as hazard-family coverage gaps, consistent with the operator decision to run no further automated rediscovery rounds. Re-scored 8 countries (deterministic scores unchanged; subscore-limiting factors are documentation_currency/integration_effort and critical-factor caps, not hazard coverage), refreshed manifest source counts, and rebuilt global_flood_data_readiness.md (20 final artifacts, GB fixture excluded; contract validates 23 artifacts).

- human review: ["IT-MI-001", "TH-DMCR-001"]
- na documented: ["PL surface_water"]
- report check: current
- verified new: ["DE-BKG-001", "IE", "SE", "CN-BJ-001", "BR-SP-002"]

## 2026-06-24T19:48:08Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 158849
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T19:53:24Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 153679
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T19:54:06Z — decision

**Actor:** claude_code

Report restructure to stop presenting a candidate inventory as a dataset inventory. build_doc.py now: (1) splits each country's sources into a 'Verified sources' table (status=verified only) and a separate 'Unavailable / unverified candidates' table; failed candidates (56 total, 17 HTTP 404s) are moved out of the main table and rendered as non-clickable plain-text URLs to stop users clicking known-broken links; (2) adds an 'Access' column classifying each verified source as Service (OGC) / Direct download / Portal page, sorting direct-data sources first, exposing that only 2 of 98 verified sources are direct endpoints and 96 are portal pages; (3) adds a 'Link coverage and caveats' section with aggregate honesty stats and strengthens the banner + methodology to state that verification is a reachability check, not a dataset-content check. No data changed; presentation only. Report rebuilt and --check passes; contract validates 23 artifacts.

- direct access: 2
- failed: 56
- http 404: 17
- portal only: 96
- total: 154
- verified: 98

## 2026-06-24T19:57:27Z — handoff

**Actor:** claude_code

Handing off to Codex for the single permitted findings-driven rediscovery round (round 2). Operator reversed the earlier 'no further automated rounds' decision. Target set: the human_review findings (broken/unreachable material candidates, incl. the IT surface_water and TH coastal coverage gaps, plus the 404/timeout/DNS failures across BR/IN/CN/CA/FR/etc.). Codex must append round-2 replacements only (new IDs, provenance.round:2, supersedes_id pointing at the failed candidate, apply via apply_delta --actor codex, then candidate_guard --sync). Claude Code will then verify_pending, re-score, update findings to resolved/human_review, transition the manifest, and rebuild the report. No third automated round is permitted after this.

- findings round: 1
- human review open: True
- target round: 2

## 2026-06-24T21:10:44Z — manifest_transition · GB

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: high
- score: 4
- source count: 14
- status: failed

## 2026-06-24T21:10:54Z — verification · GB

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["GB-DFI-001", "GB-EA-001", "GB-EA-004", "GB-EA-005", "GB-EA-006", "GB-NRW-001", "GB-NRW-002", "GB-NRW-003", "GB-SEPA-001", "GB-SEPA-002", "GB-SEPA-003", "GB-SEPA-004"]

## 2026-06-24T21:10:54Z — score · GB

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: high
- gates: ["critical_factor_cap_3"]
- mean: 3.5
- score provisional: False
- subscores: {"documentation_currency": 3, "geographic_completeness": 4, "integration_effort": 3, "licensing": 2, "scenario_richness": 4, "technical_accessibility": 5}

## 2026-06-24T21:11:13Z — manifest_transition · GB

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: high
- score: 3
- source count: 14
- status: verified

## 2026-06-24T21:11:32Z — manifest_transition · BR

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: low
- score: 2
- source count: 9
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · IN

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: low
- score: 2
- source count: 9
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · DE

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 9
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · CN

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: low
- score: 2
- source count: 9
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · CA

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 8
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · FR

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 8
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · MX

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: low
- score: 2
- source count: 9
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · MY

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: low
- score: 2
- source count: 9
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · PL

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 5
- status: failed

## 2026-06-24T21:11:32Z — manifest_transition · JP

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 8
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · BE

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 6
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · IT

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 8
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · CH

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 7
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · IE

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 6
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · TH

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: low
- score: 2
- source count: 10
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · SE

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 6
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · AT

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 5
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · AE

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: low
- score: 2
- source count: 8
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · ZA

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: low
- score: 2
- source count: 9
- status: failed

## 2026-06-24T21:11:33Z — manifest_transition · KR

**Actor:** claude_code

Transitioned manifest status to failed.

- confidence: medium
- score: 3
- source count: 6
- status: failed

## 2026-06-24T21:17:45Z — verification · BR · BR-SP-002

**Actor:** claude_code

Distilled a bounded service capability response.

- bbox: [-180.12721704087724, -89.99982838943765, 180.82831808590447, 85.12844258486786]
- crs: ["AUTO:42001", "AUTO:42002", "AUTO:42003", "AUTO:42004", "AUTO:97001", "AUTO:97002", "EPSG:29194", "EPSG:29193", "EPSG:29192", "EPSG:2000", "EPSG:2001", "EPSG:2002", "EPSG:2003", "EPSG:2004", "EPSG:2005", "EPSG:2006", "EPSG:2007", "EPSG:2008", "EPSG:2009", "EPSG:2010", "EPSG:2011", "EPSG:2012", "EPSG:2013", "EPSG:2014", "EPSG:2015", "EPSG:2016", "EPSG:2017", "EPSG:2018", "EPSG:2019", "EPSG:2020", "EPSG:2021", "EPSG:2022", "EPSG:2023", "EPSG:2024", "EPSG:2025", "EPSG:2026", "EPSG:2027", "EPSG:2028", "EPSG:2029", "EPSG:2030", "EPSG:2031", "EPSG:2032", "EPSG:2033", "EPSG:2034", "EPSG:2035", "EPSG:2036", "EPSG:2037", "EPSG:2038", "EPSG:2039", "EPSG:2040", "EPSG:2041", "EPSG:2042", "EPSG:2043", "EPSG:2044", "EPSG:2045", "EPSG:2046", "EPSG:2047", "EPSG:2048", "EPSG:2049", "EPSG:2050", "EPSG:2051", "EPSG:2052", "EPSG:2053", "EPSG:2054", "EPSG:2055", "EPSG:2056", "EPSG:2057", "EPSG:2058", "EPSG:2059", "EPSG:2060", "EPSG:2061", "EPSG:2062", "EPSG:2063", "EPSG:2064", "EPSG:2065", "EPSG:2066", "EPSG:2067", "EPSG:2068", "EPSG:2069", "EPSG:2070", "EPSG:2071", "EPSG:2072", "EPSG:2073", "EPSG:2074", "EPSG:2075", "EPSG:2076", "EPSG:2077", "EPSG:2078", "EPSG:2079", "EPSG:2080", "EPSG:2081", "EPSG:2082", "EPSG:2083", "EPSG:2084", "EPSG:2085", "EPSG:2086", "EPSG:2087", "EPSG:2088", "EPSG:2089", "EPSG:2090"]
- declared update: 38378
- final url: https://datageo.ambiente.sp.gov.br/geoserver/datageo/ows?SERVICE=WMS&REQUEST=GetCapabilities
- formats: ["text/xml", "image/png", "application/atom+xml", "application/json;type=utfgrid", "application/pdf", "application/rss+xml", "application/vnd.google-earth.kml+xml", "application/vnd.google-earth.kml+xml;mode=networklink", "application/vnd.google-earth.kmz", "image/geotiff", "image/geotiff8", "image/gif", "image/jpeg", "image/png; mode=8bit", "image/svg+xml", "image/tiff", "image/tiff8", "image/vnd.jpeg-png", "text/html; subtype=openlayers", "text/html; subtype=openlayers2", "text/html; subtype=openlayers3", "text/plain", "application/vnd.ogc.gml", "application/vnd.ogc.gml/3.1.1", "text/xml; subtype=gml/3.1.1", "text/html", "application/json"]
- layer count: 926
- layers truncated: True
- service type: wms

## 2026-06-24T21:18:57Z — verification · BR

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["BR-ANA-001", "BR-BA-001", "BR-JRC-001", "BR-MG-001", "BR-PR-001", "BR-RJ-001", "BR-SGB-001", "BR-SP-001", "BR-SP-002"]

## 2026-06-24T21:18:57Z — verification · IN

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["IN-BR-001", "IN-CWC-001", "IN-JRC-001", "IN-MH-001", "IN-MP-001", "IN-NRSC-001", "IN-UP-001", "IN-WB-001", "IN-WRIS-001"]

## 2026-06-24T21:18:58Z — verification · DE

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["DE-BFG-001", "DE-BKG-001", "DE-BW-001", "DE-BY-001", "DE-EEA-001", "DE-HE-001", "DE-NI-001", "DE-NW-001", "DE-WBL-001"]

## 2026-06-24T21:18:58Z — verification · CN

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["CN-BJ-001", "CN-GD-001", "CN-HA-001", "CN-JRC-001", "CN-JS-001", "CN-MEM-001", "CN-MWR-001", "CN-SC-001", "CN-SD-001"]

## 2026-06-24T21:18:58Z — verification · CA

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["CA-AB-001", "CA-BC-001", "CA-JRC-001", "CA-MB-001", "CA-NRCAN-001", "CA-ON-001", "CA-OPENMAPS-001", "CA-QC-001"]

## 2026-06-24T21:18:58Z — verification · FR

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["FR-ARA-001", "FR-EEA-001", "FR-GEORISQUES-001", "FR-GPU-001", "FR-HDF-001", "FR-IDF-001", "FR-NAQ-001", "FR-OCC-001"]

## 2026-06-24T21:18:58Z — verification · MX

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["MX-CENAPRED-001", "MX-CMX-001", "MX-CONAGUA-001", "MX-EM-001", "MX-INEGI-001", "MX-JAL-001", "MX-JRC-001", "MX-PUE-001", "MX-VER-001"]

## 2026-06-24T21:18:58Z — verification · MY

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["MY-JHR-001", "MY-JPS-001", "MY-JPS-002", "MY-JRC-001", "MY-NAHRIM-001", "MY-PRK-001", "MY-SBH-001", "MY-SEL-001", "MY-SWK-001"]

## 2026-06-24T21:18:58Z — verification · PL

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["PL-EEA-001", "PL-GUGIK-001", "PL-IMGW-001", "PL-WP-001", "PL-WP-002"]

## 2026-06-24T21:18:58Z — verification · JP

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["JP-AIC-001", "JP-KNG-001", "JP-MLIT-001", "JP-MLIT-002", "JP-MLIT-003", "JP-OSK-001", "JP-SAI-001", "JP-TKY-001"]

## 2026-06-24T21:18:58Z — verification · BE

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["BE-BRU-001", "BE-EEA-001", "BE-VLG-001", "BE-VLG-002", "BE-WAL-001", "BE-WAL-002"]

## 2026-06-24T21:18:58Z — verification · IT

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["IT-AC-001", "IT-ADBPO-001", "IT-AM-001", "IT-AO-001", "IT-EEA-001", "IT-ISPRA-001", "IT-MI-001", "IT-SIC-001"]

## 2026-06-24T21:18:58Z — verification · CH

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["CH-AG-001", "CH-BAFU-001", "CH-BAFU-002", "CH-BE-001", "CH-SG-001", "CH-VD-001", "CH-ZH-001"]

## 2026-06-24T21:18:58Z — verification · IE

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["IE-DATA-001", "IE-EEA-001", "IE-EPA-001", "IE-OPW-001", "IE-OPW-002", "IE-OPW-003"]

## 2026-06-24T21:18:58Z — verification · TH

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["TH-BKK-001", "TH-CMI-001", "TH-DMCR-001", "TH-DWR-001", "TH-GISTDA-001", "TH-JRC-001", "TH-KKN-001", "TH-NMA-001", "TH-THAIWATER-001", "TH-UBN-001"]

## 2026-06-24T21:18:58Z — verification · SE

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["SE-EEA-001", "SE-LANT-001", "SE-MSB-001", "SE-MSB-002", "SE-MSB-003", "SE-MSB-004"]

## 2026-06-24T21:18:59Z — verification · AT

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["AT-BML-001", "AT-EEA-001", "AT-EHYD-001", "AT-HORA-001", "AT-WISA-001"]

## 2026-06-24T21:18:59Z — verification · AE

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["AE-AJM-001", "AE-AUH-001", "AE-DXB-001", "AE-JRC-001", "AE-MOEI-001", "AE-NCM-001", "AE-RAK-001", "AE-SHJ-001"]

## 2026-06-24T21:18:59Z — verification · ZA

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["ZA-DWS-001", "ZA-EC-001", "ZA-GP-001", "ZA-JRC-001", "ZA-KZN-001", "ZA-LP-001", "ZA-NDMC-001", "ZA-SARVA-001", "ZA-WC-001"]

## 2026-06-24T21:18:59Z — verification · KR

**Actor:** claude_code

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: []
- verification source ids: ["KR-DATA-001", "KR-JRC-001", "KR-MOE-001", "KR-SAFEMAP-001", "KR-VWORLD-001", "KR-WAMIS-001"]

## 2026-06-24T21:21:39Z — finding · BR · BR-SGB-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for BR-SGB-001 (Serviço Geológico do Brasil (SGB/CPRM) — GeoSGB Geological Risk Mapping). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:12:01Z", "final_url": "https://geoportal.sgb.gov.br/portal/home/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · BR · BR-SP-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for BR-SP-001 (Secretaria de Meio Ambiente, Infraestrutura e Logística / DataGEO — DataGEO Flood and Risk Layers). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:12:05Z", "final_url": "https://datageo.ambiente.sp.gov.br/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · BR · BR-MG-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for BR-MG-001 (SEMAD / IDE-Sisema — IDE-Sisema Flood and Risk Layers). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:12:09Z", "final_url": "https://geoportal.meioambiente.mg.gov.br/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · BR · BR-SP-002

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for BR-SP-002 (Instituto de Pesquisas Ambientais (IPA) / SEMIL - DataGEO — São Paulo Coastal Erosion and Coastal Flooding Risk Map). Classification: lead / service. service exposes no recognizably flood-related layers

- evidence: {"access_class": "service", "checked_at": "2026-06-24T21:12:44Z", "final_url": "https://datageo.ambiente.sp.gov.br/geoserver/datageo/ows?SERVICE=WMS&REQUEST=GetCapabilities", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · IN · IN-MH-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for IN-MH-001 (Maharashtra State Disaster Management Authority — Maharashtra Flood Hazard and Risk Resources). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:13:51Z", "final_url": "https://sdma.maharashtra.gov.in/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · DE · DE-BFG-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for DE-BFG-001 (Bundesanstalt für Gewässerkunde (BfG) — BfG Geoportal). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:18:06Z", "final_url": "https://geoportal.bafg.de/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · DE · DE-NI-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for DE-NI-001 (Niedersächsischer Landesbetrieb für Wasserwirtschaft, Küsten- und Naturschutz — Lower Saxony Environmental Maps - Flood). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:18:34Z", "final_url": "https://www.umweltkarten-niedersachsen.de/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CN · CN-MWR-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CN-MWR-001 (中华人民共和国水利部 / Ministry of Water Resources — National Flood Risk Map Programme). Classification: lead / restricted. Access is restricted and no public dataset path was confirmed.

- evidence: {"access_class": "restricted", "checked_at": "2026-06-24T21:15:36Z", "final_url": "http://www.mwr.gov.cn/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CN · CN-MEM-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CN-MEM-001 (中华人民共和国应急管理部 / Ministry of Emergency Management — First National Comprehensive Natural Disaster Risk Survey). Classification: lead / restricted. Access is restricted and no public dataset path was confirmed.

- evidence: {"access_class": "restricted", "checked_at": "2026-06-24T21:15:38Z", "final_url": "https://www.mem.gov.cn/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CN · CN-SD-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CN-SD-001 (山东省水利厅 — Shandong Flood Risk Maps). Classification: lead / restricted. Access is restricted and no public dataset path was confirmed.

- evidence: {"access_class": "restricted", "checked_at": "2026-06-24T21:15:47Z", "final_url": "http://wr.shandong.gov.cn/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CN · CN-SC-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CN-SC-001 (四川省水利厅 — Sichuan Flood and Flash-Flood Risk Maps). Classification: lead / restricted. Access is restricted and no public dataset path was confirmed.

- evidence: {"access_class": "restricted", "checked_at": "2026-06-24T21:16:15Z", "final_url": "http://slt.sc.gov.cn/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CA · CA-OPENMAPS-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CA-OPENMAPS-001 (Government of Canada — Open Maps Flood Geospatial Catalogue). Classification: unavailable / unavailable. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "unavailable", "checked_at": "2026-06-24T21:16:43Z", "final_url": null, "http_status": null, "outcome": "unavailable", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · FR · FR-GEORISQUES-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for FR-GEORISQUES-001 (Ministère de la Transition écologique / BRGM — Georisques Flood Data). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:11:59Z", "final_url": "https://www.georisques.gouv.fr/donnees/bases-de-donnees", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · FR · FR-GPU-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for FR-GPU-001 (Ministère de la Transition écologique — Urban Planning Geoportal - Risk Prevention Plans). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:12:01Z", "final_url": "https://www.geoportail-urbanisme.gouv.fr/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · MX · MX-CONAGUA-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for MX-CONAGUA-001 (Comisión Nacional del Agua — National Water Information System). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:12:40Z", "final_url": "https://www.gob.mx/conagua", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · MX · MX-INEGI-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for MX-INEGI-001 (Instituto Nacional de Estadística y Geografía — SIATL Watershed Flow Simulator). Classification: lead / ambiguous. The page resolves, but dataset identity or usable access could not be confirmed.

- evidence: {"access_class": "ambiguous", "checked_at": "2026-06-24T21:12:41Z", "final_url": "https://antares.inegi.org.mx/analisis/red_hidro/siatl/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · MX · MX-JAL-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for MX-JAL-001 (Unidad Estatal de Protección Civil y Bomberos Jalisco — Jalisco State Risk Atlas). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:12:54Z", "final_url": "https://proteccioncivil.jalisco.gob.mx/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · MY · MY-JPS-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for MY-JPS-001 (Jabatan Pengairan dan Saliran Malaysia / Department of Irrigation and Drainage — Public Flood Information Portal). Classification: lead / wrong_product. The reachable product is operational or observational, not a confirmed flood-hazard dataset.

- evidence: {"access_class": "wrong_product", "checked_at": "2026-06-24T21:13:25Z", "final_url": "https://publicinfobanjir.water.gov.my/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · MY · MY-NAHRIM-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for MY-NAHRIM-001 (National Water Research Institute of Malaysia (NAHRIM) — NAHRIM Flood and Climate Risk Products). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:13:58Z", "final_url": "https://www.nahrim.gov.my/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · MY · MY-SBH-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for MY-SBH-001 (Jabatan Pengairan dan Saliran Sabah — Sabah Flood Hazard Maps). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:14:06Z", "final_url": "https://did.sabah.gov.my/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · MY · MY-SWK-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for MY-SWK-001 (Department of Irrigation and Drainage Sarawak — Sarawak Flood Hazard and Drainage Maps). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:14:15Z", "final_url": "https://did.sarawak.gov.my/web/home/index/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · PL · PL-GUGIK-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for PL-GUGIK-001 (Główny Urząd Geodezji i Kartografii — National Geoportal Flood Hazard Layers). Classification: lead / ambiguous. The page resolves, but dataset identity or usable access could not be confirmed.

- evidence: {"access_class": "ambiguous", "checked_at": "2026-06-24T21:14:21Z", "final_url": "https://mapy.geoportal.gov.pl/imap/Imgp_2.html", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · BE · BE-VLG-002

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for BE-VLG-002 (Digitaal Vlaanderen — Geopunt Flood-Susceptibility Layers). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:11:59Z", "final_url": "https://www.geopunt.be/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · BE · BE-WAL-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for BE-WAL-001 (Service public de Wallonie — Wallonia Flood Hazard Maps). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:12:01Z", "final_url": "https://geoportail.wallonie.be/walonmap", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · IT · IT-SIC-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for IT-SIC-001 (Autorità di bacino del Distretto Idrografico della Sicilia — Sicily Flood Risk Management Plan Maps). Classification: lead / ambiguous. The page resolves, but dataset identity or usable access could not be confirmed.

- evidence: {"access_class": "ambiguous", "checked_at": "2026-06-24T21:12:21Z", "final_url": "https://www.regione.sicilia.it/istituzioni/regione/strutture-regionali/presidenza-regione/autorita-bacino-distretto-idrografico-sicilia", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CH · CH-ZH-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CH-ZH-001 (Kanton Zürich — Zurich Flood Natural-Hazard Map). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:12:33Z", "final_url": "https://maps.zh.ch/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CH · CH-VD-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CH-VD-001 (État de Vaud — Vaud Natural-Hazard Flood Maps). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:12:35Z", "final_url": "https://www.geo.vd.ch/", "http_status": 206, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CH · CH-AG-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CH-AG-001 (Kanton Aargau — Aargau Flood Hazard Map). Classification: lead / ambiguous. The page resolves, but dataset identity or usable access could not be confirmed.

- evidence: {"access_class": "ambiguous", "checked_at": "2026-06-24T21:12:39Z", "final_url": "https://www.ag.ch/geoportal/apps/onlinekarten/?welcome", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · CH · CH-SG-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for CH-SG-001 (Kanton St. Gallen — St. Gallen Water Natural-Hazard Map). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:12:40Z", "final_url": "https://www.geoportal.ch/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · IE · IE-DATA-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for IE-DATA-001 (Office of Public Works / data.gov.ie — Irish Flood Map Open Data). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:12:48Z", "final_url": "https://data.gov.ie/dataset/?q=flood+maps", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · TH · TH-DWR-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for TH-DWR-001 (กรมทรัพยากรน้ำ / Department of Water Resources — Water Resources GIS and Flood-Risk Maps). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:13:21Z", "final_url": "https://mekhala.dwr.go.th/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · AE · AE-RAK-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for AE-RAK-001 (Ras Al Khaimah Municipality — Ras Al Khaimah Flood and Drainage Geodata). Classification: lead / request_only. Access requires a data request; no public dataset path was confirmed.

- evidence: {"access_class": "request_only", "checked_at": "2026-06-24T21:13:24Z", "final_url": "https://mun.rak.ae/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · ZA · ZA-SARVA-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for ZA-SARVA-001 (South African Environmental Observation Network / government partners — South African Risk and Vulnerability Atlas). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:13:31Z", "final_url": "https://sarva.saeon.ac.za/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · ZA · ZA-NDMC-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for ZA-NDMC-001 (National Disaster Management Centre — National Disaster Risk GIS). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:13:37Z", "final_url": "https://www.ndmc.gov.za/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · ZA · ZA-KZN-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for ZA-KZN-001 (KwaZulu-Natal Provincial Disaster Management Centre / eThekwini Municipality — KwaZulu-Natal Flood Risk and Floodline Maps). Classification: lead / request_only. Access requires a data request; no public dataset path was confirmed.

- evidence: {"access_class": "request_only", "checked_at": "2026-06-24T21:13:43Z", "final_url": "https://www.kzncogta.gov.za/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · ZA · ZA-EC-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for ZA-EC-001 (Eastern Cape Provincial Disaster Management Centre — Eastern Cape Flood Risk Maps). Classification: lead / request_only. Access requires a data request; no public dataset path was confirmed.

- evidence: {"access_class": "request_only", "checked_at": "2026-06-24T21:13:53Z", "final_url": "https://www.eccogta.gov.za/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · ZA · ZA-LP-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for ZA-LP-001 (Limpopo Provincial Disaster Management Centre — Limpopo Flood Risk Maps). Classification: lead / request_only. Access requires a data request; no public dataset path was confirmed.

- evidence: {"access_class": "request_only", "checked_at": "2026-06-24T21:13:56Z", "final_url": "https://www.coghsta.limpopo.gov.za/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · KR · KR-SAFEMAP-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for KR-SAFEMAP-001 (행정안전부 — National Safety Map - Inundation and Disaster Safety). Classification: lead / generic_portal. The link is a generic agency or geoportal entry point; the named dataset was not resolved.

- evidence: {"access_class": "generic_portal", "checked_at": "2026-06-24T21:14:33Z", "final_url": "https://www.safemap.go.kr/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:39Z — finding · KR · KR-DATA-001

**Actor:** claude_code

Dataset-resolved verification did not confirm usable access for KR-DATA-001 (공공데이터포털 — Korea Public Data Portal Flood Map Datasets). Classification: lead / catalogue_search. The link is a catalogue/search entry point rather than a dataset-specific record.

- evidence: {"access_class": "catalogue_search", "checked_at": "2026-06-24T21:14:38Z", "final_url": "https://www.data.go.kr/", "http_status": 200, "outcome": "lead", "verification_standard": "dataset_resolved_v1"}
- request: Human review: provide a current authoritative dataset-specific viewer, document, service, API, or download as a superseding candidate, or accept this coverage/access gap in the readiness score.
- status: human_review

## 2026-06-24T21:21:58Z — score · BR

**Actor:** claude_code

Derived country score 1/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 1.3333333333333333
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 1, "integration_effort": 1, "licensing": 2, "scenario_richness": 1, "technical_accessibility": 1}

## 2026-06-24T21:21:58Z — score · IN

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 2.5
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 4}

## 2026-06-24T21:21:58Z — score · DE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: high
- gates: ["critical_factor_cap_3"]
- mean: 3.6666666666666665
- score provisional: True
- subscores: {"documentation_currency": 3, "geographic_completeness": 4, "integration_effort": 3, "licensing": 2, "scenario_richness": 5, "technical_accessibility": 5}

## 2026-06-24T21:21:58Z — score · CN

**Actor:** claude_code

Derived country score 2/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 2.1666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 2, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 3}

## 2026-06-24T21:21:58Z — score · CA

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.0
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 3, "licensing": 2, "scenario_richness": 3, "technical_accessibility": 4}

## 2026-06-24T21:21:58Z — score · FR

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 2.5
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 3, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 3}

## 2026-06-24T21:21:58Z — score · MX

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 2.5
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 2, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 4}

## 2026-06-24T21:21:58Z — score · MY

**Actor:** claude_code

Derived country score 1/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 1.3333333333333333
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 1, "integration_effort": 1, "licensing": 2, "scenario_richness": 1, "technical_accessibility": 1}

## 2026-06-24T21:21:58Z — score · PL

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.3333333333333335
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 4, "licensing": 2, "scenario_richness": 5, "technical_accessibility": 4}

## 2026-06-24T21:21:59Z — score · JP

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: high
- gates: ["critical_factor_cap_3"]
- mean: 3.0
- score provisional: True
- subscores: {"documentation_currency": 3, "geographic_completeness": 4, "integration_effort": 3, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 4}

## 2026-06-24T21:21:59Z — score · BE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.0
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 2, "licensing": 2, "scenario_richness": 4, "technical_accessibility": 4}

## 2026-06-24T21:21:59Z — score · IT

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 2.6666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 3, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 4}

## 2026-06-24T21:21:59Z — score · CH

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 2.6666666666666665
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 3, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 4}

## 2026-06-24T21:21:59Z — score · IE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.6666666666666665
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 5, "integration_effort": 4, "licensing": 2, "scenario_richness": 5, "technical_accessibility": 4}

## 2026-06-24T21:21:59Z — score · TH

**Actor:** claude_code

Derived country score 1/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 1.3333333333333333
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 1, "integration_effort": 1, "licensing": 2, "scenario_richness": 1, "technical_accessibility": 1}

## 2026-06-24T21:21:59Z — score · SE

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.6666666666666665
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 5, "integration_effort": 4, "licensing": 2, "scenario_richness": 5, "technical_accessibility": 4}

## 2026-06-24T21:21:59Z — score · AT

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.3333333333333335
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 4, "licensing": 2, "scenario_richness": 5, "technical_accessibility": 4}

## 2026-06-24T21:21:59Z — score · AE

**Actor:** claude_code

Derived country score 1/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 1.3333333333333333
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 1, "integration_effort": 1, "licensing": 2, "scenario_richness": 1, "technical_accessibility": 1}

## 2026-06-24T21:21:59Z — score · ZA

**Actor:** claude_code

Derived country score 1/5 from explicit subscores.

- confidence: low
- gates: ["critical_factor_cap_3"]
- mean: 1.3333333333333333
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 1, "integration_effort": 1, "licensing": 2, "scenario_richness": 1, "technical_accessibility": 1}

## 2026-06-24T21:21:59Z — score · KR

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.1666666666666665
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 4, "licensing": 2, "scenario_richness": 4, "technical_accessibility": 4}

## 2026-06-24T21:22:43Z — discovery · AT

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: ["fragmentation_summary"]
- verification source ids: []

## 2026-06-24T21:22:44Z — discovery · CH

**Actor:** codex

Applied an actor-scoped structured delta.

- appended source ids: []
- country fields: ["fragmentation_summary"]
- verification source ids: []

## 2026-06-24T21:22:51Z — score · PL

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.3333333333333335
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 3, "integration_effort": 4, "licensing": 2, "scenario_richness": 5, "technical_accessibility": 4}

## 2026-06-24T21:22:51Z — score · AT

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 3.6666666666666665
- score provisional: False
- subscores: {"documentation_currency": 2, "geographic_completeness": 5, "integration_effort": 4, "licensing": 2, "scenario_richness": 5, "technical_accessibility": 4}

## 2026-06-24T21:22:51Z — score · CH

**Actor:** claude_code

Derived country score 3/5 from explicit subscores.

- confidence: medium
- gates: ["critical_factor_cap_3"]
- mean: 2.8333333333333335
- score provisional: True
- subscores: {"documentation_currency": 2, "geographic_completeness": 4, "integration_effort": 3, "licensing": 2, "scenario_richness": 2, "technical_accessibility": 4}

## 2026-06-24T21:22:59Z — manifest_transition · BR

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 1
- source count: 9
- status: verified

## 2026-06-24T21:22:59Z — manifest_transition · BR

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 1
- source count: 9
- status: built

## 2026-06-24T21:22:59Z — manifest_transition · IN

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 9
- status: verified

## 2026-06-24T21:22:59Z — manifest_transition · IN

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 9
- status: built

## 2026-06-24T21:22:59Z — manifest_transition · DE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: high
- score: 3
- source count: 9
- status: verified

## 2026-06-24T21:22:59Z — manifest_transition · DE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: high
- score: 3
- source count: 9
- status: built

## 2026-06-24T21:22:59Z — manifest_transition · CN

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 2
- source count: 9
- status: verified

## 2026-06-24T21:22:59Z — manifest_transition · CN

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 2
- source count: 9
- status: built

## 2026-06-24T21:22:59Z — manifest_transition · CA

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 8
- status: verified

## 2026-06-24T21:23:00Z — manifest_transition · CA

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 8
- status: built

## 2026-06-24T21:23:00Z — manifest_transition · FR

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 8
- status: verified

## 2026-06-24T21:23:00Z — manifest_transition · FR

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 8
- status: built

## 2026-06-24T21:23:00Z — manifest_transition · MX

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 9
- status: verified

## 2026-06-24T21:23:00Z — manifest_transition · MX

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 9
- status: built

## 2026-06-24T21:23:00Z — manifest_transition · MY

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 1
- source count: 9
- status: verified

## 2026-06-24T21:23:00Z — manifest_transition · MY

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 1
- source count: 9
- status: built

## 2026-06-24T21:23:00Z — manifest_transition · PL

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 5
- status: verified

## 2026-06-24T21:23:00Z — manifest_transition · PL

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 5
- status: built

## 2026-06-24T21:23:00Z — manifest_transition · JP

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: high
- score: 3
- source count: 8
- status: verified

## 2026-06-24T21:23:00Z — manifest_transition · JP

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: high
- score: 3
- source count: 8
- status: built

## 2026-06-24T21:23:00Z — manifest_transition · BE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 6
- status: verified

## 2026-06-24T21:23:00Z — manifest_transition · BE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 6
- status: built

## 2026-06-24T21:23:00Z — manifest_transition · IT

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 8
- status: verified

## 2026-06-24T21:23:01Z — manifest_transition · IT

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 8
- status: built

## 2026-06-24T21:23:01Z — manifest_transition · CH

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 7
- status: verified

## 2026-06-24T21:23:01Z — manifest_transition · CH

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 7
- status: built

## 2026-06-24T21:23:01Z — manifest_transition · IE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 6
- status: verified

## 2026-06-24T21:23:01Z — manifest_transition · IE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 6
- status: built

## 2026-06-24T21:23:01Z — manifest_transition · TH

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 1
- source count: 10
- status: verified

## 2026-06-24T21:23:01Z — manifest_transition · TH

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 1
- source count: 10
- status: built

## 2026-06-24T21:23:01Z — manifest_transition · SE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 6
- status: verified

## 2026-06-24T21:23:01Z — manifest_transition · SE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 6
- status: built

## 2026-06-24T21:23:01Z — manifest_transition · AT

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 5
- status: verified

## 2026-06-24T21:23:01Z — manifest_transition · AT

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 5
- status: built

## 2026-06-24T21:23:01Z — manifest_transition · AE

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 1
- source count: 8
- status: verified

## 2026-06-24T21:23:01Z — manifest_transition · AE

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 1
- source count: 8
- status: built

## 2026-06-24T21:23:01Z — manifest_transition · ZA

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: low
- score: 1
- source count: 9
- status: verified

## 2026-06-24T21:23:01Z — manifest_transition · ZA

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: low
- score: 1
- source count: 9
- status: built

## 2026-06-24T21:23:01Z — manifest_transition · KR

**Actor:** claude_code

Transitioned manifest status to verified.

- confidence: medium
- score: 3
- source count: 6
- status: verified

## 2026-06-24T21:23:02Z — manifest_transition · KR

**Actor:** claude_code

Transitioned manifest status to built.

- confidence: medium
- score: 3
- source count: 6
- status: built

## 2026-06-24T21:23:08Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 151214
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T21:24:00Z — decision

**Actor:** human

Authorized a full dataset-resolved re-audit and one bounded replacement-search pass, superseding the earlier decision to stop automated rediscovery.

- audit scope: GB fixture plus all 154 final-country sources
- replacement round: 2
- verification standard: dataset_resolved_v1

## 2026-06-24T21:24:00Z — discovery

**Actor:** codex

Completed the bounded round-2 replacement search pass; no high-confidence dataset-specific replacement URL was found that met the append-only standard.

- candidate additions: 0
- decision: Leave unresolved records in human_review rather than guess replacement URLs.
- page reads: {"AT": 2, "BE": 2, "CA": 2, "CH": 1, "CN": 1, "DE": 5, "FR": 1, "IE": 1, "IN": 2, "IT": 1, "JP": 4, "KR": 2, "MX": 1, "MY": 1, "PL": 2, "SE": 2}
- searches: {"AE": 1, "AT": 0, "BE": 2, "BR": 2, "CA": 2, "CH": 1, "CN": 2, "DE": 2, "FR": 1, "IE": 1, "IN": 2, "IT": 2, "JP": 2, "KR": 2, "MX": 1, "MY": 1, "PL": 1, "SE": 2, "TH": 1, "ZA": 1}

## 2026-06-24T21:24:00Z — verification

**Actor:** claude_code

Completed dataset-resolved verification for the GB calibration fixture and all final-country sources.

- confirmed dataset access: 44
- final sources: 154
- http 404: 17
- raw payloads logged: False
- reachable leads: 53
- service probes: 9
- standard: dataset_resolved_v1
- unavailable: 57

## 2026-06-24T21:24:11Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 151158
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T21:26:15Z — discovery

**Actor:** codex

Completed supplementary official-page review for dataset-specific catalogue pages used by the strict classifier.

- candidate additions: 0
- confirmed pages: ["AT-BML-001", "DE-WBL-001"]
- page reads: {"AT": 1, "DE": 1}

## 2026-06-24T21:26:31Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 151160
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T21:26:44Z — test

**Actor:** toolkit

Dataset-resolved implementation acceptance checks passed.

- candidate guards passed: 21
- contract artifacts validated: 23
- notebook check: consistent
- report check: current
- unit tests passed: 44
- unit tests skipped: 1

## 2026-06-24T21:26:44Z — handoff

**Actor:** claude_code

Completed the dataset-resolved full-source audit and rebuilt the twenty-country report.

- confirmed dataset access: 44
- human review findings: 94
- reachable leads: 53
- report: global_flood_data_readiness.md
- round2 replacements added: 0
- unavailable: 57

## 2026-06-24T21:45:49Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 193038
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T21:46:46Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 204617
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T21:47:02Z — implementation

**Actor:** claude_code

Added additive per-country portal search guides and complete website-root directories without changing source records or existing evidence tables.

- countries: 20
- country search vocabularies: 20
- included url types: ["primary", "service", "download", "verification final", "selected access", "population source"]
- preserved source records: 154
- website root entries: 155

## 2026-06-24T21:47:02Z — test

**Actor:** toolkit

Portal-guide acceptance checks passed.

- candidate guards passed: 21
- contract artifacts validated: 23
- report check: current
- source ids preserved: 154
- unit tests passed: 47
- unit tests skipped: 1

## 2026-06-24T21:47:11Z — decision

**Actor:** claude_code

Corrected the portal-directory aggregate: the final report contains 170 country-scoped website-root entries, not 155.

- previous logged value: 155
- reason: Final count includes verification redirects, selected access roots, and population-source roots.
- website root entries: 170

## 2026-06-24T21:52:42Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 212406
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T21:53:04Z — implementation

**Actor:** claude_code

Added concise English glosses for native-language portal search terms in every ranked country while preserving the original terms and all existing report content.

- contract artifacts validated: 23
- countries with native term guides: 20
- report check: current
- unit tests passed: 49
- unit tests skipped: 1

## 2026-06-24T22:01:03Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 229620
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T22:01:45Z — build

**Actor:** claude_code

Built the deterministic Markdown readiness report.

- bytes: 229620
- country count: 20
- output: global_flood_data_readiness.md

## 2026-06-24T22:02:41Z — decision

**Actor:** claude_code

Report redesigned from a scored ranking into an actionable workbook (presentation-only; build_doc.py). Dropped the subjective 1-5 composite score and the per-country subscores table everywhere; removed the 'Scoring method' section and reframed methodology step 3 as 'Assessment' (six factors as evaluation lenses, no grade). Replaced 'Executive ranking' with a factual 'Country overview' table (per-hazard-family confirmed/unconfirmed/none, confirmed-source count, leads, needs-review). Added a 'How to use this report' guide (three source tiers, Access column, portal search guide, plus a six-factor source-evaluation checklist). Added per-country 'What we have' snapshot and a derived 'What comes next' action list (confirm hazard gaps, work leads, resolve broken sources, extend pilots, verify licensing). Kept confidence as a completeness caveat. Score/subscores remain in the JSON artifacts for provenance, just unrendered. Build, --check, validate_contract (23 artifacts), and ruff all pass.

- added: ["how_to_use", "country_overview_factual", "what_we_have", "what_comes_next"]
- kept in data: ["score", "subscores", "confidence"]
- removed: ["composite_score", "subscores_table", "scoring_method_section"]

## 2026-06-25T15:08:53Z — verification · FR

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 63524
- content type: text/html
- final url: https://www.georisques.gouv.fr/donnees/bases-de-donnees
- head status: 200
- http status: 200
- range honored: False

## 2026-06-25T15:08:57Z — verification · MY

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 15598
- content type: text/html
- final url: https://publicinfobanjir.water.gov.my/
- head status: 200
- http status: 206
- range honored: True

## 2026-06-25T15:09:45Z — verification · FR

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 592
- content type: application/json
- final url: https://www.georisques.gouv.fr/api/v1/gaspar/azi?rayon=1000&latlon=2.3522,48.8566&page=1&page_size=1
- head status: 200
- http status: 200
- range honored: False

## 2026-06-25T15:09:47Z — verification · FR

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 103
- content type: application/json
- final url: https://georisques.gouv.fr/api/v1/zonage_inondation?code_insee=75056
- head status: 404
- http status: 404
- range honored: False

## 2026-06-25T15:09:48Z — verification · FR

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 592
- content type: application/json
- final url: https://www.georisques.gouv.fr/api/v1/gaspar/azi?code_insee=75056
- head status: 200
- http status: 200
- range honored: False

## 2026-06-25T15:09:51Z — verification · MY

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 57962
- content type: text/html
- final url: https://publicinfobanjir.water.gov.my/arcgis/rest/services?f=json
- head status: 404
- http status: 404
- range honored: False

## 2026-06-25T15:09:53Z — verification · MY

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 56975
- content type: application/json
- final url: https://publicinfobanjir.water.gov.my/wp-json/
- head status: 200
- http status: 206
- range honored: True

## 2026-06-25T15:09:55Z — verification · MY

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 57962
- content type: text/html
- final url: https://publicinfobanjir.water.gov.my/hujan/data/hujan_table.php
- head status: 404
- http status: 404
- range honored: False

## 2026-06-25T15:12:03Z — verification · TH

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 3123
- content type: text/html
- final url: https://www.thaiwater.net/
- head status: 200
- http status: 200
- range honored: False

## 2026-06-25T15:12:06Z — verification · TH

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 34
- content type: text/plain
- final url: https://api-v3.thaiwater.net/api/v1/thaiwater30/provinces
- head status: 404
- http status: 404
- range honored: False

## 2026-06-25T15:12:07Z — verification · TH

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 3123
- content type: text/html
- final url: https://www.thaiwater.net/api/v1/flood
- head status: 200
- http status: 200
- range honored: False

## 2026-06-25T15:12:10Z — verification · KR

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 1410
- content type: text/html
- final url: https://www.safemap.go.kr/
- head status: 400
- http status: 200
- range honored: False

## 2026-06-25T15:12:11Z — verification · KR

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 130
- content type: application/json
- final url: https://www.safemap.go.kr/openApiService/data/getDisasterInfoData.do
- head status: 400
- http status: 200
- range honored: False

## 2026-06-25T15:12:14Z — verification · KR

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 17111
- content type: text/html
- final url: https://www.safemap.go.kr/main/smap.do
- head status: 400
- http status: 200
- range honored: False

## 2026-06-25T15:12:17Z — verification · MX

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 371
- content type: text/html
- final url: https://www.gob.mx/conagua
- head status: 200
- http status: 206
- range honored: True

## 2026-06-25T15:12:19Z — verification · MX

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 371
- content type: text/html
- final url: https://www.gob.mx/conagua
- head status: 200
- http status: 206
- range honored: True

## 2026-06-25T15:12:19Z — verification · MX

**Actor:** claude_code

Ran a bounded URL check.

- bytes: 0
- content type: None
- final url: None
- head status: None
- http status: None
- range honored: None

# Codex: discovery pass

This repository implements contract version `1.0.0`.

- Produce unverified candidate records only.
- Each country's candidate set must cover every applicable flood-hazard family
  in `config/countries.json` -> `hazard_families_required` (fluvial, coastal,
  surface_water). Where a family is physically inapplicable (e.g. coastal for a
  landlocked state), state the explicit N/A in `fragmentation_summary`; never
  drop a required family silently.
- Never populate verification, `last_update`, score, confidence, or subscores.
- Never generate `global_flood_data_readiness.md`.
- Use the budgets in `config/countries.json`.
- Raw service payloads may only be read by `tools/validate_url.py` and
  `tools/probe_capabilities.py`.
- Log searches, page-read counts, probes, candidate additions, decisions, and
  handoffs with `python3 tools/lab_notebook.py record`. Never log raw payloads.
- Candidate records are append-only. In round 2, append only findings-targeted
  replacements with a new ID, `provenance.round: 2`, and `supersedes_id`.
- Apply changes with `tools/apply_delta.py --actor codex` and transition a
  completed discovery with `tools/update_manifest.py --actor codex`.
- After creating a new country file, freeze its candidate fingerprints with
  `tools/candidate_guard.py data/<ISO2>.json --actor codex --sync`.
- GB is the stage-gated fixture. Do not start the twenty final countries until
  the GB verification pilot and human review are complete.

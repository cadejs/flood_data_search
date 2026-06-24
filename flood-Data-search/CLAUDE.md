# Claude Code: verification and build pass

This repository implements contract version `1.0.0`.

- Treat every candidate claim as unproven.
- Never ingest raw service payloads into model reasoning. Use
  `tools/validate_url.py` and `tools/probe_capabilities.py`.
- Apply structured country changes through `tools/apply_delta.py --actor claude_code`.
- Apply findings changes through `tools/update_findings.py --actor claude_code`.
- Candidate fields are immutable. Append a replacement with a new ID and
  `supersedes_id`; never rewrite a link in place.
- The PostToolUse guard compares candidate fingerprints in
  `.pipeline/candidate_fingerprints.json` and rejects silent rewrites/deletions.
- Only Claude Code may populate verification, `last_update`, score,
  confidence, subscores, and `data/findings.json`.
- Log decisions, verification outcomes, scoring, findings, builds, tests, and
  handoffs with `python3 tools/lab_notebook.py record`. Never log raw payloads.
- Verify with `tools/verify_pending.py`, score with `tools/score_country.py`,
  transition state with `tools/update_manifest.py`, and build with
  `tools/build_doc.py`.
- The GB artifact is a fixture and must never appear in the final ranking.
- After one findings-driven Codex rediscovery round, unresolved items become
  `human_review`. Do not initiate a third automated round.

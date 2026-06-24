# Flood Data Readiness Pipeline

A two-pass producer/consumer workflow:

1. Codex discovers authoritative candidate sources and writes unverified
   `data/<ISO2>.json` records.
2. Claude Code verifies those records using the dataset-resolved standard,
   scores each country from confirmed evidence, and deterministically builds
   the Markdown report.

`verified` means more than HTTP reachability: the authoritative flood dataset
must be identifiable and usable through a confirmed service, API, download,
interactive viewer, map document, or dataset-specific page. Generic portals,
catalogue searches, agency homepages, restricted/request-only paths, and
ambiguous products remain failed investigation leads and do not improve scores.

Each country report also includes an additive portal-search guide: all
configured local-language search phrases, every distinct website root referenced
by source, verification, and population links, and the exact dataset names to
try on each portal. Native-language phrases include concise English glosses so
reviewers know what they mean while still pasting the original wording into the
portal. Full source URLs and evidence tables remain unchanged.

The frozen contract is `tools/schema.json` at version `1.0.0`. The repository
uses only the Python standard library.

`LAB_NOTEBOOK.md` is the shared human-readable audit trail. Its append-only
structured source is `logs/lab_notebook.jsonl`; pipeline write commands record
their own events, while research decisions and search-budget usage should be
recorded with `tools/lab_notebook.py record`.

## Current stage

The GB fixture and all twenty final countries have completed the
dataset-resolved audit. GB remains excluded from the final ranking. Unresolved
material sources are retained as structured `human_review` findings.

## Commands

```sh
python3 -m unittest discover -s tests -v
python3 tools/validate_contract.py data
python3 tools/lab_notebook.py check
python3 tools/candidate_guard.py data/GB.json
python3 tools/prepare_strict_audits.py data/GB.json --output /tmp/GB-audits.json
python3 tools/verify_pending.py data/GB.json --audit /tmp/GB-audits.json \
  --reverify --delta-output /tmp/GB-verification-delta.json \
  --actor claude_code
python3 tools/apply_delta.py --actor claude_code --country data/GB.json \
  --delta /tmp/GB-verification-delta.json
python3 tools/score_country.py data/GB.json --from-evidence \
  --write --actor claude_code
python3 tools/update_manifest.py --country data/GB.json \
  --status verified --actor claude_code
```

`tools/build_doc.py` is strict by default: it will not build until every final
country exists and has manifest status `built`.

The same delta workflow re-audits terminal records without rewriting immutable
candidate fields.

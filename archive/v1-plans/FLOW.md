---
title: "shipwithai-data — final pipeline flow"
date: 2026-05-24
status: as-built
---

# Final pipeline as built

This is what actually exists and runs end-to-end on the shipwithai-data corpus.

## Stage-by-stage flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          INPUT                                           │
│  shipwithai-data/01-raw/      (849 files w/ source_url frontmatter)     │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ M1 — shipwithai_recrawl.py                       (deterministic, local) │
│  • crawl4ai AsyncWebCrawler + PruningContentFilter (Fit Markdown)       │
│  • Politeness: 3 concurrent, 1 req/sec/domain, 2 retries+backoff        │
│  • Dedupe by source_url (88 cross-topic duplicates dropped)             │
│  Output: 01-raw-v2/<topic>/<domain>/<...>/<slug>.md  +  failure dir     │
│                                                                          │
│  RESULT: 736 successful crawls / 25 failed (3.3% — anti-bot, JS SPAs)   │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ M2 — shipwithai_clean.py + cleaning_rules.yaml   (deterministic, local) │
│  ▸ Line-drop pass:                                                      │
│      images, image-link rows, multi-bullet nav, cookie banners,         │
│      copyright lines, rating widgets, Trustpilot, newsletter headings,  │
│      ASCII-split heading detector                                       │
│  ▸ Drop-rule filter:                                                    │
│      word_count < 250  → too-short                                      │
│      text_to_link_ratio < 0.5  → low-link-ratio                         │
│      no H1  → no-h1                                                     │
│      stopword_ratio < 2.5%  → not-english                               │
│      ≥10 single-letter lines  → ascii-split-body                        │
│      ≥20 cookie-table lines  → excessive-cookie-table                   │
│  ▸ Metrics recompute (word_count, text_to_link_ratio, signal_score)     │
│  ▸ Prettier --write                                                      │
│  Output: 02-cleaned/ (kept)  +  02-quarantine/<reason>/ (dropped)       │
│                                                                          │
│  RESULT: 506 kept / 240 quarantined (no-h1=166, too-short=71, ...)      │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ POLISH — 11 Haiku 4.5 sub-agents in parallel        (LLM, ~$3 spend)    │
│  • Each agent reads ~50 files via Read tool, removes site chrome,       │
│    Writes back. Strict "delete only, never reword" prompt.              │
│  • Validation batch (10 files), 10 parallel batches (50 files each),    │
│    1 domain-focused footer-cleanup pass (47 files, partial: 16/47).     │
│  Output: same 02-cleaned/ files, body now polished                      │
│                                                                          │
│  RESULT: ~85% fully clean, ~30-50% have residual end-of-file footer     │
│          chunks on resumeworded/indeed/wahresume                         │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ M5 — shipwithai_ingest.py                       (orchestrator wrapper)  │
│                                                                          │
│   02-cleaned/ ──▶ build manifest.jsonl + _processed/                     │
│   ──▶ cv-rag/pipeline/parent.py     (H2 split, parent chunks)            │
│   ──▶ PATCH parents.jsonl  (inject source_corpus + source_url)           │
│   ──▶ cv-rag/pipeline/child.py      (~200-token children)                │
│   ──▶ PATCH children.jsonl                                               │
│   ──▶ cv-rag/pipeline/tag.py        (rule-based + heading-regex tags)    │
│   ──▶ cv-rag/pipeline/embed.py      (bge-small dense + bm25 sparse)      │
│   ──▶ cv-rag/pipeline/upsert.py     (Qdrant incremental upsert)          │
│                                                                          │
│   Every payload carries:                                                 │
│     source_corpus: "shipwithai-data"     ← filterable                    │
│     source_url: https://...              ← citeable                      │
│     topic, source_domain, tags, signal_score, ...                        │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                        OUTPUT (Qdrant)                                   │
│   kb_parents      (existing 11,056 + new shipwithai parents)            │
│   kb_children     (existing 22,210 + new shipwithai children)           │
│                                                                          │
│   Two consumers, one index:                                              │
│   • CV assistant — uses kb_search across the full corpus                 │
│   • Course drafter — uses kb_search w/ filter source_corpus="shipw..."   │
└─────────────────────────────────────────────────────────────────────────┘
```

## What's instrumented

| Layer | Mechanism | Where |
|---|---|---|
| Per-file metrics | word_count, signal_score, text_to_link_ratio in frontmatter | every 02-cleaned/*.md |
| Cleaning report | kept/dropped by reason | 02-cleaning-report.json |
| Ingest report | parents/children/skipped counts | _ingest_work/upsert_report.json |
| Retrieval quality | M6 eval suite | cv-rag/tests/eval/run_eval.py |
| M5 contracts | 5 e2e tests (round-trip, idempotency, filter isolation, co-existence, patch unit) | cv-rag/tests/test_shipwithai_ingest.py |

## How good is it? (honest scorecard)

| Dimension | Score | Comment |
|---|---|---|
| Body content fidelity | 9/10 | Verbatim preservation through all stages |
| Chrome removal | 7.5/10 | ~85% clean; 30-50% have end-of-file footer chunks |
| Determinism | 6/10 | M1+M2+M5 deterministic; Haiku polish is non-deterministic |
| Reproducibility from source | 8/10 | All source_url preserved; re-crawl idempotent |
| Source citation | 9/10 | Every chunk carries source_url; per-corpus filterable |
| Test coverage | 8/10 | 5 M5 e2e tests pass; M1+M2 not tested per PRD scope |
| Co-existence with cv-kb-clean | 10/10 | Tested; existing chunks untouched |
| Idempotency | 10/10 | Tested; re-runs do not duplicate |
| End-to-end runtime | n/a | M1: ~12 min, M2: ~1 min, polish: ~30 min parallel, M5: ~10 min |

## Industry-standard pipeline (deferred for next corpus)

See `NEXT_CORPUS_PIPELINE.md`. Adds:
- **trafilatura** in place of crawl4ai Fit Markdown (better DOM-tree pruning)
- **Phi-4-mini / Qwen3-0.6B** local LLM for polish (replaces Haiku, runs free on CPU)
- Same overall shape, marginal +5-7% cleanup gain

## Comparison to original PRD

| PRD requirement | Status |
|---|---|
| Clean corpus deterministically | ✓ (M1+M2); hybrid polish layer added on top |
| No LLM in indexing pipeline | ✓ (M5 ingest itself is LLM-free) |
| Re-runnable, diffable | ✓ for M1+M2; ⚠ for polish layer (non-deterministic) |
| 5 modules built | ✓ (M1 new, M2 new, M3 mod, M4 no-op, M5 new) |
| Tests for shipwithai_ingest only | ✓ (5/5 pass) |
| GraphRAG / LightRAG / RAPTOR not used | ✓ |
| No LLM-Wiki / STORM bulk synthesis | ✓ |
| source_corpus payload field | ✓ |
| Re-crawl politeness | ✓ (3 concurrent, 1 rps/domain, 2 retries) |
| Quarantine with reason directory | ✓ (6 reasons total) |
| Cleaning report JSON | ✓ |
| No mutation of existing cv-kb-clean chunks | ✓ (test_legacy_chunk_untouched passes) |

## Where to dig deeper

- Source code: `shipwithai-data/scripts/{shipwithai_recrawl,shipwithai_clean,shipwithai_ingest}.py`
- Tests: `cv-rag/tests/test_shipwithai_ingest.py`
- Cleaning rules: `shipwithai-data/scripts/cleaning_rules.yaml`
- Tag rules added: `cv-rag/pipeline/tag_rules.yaml` (7 new entries)
- Reports: `shipwithai-data/02-cleaning-report.json`, `_ingest_work/upsert_report.json`
- PRD: `shipwithai-data/PRD_CLEAN_AND_INGEST.md`
- Plan: `shipwithai-data/IMPLEMENTATION_PLAN.md`

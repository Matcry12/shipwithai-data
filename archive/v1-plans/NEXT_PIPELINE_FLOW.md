---
title: "Proposed next-corpus pipeline — visual flow"
date: 2026-05-24
status: design / not implemented
companion: NEXT_CORPUS_PIPELINE.md
---

# Proposed pipeline (trafilatura + small LLM polish)

```
┌─────────────────────────────────────────────────────────────────────────┐
│                          INPUT                                           │
│   URL list with topic + career_level metadata                            │
│   (frontmatter or JSON manifest)                                         │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STAGE 1 — Fetch                                  (existing: crawl4ai)    │
│  • crawl4ai AsyncWebCrawler, headless Chrome                             │
│  • Politeness: 3 concurrent, 1 rps/domain, 2 retries                     │
│  • Output: raw HTML (or pre-extracted markdown if site allows)           │
│                                                                          │
│  WHY KEEP: handles JS-rendered SPAs, anti-bot, rate limiting better      │
│            than pure HTTP libraries. Already proven on shipwithai.       │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │  raw HTML
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STAGE 2 — Content extraction              (NEW: trafilatura)             │
│  • pip install trafilatura                                               │
│  • trafilatura.extract(html, output_format="markdown",                   │
│                        include_comments=False, include_tables=True)      │
│  • DOM-tree pruning algorithm — distinguishes article body from chrome   │
│  • Auto-fallback to readability-lxml if extraction too short             │
│                                                                          │
│  WHY: Used in production by HuggingFace, Common Crawl, IBM. Strips      │
│       footers/ads/nav at the HTML structural level — much better than   │
│       trying to remove chrome from already-converted markdown.           │
│                                                                          │
│  EXPECTED: 90-95% chrome-clean output. 5-10% better than Fit Markdown.  │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │  clean markdown body
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STAGE 3 — Text normalization              (existing pattern, lighter)    │
│  • markdowncleaner OR small custom regex pass                            │
│  • Drop:                                                                 │
│      - Lines with > N consecutive blanks                                 │
│      - Smart-quote → ASCII normalization                                 │
│      - Zero-width chars, nbsp                                            │
│      - Trailing whitespace                                               │
│  • NO drop-rule filter at this stage (defer to drop after polish)        │
│                                                                          │
│  WHY: trafilatura already removed most chrome, so this is just hygiene. │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │  normalized markdown
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STAGE 4 — Chrome polish via local small LLM   (NEW: Phi-4-mini local)   │
│                                                                          │
│  Model: microsoft/Phi-4-mini (3.8B, runs CPU via llama.cpp/ollama)      │
│  Alternative: Qwen/Qwen3-0.6B (faster but lower quality)                 │
│                                                                          │
│  STRICT CONTRACT — preserving schema (not destructive!):                 │
│                                                                          │
│    prompt = "Output the article markdown VERBATIM. Delete only site     │
│              chrome (cookie banners, footer nav, author bios, related-  │
│              article lists). Do NOT reword/summarize/restructure body." │
│                                                                          │
│    response_schema = {"cleaned_markdown": str}   ← single field         │
│                                                                          │
│  ⚠  WRONG (do NOT do this — destructive summarization):                 │
│       schema = {title, summary, body, key_points}                       │
│       This is LLM-Wiki/STORM and was rejected at project start.         │
│                                                                          │
│  ⚙  IMPLEMENTATION:                                                      │
│     - HuggingFace `outlines` for schema enforcement                      │
│     - Batch ~10 files/run with seeded sampling for determinism-ish      │
│     - Failure mode: if model returns < 50% of input length, REJECT and  │
│       keep the pre-polish markdown (safety net against truncation)      │
│                                                                          │
│  EXPECTED: ~95-97% clean output, body verbatim                          │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │  polished markdown
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STAGE 5 — Frontmatter + format                  (existing pattern)       │
│  • Attach frontmatter (source_url, topic, career_level, slug,            │
│    source_domain, word_count, signal_score, cleaner_version, language)  │
│  • Prettier --write for consistent markdown structure                    │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│ STAGE 6 — Quality gate (drop-rule filter)        (existing pattern)      │
│  • word_count < 250 → quarantine                                         │
│  • text_to_link_ratio < 0.5 → quarantine                                 │
│  • No H1 → quarantine (with title-synthesis fallback)                    │
│  • language != en → quarantine                                           │
│  • Emit 02-cleaning-report.json                                          │
│                                                                          │
│  WHY at this stage: only drop after the model has had a chance to       │
│  rescue marginal files. Some pages have a short body + lots of chrome — │
│  trafilatura + Phi-4-mini can recover them; raw rule-based filtering    │
│  would have dropped them.                                                │
└──────────────────────────────────┬──────────────────────────────────────┘
                                   │
                                   ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                       OUTPUT                                             │
│  02-cleaned/<topic>/<domain>/<slug>.md                                   │
│  02-quarantine/<reason>/...                                              │
│  Ready for the same cv-rag ingest orchestrator (no change needed there)  │
└─────────────────────────────────────────────────────────────────────────┘
```

## How good would it be? (estimated)

| Dimension | Current pipeline | Proposed pipeline | Delta |
|---|---|---|---|
| Body fidelity | 9/10 | 9/10 | even (if chrome-remover schema is used; -3 if destructive schema) |
| Chrome removal | 7.5/10 | 9/10 | +1.5 |
| Determinism | 6/10 | 6/10 | even (still LLM-based polish, just local) |
| Cost | ~$3 (Haiku) | $0 (local) | +$3 saved |
| Runtime | ~45 min | ~1.5-3 hr (CPU inference) | -1h+ |
| Setup complexity | low | medium (model download, outlines lib) | -1 |
| Reproducibility | medium | medium-high (seeded local inference) | +0.5 |
| Network dependency | yes (Haiku API) | no | +1 |

**Net: +1 to +2 quality points, no cost, but +1 hour runtime and one-time setup overhead.**

## Honest comparison vs current

| Decision factor | Verdict |
|---|---|
| Is the proposed pipeline better in theory? | Yes — trafilatura > crawl4ai Fit MD for chrome detection |
| Is it worth redoing the current 506 files? | No — marginal gain doesn't justify rework |
| Is it the right pipeline for the next corpus? | **Yes** — adopt for any future bulk-crawl project |
| Critical caveat | Stage 4 schema MUST be single-field "cleaned_markdown", NOT a `{summary, body, points}` template. The latter is destructive LLM-Wiki. |

## Risks of this pipeline

1. **Phi-4-mini quality on long articles.** 4K context limit. Articles > 3000 words may need chunked processing — re-stitching risks line ordering errors.
2. **Local CPU inference is slow.** ~5-15 sec/file vs Haiku's ~3-5 sec/file via API. 506 files would take ~1-2 hours.
3. **Schema enforcement libraries are evolving.** `outlines` and `guidance` have rough edges; HuggingFace structured outputs API is newer than typical SDKs.
4. **Trafilatura sometimes drops legitimate content.** Aggressive DOM-pruning can mistake a column layout for a sidebar. Need a safety net.
5. **Determinism is improved but not perfect.** Seeded sampling on CPU produces consistent output per (model, prompt, seed, hardware), but model updates would still cause drift.

## Recommended adoption path (when applicable)

1. **Pilot:** run the pipeline on 50 URLs from a new domain (not shipwithai). Compare output to crawl4ai+Haiku baseline.
2. **Bench:** measure precision@3 on a retrieval eval — does the proposed pipeline produce a higher-quality index?
3. **Adopt:** if bench shows ≥5% improvement on M6 eval, swap in as the default for next corpus.
4. **Fallback:** keep the current crawl4ai+Haiku path as the safety net for sites trafilatura mangles.

## Bottom line

**Architecturally cleaner, marginally better, free.** Use it for the next corpus, not this one.

---
status: idea-deferred
title: "Production-grade cleaning pipeline for the next corpus"
date: 2026-05-24
context: |
  This idea surfaced during the shipwithai-data clean+ingest project after we'd
  already produced 02-cleaned/. Marginal gain over current state didn't justify
  rework, but it's the right architecture for the *next* corpus.
---

# Next-corpus cleaning pipeline (deferred)

Industry-standard pipeline for HTML → clean RAG-ready markdown. Free, all-local,
no paid APIs.

## Stack

| Stage | Tool | Why |
|---|---|---|
| 1. Crawl | crawl4ai | Already have it; handles JS, anti-bot, rate limits |
| 2. Boilerplate removal | **trafilatura** | Used by HuggingFace datasets, Common Crawl, IBM, Microsoft Research. Strips nav/ads/footers via DOM-tree pruning with readability-lxml fallback. Better than crawl4ai Fit Markdown for chrome detection. |
| 3. Text normalization | markdowncleaner + small regex pass | Fix encoding, dedup lines, drop short noise. Deterministic. |
| 4. Semantic polish | **Phi-4-mini** or **Qwen3-0.6B** via HuggingFace | Local small LLM. Run as a **chrome remover only** — preserves article body verbatim. |
| 5. Final format | Prettier | Normalize markdown structure |

## Critical design rule for Stage 4

**The LLM is a chrome remover, NOT a content structurer.**

Wrong (destructive — what NOT to do):
```python
# This is summarization. Loses fidelity. Forbidden.
model.generate(prompt, response_schema={
  "title": str, "summary": str, "body": str, "key_points": List[str]
})
```

Right (preserving — chrome removal only):
```python
# Single-field schema — model is forced to only delete, not rewrite.
model.generate(
    prompt="Output the article markdown VERBATIM. Delete only site chrome "
           "(cookie banners, footer nav, author bios, related-article lists). "
           "Do NOT reword, summarize, or restructure body content.",
    response_schema={"cleaned_markdown": str},
)
```

Why this matters: course drafting needs **direct quotability** with `source_url` citation.
If Phi-4-mini rewrites the body, you can no longer say "according to the original at
example.com" because the quote no longer exists at that URL.

This is the same rule we applied to the Haiku polish pass in the current project.

## Pipeline diagram

```
Raw URL
  ↓ crawl4ai (fetch HTML)
  ↓ trafilatura (DOM-pruned content extraction, readability fallback)
  ↓ markdowncleaner + regex (encoding fix, line dedup)
  ↓ Phi-4-mini / Qwen3-0.6B (chrome-remover schema, body preserved verbatim)
  ↓ Prettier (final format)
Clean .md with frontmatter (source_url, topic, career_level, signal_score)
```

## Cost / runtime

- All local; CPU-friendly inference for Phi-4-mini (~2-3 sec/file on modern CPU)
- Free on HuggingFace Spaces CPU tier for batch runs
- Zero API spend

## Why we are NOT switching to this for shipwithai-data

| Aspect | Current state | This pipeline | Marginal gain |
|---|---|---|---|
| Cleaning quality | ~85% clean (Haiku polish hybrid) | ~90-92% (trafilatura+Phi-4) | +5-7% |
| Body fidelity | 100% preserved | Risk of small-model errors | -5-10% |
| Time | Already done | 4-8 more hours | — |
| Determinism | Hybrid (Haiku) | Hybrid (Phi-4) | Same |

Marginal cleanup gain doesn't justify rework + fidelity risk.

## When to revisit

- Next crawled corpus (e.g. expanding past CV-writing into broader career content)
- A reclean of shipwithai-data if downstream course quality reveals issues
- Switching to a fully air-gapped / no-API workflow

## Open implementation questions (for next time)

- Which Phi-4-mini quantization? Q4 GGUF via llama.cpp keeps it CPU-friendly.
- Structured output enforcement: HF's `outlines` library or `guidance`?
- How to handle trafilatura's output preserving markdown structure vs. plain text — likely run trafilatura with `output_format="markdown"`.
- Batch size for parallel CPU inference on free Spaces tier.

## Source

Idea proposed by user 2026-05-24 during shipwithai-data clean+ingest project.
Deferred to next corpus to avoid throwing away ~85%-clean existing work.

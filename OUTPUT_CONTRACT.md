---
title: "Output contract — URL → structured JSON (Firecrawl-exact)"
date: 2026-05-25
status: draft / pending final sign-off
purpose: defines the single artifact the rebuilt pipeline produces per URL
---

# Output contract

**One URL in → one JSON object out.** Firecrawl-exact shape, enriched metadata.
This is the source of truth for everything downstream (chunk → tag → embed → ingest).

## The object

```jsonc
{
  // ─── the LLM-ready payload ───
  "markdown": "# Career Change to Software Engineer\n\nClean body, no chrome...",

  // ─── Firecrawl-style metadata, enriched ───
  "metadata": {
    // provenance — who / where / when
    "source_url":    "https://www.indeed.com/career-advice/...",
    "source_domain": "indeed.com",
    "fetched_at":    "2026-05-25T10:00:00Z",   // ISO-8601 UTC
    "http_status":   200,
    "extractor":     "trafilatura-1.12",        // engine that produced markdown

    // content identity
    "title":         "Career Change to Software Engineer",
    "description":   "...",                      // meta description → fallback og:description
    "language":      "en",
    "word_count":    1240,
    "content_hash":  "sha256:abcd…",             // over markdown body ONLY → dedupe + change-detect

    // SEO / authorship
    "og_title":       "...",
    "author":         null,                      // string | null
    "published_date": null,                      // ISO date string | null
    "reading_time":   6,                          // minutes, ceil(word_count / 200)

    // quality signal — computed, NEVER from an LLM
    "signal_score":       0.82,                   // 0–1 keep-worthiness
    "text_to_link_ratio": 0.91,
    "extractor_version":  "pipeline-2.0.0"
  },

  // ─── outbound links (Firecrawl returns these) ───
  "links": ["https://...", "https://..."],

  // ─── quality-gate verdict (our addition) ───
  "status":      "kept",    // "kept" | "quarantined"
  "drop_reason": null       // null when kept; e.g. "too-short" when quarantined
}
```

## Field reference

| Field | Type | Source | Notes |
|---|---|---|---|
| `markdown` | string | extractor | Clean article body. No nav/cookie/footer/related-articles. Starts with the H1. |
| `metadata.source_url` | string | input | Canonical URL fetched. |
| `metadata.source_domain` | string | derived | Registrable domain of `source_url`. |
| `metadata.fetched_at` | string | runtime | ISO-8601 UTC timestamp of fetch. |
| `metadata.http_status` | int | fetch | 200 on success. |
| `metadata.extractor` | string | runtime | Engine + version that produced `markdown`. |
| `metadata.title` | string | extractor | `<h1>` / `<title>` / og:title, in that priority. |
| `metadata.description` | string\|null | extractor | meta description → og:description fallback. |
| `metadata.language` | string | detector | ISO 639-1 (`en`). |
| `metadata.word_count` | int | derived | Whitespace-split count of `markdown`. |
| `metadata.content_hash` | string | derived | `sha256:` over `markdown` body only. |
| `metadata.og_title` | string\|null | extractor | OpenGraph title if present. |
| `metadata.author` | string\|null | extractor | null if not found. |
| `metadata.published_date` | string\|null | extractor | ISO date; null if not found. |
| `metadata.reading_time` | int | derived | `ceil(word_count / 200)` minutes. |
| `metadata.signal_score` | float | computed | 0–1 keep-worthiness heuristic. |
| `metadata.text_to_link_ratio` | float | computed | body text chars / link markup chars. |
| `metadata.extractor_version` | string | runtime | Version of THIS pipeline. |
| `links` | string[] | extractor | Outbound links found in the article body. |
| `status` | string | quality gate | `"kept"` or `"quarantined"`. |
| `drop_reason` | string\|null | quality gate | null when kept. |

## Design decisions (baked in)

1. **`null` for missing optionals, never omit the key.** Stable schema — every
   object has every field. Trivial to load into a dataframe; no `KeyError`.

2. **`content_hash` over the markdown body only**, not the whole object. A
   re-crawl that only changes a footer date or timestamp must NOT look like new
   content. This hash drives dedupe and change-detection.

3. **`status` + `drop_reason` live *inside* the object**, not encoded by which
   folder the file lands in. The quality gate **annotates, it does not silently
   drop.** Quarantined items stay fully inspectable.

## Resolved (recommended defaults — revisit if needed)

4. **One output directory, filtered by `status`.** Both kept and quarantined
   objects land in `output/`. No separate `quarantine/` tree. Consumers filter
   on `status == "kept"`. Rationale: matches "annotate, don't drop"; nothing
   disappears from view.

5. **Filename = URL-path slug + short hash suffix.**
   e.g. `career-change-to-software-engineer-a1b2.json`
   Human-readable AND collision-free (hash from full `source_url`). The hash
   suffix disambiguates same-slug pages from different domains/paths.

## Drop reasons (quality gate vocabulary)

`too-short` · `low-link-ratio` · `no-h1` · `not-english` ·
`ascii-split-body` · `excessive-cookie-table` · `fetch-failed`

## What this contract intentionally excludes

- **No `{summary, key_points, ...}` LLM-synthesized fields.** `markdown` is the
  body verbatim minus chrome. No summarization, no restructuring. (Rejected at
  project start — that path is LLM-Wiki / STORM, destructive.)
- **No raw HTML in the object.** If we ever need it for debugging, it goes to a
  sidecar, not this object.

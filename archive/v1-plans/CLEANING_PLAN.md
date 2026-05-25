# 02-cleaned Data Cleaning Plan

**Goal:** Transform 773 noisy markdown files into clean, LLM-ready content.  
**Input:** `02-cleaned/<topic>/<domain>/<file>.md`  
**Output:** `02-cleaned-v2/<topic>/<domain>/<file>.md`  
**Do not touch:** `01-raw/` (preserve original), `02-cleaned/` (keep as backup)

---

## What "LLM-ready" means

Each output file should contain only content a human would actually read:
- Clear headings and prose paragraphs
- Bullet lists with real advice
- Code/template examples where relevant
- Minimal 3-field header for context (title, topic, source_url)

No website chrome, no marketing, no images, no nav menus.

---

## Output format (each file)

```markdown
---
title: "..."
topic: "..."
source_url: "..."
---

# Page Title

## Section Heading

Content here...
```

Strip all other frontmatter fields — `word_count`, `signal_score`, `career_level`, `tags`, etc. are pipeline metadata, not content.

---

## Noise patterns to strip

### Always remove (line-level)

| Pattern | Example |
|---|---|
| Image lines | `![alt text](https://cdn.example.com/img.png)` |
| Image-in-link lines | `[![Avatar](img-url)](link-url)` |
| GitHub badge lines | `[![Go](https://img.shields.io/badge/...)](url)` |
| Anchor-only lines | `[ ](https://site.com#section)` |
| Horizontal rule dividers | `* * *` or `---` (body, not frontmatter) |
| Emoji-only / icon-only lines | `📍 Berlin, Germany` standalone lines |
| Lines with >80% link content | `[Resume Builder](url) > [Examples](url) > [Manager](url)` |

### Always remove (block-level — strip the entire block)

| Block type | Detection |
|---|---|
| Author/reviewer attribution | Lines starting with `By `, `Reviewed by`, `Written by`, `Compiled and approved by` |
| Promoted/sponsored inserts | Lines containing `Promoted`, `Sponsored`, `Advertisement` |
| CTA blocks | Lines matching: `Sign up`, `Get started`, `Try it free`, `Learn more`, `Subscribe`, `Join now`, `Create account`, `Try for free` |
| Social share buttons | Lines with share-button emoji patterns (`👍`, `🦄`, `🔥`, `❤️`, `💡` as standalone) |
| Cookie/consent notices | Lines containing `cookie`, `GDPR`, `privacy policy`, `we use cookies` (case-insensitive) |
| Breadcrumb navigation | Lines like `Home > Blog > Article` or `[Section](url) > [Page](url)` with `>` separators |

### Strip from prose (inline cleanup)

| Pattern | Action |
|---|---|
| Inline markdown links `[text](url)` | Keep text, remove URL → `text` |
| Inline image references in text | Remove entirely |
| Trailing whitespace per line | Strip |
| 3+ consecutive blank lines | Collapse to 1 blank line |

---

## Quality filter (drop entire file if any condition is true)

| Condition | Threshold | Reason |
|---|---|---|
| Word count after cleaning | < 200 words | Too short to be useful |
| Heading count ≥ word count / 20 | e.g. 15 headings, 280 words | Skeleton/index page, no substance |
| No H1 or H2 headings | — | Unstructured dump |
| >60% of lines are list items with ≤ 5 words each | — | Pure keyword list, no context |
| File is clearly off-topic | billboards, cookie policy, error pages | Manual or keyword-based detection |

**Expected outcome:** ~600–650 files survive (from 773). The ~120–170 dropped are nav pages, stubs, and junk like `billboards.md`.

---

## Topics to exclude entirely

| Topic folder | Reason |
|---|---|
| `claude-code-workflow` | ShipWithAI product marketing, not CV content |

---

## Inline link handling — decision needed

Two options for links in body text:

**Option A — Strip URLs, keep anchor text** (recommended for LLM use)  
`[resume bullet points](https://resumeworded.com/sample-resume-bullet-points)` → `resume bullet points`  
Cleaner prose, no dead URLs polluting context.

**Option B — Keep full markdown links**  
Preserves source attribution inline. Noisier for LLM but good for human reference.

> **Decision:** Choose before running the script.

---

## Implementation steps

1. **Write `scripts/clean_v2.py`**
   - Parse and strip YAML frontmatter → keep only title, topic, source_url
   - Apply all line-level and block-level rules above
   - Apply inline link handling (per decision above)
   - Apply quality filter → write to `02-cleaned-v2/` or log to `dropped_v2.log`
   - Print summary: kept N, dropped N (by reason)

2. **Dry-run on 20 files** — spot-check output before processing all 773

3. **Run on all 773 files**

4. **Verify output**
   - Manually open 10 random files from each topic folder
   - Check: no images, no nav, no CTAs, clean headings, readable prose
   - Run word count distribution check (no file < 200 words)

5. **Done** — `02-cleaned-v2/` is the cleaned corpus, ready for any downstream use

---

## What this does NOT do

- Does **not** rewrite or summarize content — LLM does that at query time
- Does **not** change file organization (same `<topic>/<domain>/<file>` structure)
- Does **not** ingest into any system — this is just cleaning

---

## Open question for review

- Inline links: Option A (strip URLs) or Option B (keep full links)?
- Any topics to add to the exclude list beyond `claude-code-workflow`?
- Should `git-first-job` stay? (It's about getting first dev job via GitHub/portfolio — adjacent to CV writing)

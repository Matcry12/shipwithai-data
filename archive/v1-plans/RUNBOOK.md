---
title: "Corpus ingest runbook — shipping the pipeline for future crawls"
date: 2026-05-24
audience: operator (you, future self, or new teammate)
status: as-built; works today
---

# How to ship this for the next corpus

You have three options, ordered by effort:

| Option | Effort | When to use |
|---|---|---|
| **A. Copy-and-adapt this corpus** | 30 min | One-off new corpus, same domain (career content) |
| **B. Generalize the scripts** | 2-3 hr one-time + 15 min/corpus thereafter | You'll run this 3+ times |
| **C. Build the trafilatura+Phi-4 pipeline** | 4-8 hr one-time | Long-term default; better extraction quality |

---

## Option A — Copy-and-adapt (cheapest path for one more corpus)

### Step 1: Set up new corpus directory

```bash
NEW=cv-content-2026q3
mkdir -p ~/Documents/Knowledge/$NEW/{01-raw,scripts}
cd ~/Documents/Knowledge/$NEW
```

### Step 2: Drop URLs into 01-raw

Same layout as shipwithai: `01-raw/<topic>/<source_domain>/<...>/<slug>.md`
Each `.md` only needs YAML frontmatter with `source_url`:

```markdown
---
source_url: https://www.example.com/article-slug
topic: career-change
---
```

### Step 3: Copy the three scripts + rules YAML

```bash
cp ~/Documents/Knowledge/shipwithai-data/scripts/{shipwithai_recrawl,shipwithai_clean,shipwithai_ingest}.py \
   ~/Documents/Knowledge/shipwithai-data/scripts/cleaning_rules.yaml \
   ./scripts/
```

### Step 4: Adjust the `SOURCE_CORPUS_TAG` constant

In `scripts/shipwithai_ingest.py`:
```python
SOURCE_CORPUS_TAG = "cv-content-2026q3"   # ← change to new corpus slug
```

### Step 5: Run the pipeline

```bash
# Re-crawl all URLs from 01-raw frontmatter
python3 scripts/shipwithai_recrawl.py

# Clean and quality-filter
python3 scripts/shipwithai_clean.py

# (Optional) Haiku polish — see "Polish step" below
# ... spawn agents in batches ...

# Ingest into cv-rag's Qdrant
python3 scripts/shipwithai_ingest.py --upsert-mode incremental
```

### Step 6: Verify

```bash
# Filter test — confirm chunks landed with the new corpus tag
.venv/bin/python -c "
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
c = QdrantClient(host='localhost', port=6333)
flt = Filter(must=[FieldCondition(key='source_corpus', match=MatchValue(value='cv-content-2026q3'))])
print('parents:', c.count('kb_parents', count_filter=flt, exact=True).count)
print('children:', c.count('kb_children', count_filter=flt, exact=True).count)
"

# Run M6 eval to confirm no regression
.venv/bin/python ~/Documents/Knowledge/cv-rag/tests/eval/run_eval.py
```

Done.

---

## Option B — Generalize the scripts (recommended if you'll run this ≥3 times)

### What to change

1. **Move scripts to a shared location:**

   ```
   cv-rag/pipeline/corpus/
   ├── recrawl.py            (was shipwithai_recrawl.py — corpus-agnostic)
   ├── clean.py              (was shipwithai_clean.py — corpus-agnostic)
   ├── ingest.py             (was shipwithai_ingest.py — corpus-agnostic)
   ├── cleaning_rules.yaml   (shared base; override per-corpus)
   └── README.md
   ```

2. **Parameterize the source_corpus tag** — already done via CLI flag on the wrapper:

   ```bash
   python3 cv-rag/pipeline/corpus/ingest.py \
       --cleaned ~/Documents/Knowledge/<corpus>/02-cleaned \
       --source-corpus-tag <corpus> \
       --upsert-mode incremental
   ```

3. **Add a config-file driver:**

   ```yaml
   # ~/Documents/Knowledge/<corpus>/corpus.yaml
   corpus_id: cv-content-2026q3
   input_dir: ~/Documents/Knowledge/cv-content-2026q3/01-raw
   cleaning_rules: ./cleaning_rules.yaml   # or path to override
   topics: [...]                            # for tag rule lookup
   drop_overrides:
     min_word_count: 250
     min_text_to_link_ratio: 0.5
   ```

4. **Single entrypoint script:**

   ```bash
   python3 -m cv-rag.corpus run --config ~/Documents/Knowledge/<corpus>/corpus.yaml
   ```

5. **Move tag rules under cv-rag** (already there) and add new topics per corpus via additive YAML entries.

### Estimated effort

- Move/refactor: 1.5 hr
- Add config-file driver + entrypoint: 1 hr
- Test on one new corpus: 30 min
- **Total: 2.5-3 hr one-time, then ~15 min per future corpus**

---

## Option C — Build the trafilatura + Phi-4-mini pipeline

See `NEXT_PIPELINE_FLOW.md` for full design.

### Why eventually do this

- Trafilatura extracts cleaner markdown at the HTML level (no need for ~half the regex patterns in `cleaning_rules.yaml`)
- Phi-4-mini local polish replaces Haiku — free, no API key, fully reproducible with seeded sampling
- Industry-standard pipeline (HuggingFace datasets uses this)

### Implementation outline (~4-8 hr)

```bash
# 1. Add dependencies (use cv-rag venv)
.venv/bin/pip install trafilatura outlines transformers torch

# 2. Replace Stage 1+2 with trafilatura
# shipwithai_recrawl.py → cv-rag/pipeline/corpus/extract.py
#   Stage 1: crawl4ai for HTML fetch
#   Stage 2: trafilatura.extract(html, output_format="markdown")
# Output: cleaner raw markdown, fewer regex rules needed downstream

# 3. Replace Haiku polish with local Phi-4-mini via outlines
# scripts/polish.py
from outlines import models, generate
from outlines.types import json_schema

model = models.transformers("microsoft/Phi-4-mini-instruct")
schema = json_schema({
    "type": "object",
    "properties": {"cleaned_markdown": {"type": "string"}},
    "required": ["cleaned_markdown"],
})
generator = generate.json(model, schema)

# For each file:
#   prompt = f"Output the article markdown verbatim, deleting only site chrome:\n\n{body}"
#   result = generator(prompt, seed=42)   # seeded for determinism
#   write back result["cleaned_markdown"]

# 4. Keep the rest unchanged (M2 drop filter, M5 ingest)
```

### Adoption path

1. Pilot on 50 URLs from a new domain
2. Compare quality vs current pipeline (precision@3 on M6-style eval)
3. If ≥5% better, adopt as default
4. Keep current pipeline as fallback for sites trafilatura mangles

---

## The Haiku polish step (Option A or B)

This is the trickiest part to script reliably because it requires spawning
sub-agents.

### Current workflow (manual)

1. Split file list into batches of ~10-15 files (NOT 50 — context limit)
2. Spawn N Haiku sub-agents in parallel via `Agent` tool
3. Each agent uses Read + Edit to remove site chrome
4. Strict prompt: "delete only, never reword, preserve frontmatter"
5. After all complete, run Prettier once to normalize

### Pitfalls we hit

| Pitfall | Fix |
|---|---|
| Agents asked for Bash permission | Tell prompt: "you have Read+Edit, no Bash needed" |
| 50 files/batch exhausted context | Use 10-15 files/batch |
| Some agents stopped voluntarily at 10 files | Be explicit: "process all N files in this session" |
| Edit failed on non-unique `old_string` | Tell agent: "add 1-2 lines of surrounding context to make `old_string` unique" |

### What to automate next time

Wrap the agent-spawn loop in a Python script that:
1. Splits the file list into 10-file batches
2. Spawns one agent per batch in parallel
3. Waits for all to complete
4. Detects unprocessed files (via mtime + checksum)
5. Spawns recovery batches for unprocessed files

---

## Validation gates — before every ingest

Before pushing to live Qdrant:

```bash
# 1. Spot-check 3 random files for sanity
python3 -c "
import random, glob, os
os.chdir('02-cleaned')
random.seed(0)
for f in random.sample(sorted(glob.glob('**/*.md', recursive=True)), 3):
    print(f'=== {f} ===')
    print(open(f).read()[:500])
"

# 2. Confirm cleaning report sanity
python3 -c "import json; r=json.load(open('02-cleaning-report.json')); print(f'kept={r[\"kept\"]}, dropped={r[\"dropped_counts\"]}')"

# 3. Snapshot Qdrant before
curl -s http://localhost:6333/collections/kb_parents | python3 -c "import json,sys; print('pre:', json.load(sys.stdin)['result']['points_count'])"

# 4. Dry run with --skip-upsert
python3 scripts/shipwithai_ingest.py --skip-upsert

# 5. Real run
python3 scripts/shipwithai_ingest.py --upsert-mode incremental

# 6. Verify filter
.venv/bin/python -c "...filter-count code from Step 6 above..."

# 7. Eval (must pass ≥80%)
.venv/bin/python ~/Documents/Knowledge/cv-rag/tests/eval/run_eval.py
```

---

## Recovery procedures

| Failure | Recovery |
|---|---|
| `kb_search` returns garbage after ingest | Filter by `source_corpus` → delete new chunks via Qdrant API → fix → re-ingest |
| M6 eval drops below 80% | Same — delete new chunks, investigate which queries broke, fix and re-ingest |
| Re-crawl hits rate limits | Lower `CONCURRENCY` and `PER_DOMAIN_DELAY_SEC` constants in `shipwithai_recrawl.py` |
| Cleaning over-drops files | Add `--no-drop` flag (not yet implemented; would let everything through to manual review) |
| Haiku polish damages a file | Revert from `01-raw-v2/<same-path>` and skip polish for that file |

### Hard delete a corpus

If you ever need to roll back an entire corpus:

```python
from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
c = QdrantClient(host='localhost', port=6333)
flt = Filter(must=[FieldCondition(key='source_corpus', match=MatchValue(value='<corpus-id>'))])
c.delete('kb_parents', points_selector=flt)
c.delete('kb_children', points_selector=flt)
```

This works because `source_corpus` is a payload-indexed keyword field.

---

## Cost model (for budgeting future crawls)

Per 500-file corpus:

| Stage | Cost | Time |
|---|---|---|
| Re-crawl | $0 (crawl4ai local) | ~10-15 min |
| Cleaning + Prettier | $0 | ~1-2 min |
| Haiku polish (~10 batches × ~3K tokens each) | ~$3-5 | ~30 min parallel |
| Embed + upsert | $0 (fastembed local) | ~10 min |
| **Total** | **~$3-5** | **~1 hr** |

Option C (Phi-4-mini local): $0 + ~2 hr CPU time.

---

## TL;DR — fastest path forward

**For your next corpus, run Option A.** 30 minutes, you already know the pipeline.

**When you have 3+ corpora to support, do Option B.** 3-hour one-time refactor pays off forever.

**For long-term independence from API costs, do Option C.** Best done as a side project, not under deadline pressure.

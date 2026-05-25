#!/usr/bin/env python3
"""
Pipeline V2 — Stage 4: LLM enrichment (engine-agnostic).

Flow:  04-structured (kept) ──prepare──▶ enrich_inbox/
       enrich_inbox/ ──(gemma OR spawned Haiku)──▶ enrich_out/
       enrich_out/ ──merge+validate──▶ 05-enriched/

The LLM emits ONLY the metadata schema (tldr, entities, core_question, doc_type,
key_topics). It never has write-access to the body, so body integrity is
guaranteed by construction. A faithfulness check rejects enrichment whose
entities.primary / key_topics do not actually occur in the body.

Engines:
  • gemma4:e4b via Ollama  — local, ~40s/doc. Good for pilot / small / offline.
  • spawned Haiku          — Claude orchestrates agents that read inbox/*.json
                             and write enrich_out/*.json. Offloads the heavy
                             602-doc run from local hardware. (No API key.)

Modes:
    prepare   build enrich_inbox/ from kept structured docs
    ollama    enrich inbox via local gemma → enrich_out/
    merge     validate enrich_out/ + merge into 05-enriched/  (engine-agnostic)

    cv-rag/.venv/bin/python scripts/v2/enrich.py --mode prepare
    cv-rag/.venv/bin/python scripts/v2/enrich.py --mode ollama --limit 30
    cv-rag/.venv/bin/python scripts/v2/enrich.py --mode merge
"""
from __future__ import annotations
import argparse, glob, json, re, time, urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STRUCTURED = ROOT / "work" / "04-structured"
INBOX = ROOT / "work" / "enrich_inbox"
OUTBOX = ROOT / "work" / "enrich_out"
ENRICHED = ROOT / "work" / "05-enriched"
ENRICH_VERSION = "enrich-2.0.0"
BODY_CHARS = 6000     # excerpt fed to the model — enough for doc-level enrichment

ENRICH_SCHEMA = {
    "type": "object",
    "properties": {
        "tldr": {"type": "string"},
        "entities": {
            "type": "object",
            "properties": {
                "primary": {"type": "string"},
                "aliases": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["primary", "aliases"],
        },
        "core_question": {"type": "string"},
        "doc_type": {"type": "string",
                     "enum": ["how-to-guide", "listicle", "opinion", "reference",
                              "case-study", "news", "other"]},
        "key_topics": {"type": "array", "items": {"type": "string"}},
    },
    "required": ["tldr", "entities", "core_question", "doc_type", "key_topics"],
}

INSTRUCTIONS = (
    "Enrich a knowledge-base article for retrieval. Return ONLY the JSON schema. "
    "tldr <= 50 words. entities.primary = the main subject. core_question = the "
    "single question this article answers. key_topics = 3-8 short topic tags. "
    "Do NOT invent facts or topics not present in the article."
)


def build_prompt(title: str, body: str) -> str:
    return f"{INSTRUCTIONS}\n\nTITLE: {title}\n\nARTICLE:\n{body[:BODY_CHARS]}"


# ───────────────────────── prepare ─────────────────────────
def mode_prepare() -> None:
    INBOX.mkdir(parents=True, exist_ok=True)
    n = 0
    for p in sorted(glob.glob(str(STRUCTURED / "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        if d.get("status") != "kept":
            continue
        rec = {
            "name": Path(p).name,
            "title": (d.get("base_metadata") or {}).get("title") or "",
            "body": d["markdown"][:BODY_CHARS],
        }
        (INBOX / Path(p).name).write_text(
            json.dumps(rec, ensure_ascii=False, indent=2), encoding="utf-8")
        n += 1
    print(f"[prepare] wrote {n} inbox files → {INBOX}")


# ───────────────────────── ollama engine ─────────────────────────
def call_ollama(title: str, body: str, model: str = "gemma4:e4b") -> dict:
    req = {"model": model, "prompt": build_prompt(title, body), "stream": False,
           "format": ENRICH_SCHEMA, "options": {"temperature": 0, "seed": 42}}
    r = urllib.request.urlopen("http://localhost:11434/api/generate",
                               data=json.dumps(req).encode(), timeout=300)
    return json.loads(json.loads(r.read())["response"])


def mode_ollama(limit: int | None, model: str) -> None:
    OUTBOX.mkdir(parents=True, exist_ok=True)
    files = sorted(glob.glob(str(INBOX / "*.json")))
    if limit:
        files = files[:limit]
    done = 0
    for p in files:
        out_p = OUTBOX / Path(p).name
        if out_p.exists():
            continue
        rec = json.load(open(p, encoding="utf-8"))
        t = time.time()
        try:
            enr = call_ollama(rec["title"], rec["body"], model)
        except Exception as e:
            print(f"  ! {Path(p).name}: {e}")
            continue
        out_p.write_text(json.dumps(enr, ensure_ascii=False, indent=2), encoding="utf-8")
        done += 1
        if done % 10 == 0:
            print(f"  …{done}/{len(files)} ({time.time()-t:.0f}s last)")
    print(f"[ollama] enriched {done} → {OUTBOX}")


# ───────────────────────── merge + validate ─────────────────────────
def faithful(enr: dict, body: str, title: str = "") -> tuple[bool, str]:
    """entities.primary and ~a third of key_topics must be grounded in the text.

    Haystack = title + body, with hyphens/slashes normalized to spaces so
    'under-qualified' matches 'underqualified'. Tokens >=3 chars count (so short
    but meaningful tokens like 'ATS', 'git', 'cto' are honored)."""
    hay = re.sub(r"[-_/]+", " ", f"{title} {body}".lower())

    def grounded(phrase: str) -> bool:
        toks = [t for t in re.split(r"\W+", re.sub(r"[-_/]+", " ", phrase.lower())) if len(t) >= 3]
        return any(t in hay for t in toks) if toks else True

    prim = (enr.get("entities") or {}).get("primary", "")
    if not grounded(prim):
        return False, "primary-not-in-body"
    topics = enr.get("key_topics") or []
    if topics:
        hits = sum(1 for t in topics if grounded(t))
        if hits < max(1, len(topics) // 3):
            return False, "topics-not-in-body"
    return True, ""


def validate_schema(enr: dict) -> bool:
    if not isinstance(enr, dict):
        return False
    for k in ("tldr", "entities", "core_question", "doc_type", "key_topics"):
        if k not in enr:
            return False
    e = enr["entities"]
    return isinstance(e, dict) and "primary" in e and "aliases" in e


def mode_merge() -> None:
    ENRICHED.mkdir(parents=True, exist_ok=True)
    merged = enriched = passthrough = failed = 0
    fail_reasons: dict[str, int] = {}
    for p in sorted(glob.glob(str(STRUCTURED / "*.json"))):
        d = json.load(open(p, encoding="utf-8"))
        name = Path(p).name
        if d.get("status") != "kept":
            d["enrichment_status"] = "skipped-quarantined"
            (ENRICHED / name).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
            passthrough += 1
            continue
        out_p = OUTBOX / name
        if out_p.exists():
            try:
                enr = json.load(open(out_p, encoding="utf-8"))
            except Exception:
                enr = None
            if enr and validate_schema(enr):
                ok, reason = faithful(enr, d["markdown"], (d.get("base_metadata") or {}).get("title", ""))
                if ok:
                    meta = d.setdefault("base_metadata", {})
                    meta["tldr"] = enr["tldr"]
                    meta["entities"] = enr["entities"]
                    meta["core_question"] = enr["core_question"]
                    meta["doc_type"] = enr["doc_type"]
                    meta["key_topics"] = enr["key_topics"]
                    d["enrichment_status"] = "enriched"
                    d["enrich_version"] = ENRICH_VERSION
                    enriched += 1
                else:
                    d["enrichment_status"] = f"rejected:{reason}"
                    fail_reasons[reason] = fail_reasons.get(reason, 0) + 1
                    failed += 1
            else:
                d["enrichment_status"] = "rejected:bad-schema"
                fail_reasons["bad-schema"] = fail_reasons.get("bad-schema", 0) + 1
                failed += 1
        else:
            d["enrichment_status"] = "missing-enrichment"
        (ENRICHED / name).write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
        merged += 1
    print(f"[merge] total={merged+passthrough} enriched={enriched} "
          f"rejected={failed} {fail_reasons} passthrough(quarantined)={passthrough}")


def main():
    ap = argparse.ArgumentParser(description="Pipeline V2 Stage 4: LLM enrich")
    ap.add_argument("--mode", required=True, choices=["prepare", "ollama", "merge"])
    ap.add_argument("--limit", type=int, default=None)
    ap.add_argument("--model", default="gemma4:e4b")
    a = ap.parse_args()
    if a.mode == "prepare":
        mode_prepare()
    elif a.mode == "ollama":
        mode_ollama(a.limit, a.model)
    elif a.mode == "merge":
        mode_merge()


if __name__ == "__main__":
    main()

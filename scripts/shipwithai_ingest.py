"""
M5 — shipwithai_ingest.

Orchestrates the cv-rag pipeline against shipwithai-data/02-cleaned/, injecting
`source_corpus: "shipwithai-data"` and `source_url` into every Qdrant payload.

Pipeline order:
    build manifest + _processed/   (this script)
    parent.py                      (cv-rag, unchanged)
    PATCH parents.jsonl            (inject source_corpus, source_url)
    child.py                       (cv-rag, unchanged)
    PATCH children.jsonl           (inject source_corpus, source_url)
    tag.py                         (cv-rag, unchanged)
    embed.py                       (cv-rag, unchanged)
    upsert.py                      (cv-rag, unchanged)

Work dir layout (under shipwithai-data/_ingest_work/):
    manifest.jsonl
    _processed/<topic>/<domain>/<...>/<slug>.md   (body only — no frontmatter)
    parents.jsonl
    children.jsonl
    parents_tagged.jsonl, children_tagged.jsonl
    embeddings/...
    upsert_report.json

Idempotent: chunk_ids derive deterministically from source_path + headings, and
upsert uses UUID5(parent_id|child_id) as point IDs, so re-runs overwrite in place.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path

import yaml


SOURCE_CORPUS_TAG = "shipwithai-data"
CV_RAG_DEFAULT = Path("/home/matcry/Documents/Knowledge/cv-rag")


# ---------------------------------------------------------------------------
# Frontmatter helper (identical to clean / recrawl — kept local on purpose)
# ---------------------------------------------------------------------------

def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}, text
    fm = yaml.safe_load(text[4:end]) or {}
    body = text[end + 5 :]
    if not isinstance(fm, dict):
        return {}, text
    return fm, body


# ---------------------------------------------------------------------------
# Stage 1 — build manifest + _processed/
# ---------------------------------------------------------------------------

@dataclass
class IngestReport:
    parents: int = 0
    children: int = 0
    skipped: int = 0
    upserted_parents: int = 0
    upserted_children: int = 0
    server_parent_count: int = 0
    server_child_count: int = 0
    files_processed: int = 0
    notes: list[str] = field(default_factory=list)

    def __str__(self) -> str:
        return (
            f"IngestReport(files={self.files_processed}, parents={self.parents}, "
            f"children={self.children}, "
            f"upserted_parents={self.upserted_parents}, "
            f"upserted_children={self.upserted_children}, "
            f"server_count_parents={self.server_parent_count}, "
            f"server_count_children={self.server_child_count})"
        )


def build_manifest_and_processed(
    cleaned_root: Path, work_dir: Path
) -> tuple[int, dict[str, str]]:
    """Walk cleaned_root, write _processed/ + manifest.jsonl. Returns
    (count, source_path -> source_url mapping for later injection)."""
    processed_root = work_dir / "_processed"
    if processed_root.exists():
        shutil.rmtree(processed_root)
    processed_root.mkdir(parents=True)

    manifest_path = work_dir / "manifest.jsonl"
    url_by_source_path: dict[str, str] = {}

    count = 0
    with manifest_path.open("w", encoding="utf-8") as out:
        for md in sorted(cleaned_root.rglob("*.md")):
            rel = md.relative_to(cleaned_root)
            parts = rel.parts
            if len(parts) < 3:
                continue
            topic = parts[0]
            source_domain = parts[1]

            raw = md.read_text(encoding="utf-8", errors="replace")
            fm, body = parse_frontmatter(raw)
            source_url = fm.get("source_url", "")
            if not source_url:
                continue

            # Mirror the layout into _processed/, body only (no frontmatter —
            # that's what cv-rag/pipeline/parent.py expects)
            dest = processed_root / rel
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(body, encoding="utf-8")

            # cv-rag's manifest paths are relative to data/ for processed and
            # to its input root for source. We synthesize matching shapes.
            processed_rel = Path("_processed") / rel
            source_rel = Path("02-cleaned") / rel

            record = {
                "source_path": str(source_rel),
                "processed_path": str(processed_rel),
                "topic": topic,
                "source_domain": source_domain,
                "word_count": int(fm.get("word_count", 0)),
                "text_to_link_ratio": float(fm.get("text_to_link_ratio", 0.0)),
                "heading_count": int(fm.get("heading_count", 0)),
                "is_curated": bool(fm.get("is_curated", False)),
                "signal_score": float(fm.get("signal_score", 0.0)),
                "kept": True,
            }
            out.write(json.dumps(record, ensure_ascii=False) + "\n")
            url_by_source_path[record["source_path"]] = source_url
            count += 1

    return count, url_by_source_path


# ---------------------------------------------------------------------------
# Stage 2 — run a cv-rag pipeline script as a subprocess
# ---------------------------------------------------------------------------

def _python_for(cv_rag_root: Path) -> str:
    """Prefer cv-rag's .venv python (has fastembed, qdrant-client, etc).
    Falls back to current interpreter only if no venv is found."""
    candidate = cv_rag_root / ".venv" / "bin" / "python"
    if candidate.exists():
        return str(candidate)
    return sys.executable


def run_cv_rag_step(cv_rag_root: Path, script: str, work_dir: Path,
                    extra_args: list[str] | None = None) -> None:
    script_path = cv_rag_root / "pipeline" / script
    cmd = [_python_for(cv_rag_root), str(script_path), "--data", str(work_dir)]
    if extra_args:
        cmd.extend(extra_args)
    print(f"  -> {' '.join(cmd)}", file=sys.stderr)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.stderr:
        # cv-rag scripts log progress to stderr; pipe it through
        for line in result.stderr.splitlines():
            print(f"     {line}", file=sys.stderr)
    if result.returncode != 0:
        raise RuntimeError(
            f"{script} failed with exit {result.returncode}\n"
            f"stdout: {result.stdout}\nstderr: {result.stderr}"
        )


# ---------------------------------------------------------------------------
# Stage 3 — patch parents.jsonl and children.jsonl with corpus tag + URL
# ---------------------------------------------------------------------------

def patch_jsonl_with_corpus(
    path: Path, url_by_source_path: dict[str, str], cleaned_at: str
) -> int:
    """Add source_corpus, source_url, source_corpus_ingested_at to each row."""
    rows: list[dict] = []
    with path.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            rows.append(json.loads(line))

    missing = 0
    for r in rows:
        r["source_corpus"] = SOURCE_CORPUS_TAG
        r["source_corpus_ingested_at"] = cleaned_at
        sp = r.get("source_path", "")
        url = url_by_source_path.get(sp)
        if url is None:
            missing += 1
        else:
            r["source_url"] = url

    with path.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

    return len(rows), missing


# ---------------------------------------------------------------------------
# Run end to end
# ---------------------------------------------------------------------------

def run(
    cleaned_root: Path,
    work_dir: Path,
    *,
    cv_rag_root: Path = CV_RAG_DEFAULT,
    qdrant_host: str = "localhost",
    qdrant_port: int = 6333,
    upsert_mode: str = "incremental",
    skip_upsert: bool = False,
    tag_rules: Path | None = None,
) -> IngestReport:
    report = IngestReport()
    cleaned_at = datetime.now(timezone.utc).isoformat(timespec="seconds")

    work_dir.mkdir(parents=True, exist_ok=True)

    print(f"[1/7] building manifest from {cleaned_root}", file=sys.stderr)
    n, url_map = build_manifest_and_processed(cleaned_root, work_dir)
    report.files_processed = n
    print(f"      wrote {n} manifest entries", file=sys.stderr)

    print("[2/7] parent.py", file=sys.stderr)
    run_cv_rag_step(cv_rag_root, "parent.py", work_dir)

    print("[3/7] patching parents.jsonl with source_corpus + source_url", file=sys.stderr)
    n_parents, missing = patch_jsonl_with_corpus(
        work_dir / "parents.jsonl", url_map, cleaned_at
    )
    report.parents = n_parents
    if missing:
        report.notes.append(f"parents.jsonl: {missing} rows missing source_url")
    print(f"      patched {n_parents} parents ({missing} missing source_url)",
          file=sys.stderr)

    print("[4/7] child.py", file=sys.stderr)
    run_cv_rag_step(cv_rag_root, "child.py", work_dir)

    print("[5/7] patching children.jsonl with source_corpus + source_url", file=sys.stderr)
    n_children, missing_c = patch_jsonl_with_corpus(
        work_dir / "children.jsonl", url_map, cleaned_at
    )
    report.children = n_children
    if missing_c:
        report.notes.append(f"children.jsonl: {missing_c} rows missing source_url")
    print(f"      patched {n_children} children ({missing_c} missing source_url)",
          file=sys.stderr)

    print("[6/7] tag.py", file=sys.stderr)
    tag_args = []
    if tag_rules:
        tag_args = ["--rules", str(tag_rules)]
    run_cv_rag_step(cv_rag_root, "tag.py", work_dir, extra_args=tag_args)

    print("[7/7] embed.py + upsert.py", file=sys.stderr)
    run_cv_rag_step(cv_rag_root, "embed.py", work_dir)
    if not skip_upsert:
        run_cv_rag_step(
            cv_rag_root, "upsert.py", work_dir,
            extra_args=[
                "--host", qdrant_host,
                "--port", str(qdrant_port),
                "--upsert-mode", upsert_mode,
            ],
        )
        upsert_report_path = work_dir / "upsert_report.json"
        if upsert_report_path.exists():
            ur = json.loads(upsert_report_path.read_text(encoding="utf-8"))
            report.upserted_parents = ur.get("parents", {}).get("upserted", 0)
            report.upserted_children = ur.get("children", {}).get("upserted", 0)
            report.server_parent_count = ur.get("parents", {}).get("server_count", 0)
            report.server_child_count = ur.get("children", {}).get("server_count", 0)

    return report


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    here = Path(__file__).resolve().parent.parent
    parser = argparse.ArgumentParser(description="M5 — ingest cleaned corpus into cv-rag Qdrant")
    parser.add_argument("--cleaned", default=str(here / "02-cleaned"))
    parser.add_argument("--work-dir", default=str(here / "_ingest_work"))
    parser.add_argument("--cv-rag", default=str(CV_RAG_DEFAULT))
    parser.add_argument("--host", default="localhost")
    parser.add_argument("--port", type=int, default=6333)
    parser.add_argument("--upsert-mode", choices=("incremental", "full"), default="incremental")
    parser.add_argument("--skip-upsert", action="store_true",
                        help="run through embed but skip Qdrant upsert (smoke test)")
    parser.add_argument("--tag-rules", default=None,
                        help="path to tag_rules.yaml (default: cv-rag's)")
    args = parser.parse_args()

    report = run(
        Path(args.cleaned),
        Path(args.work_dir),
        cv_rag_root=Path(args.cv_rag),
        qdrant_host=args.host,
        qdrant_port=args.port,
        upsert_mode=args.upsert_mode,
        skip_upsert=args.skip_upsert,
        tag_rules=Path(args.tag_rules) if args.tag_rules else None,
    )
    print(str(report))
    for note in report.notes:
        print(f"NOTE: {note}", file=sys.stderr)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Phase 2: Extract metadata and add YAML frontmatter to crawled .md files.

Strategy:
  1. Deterministic: word_count, text_to_link_ratio, title (H1), topic (folder),
     career_level (keyword rules), signal_score, tags
  2. Quality gate: drop files with word_count < 200 OR text_to_link_ratio < 0.30
  3. Haiku Batch: files where title OR career_level is still unknown → batch_queue.json
     Run 02_haiku_batch.py after this script to resolve them.

Usage:
    python scripts/02_extract_metadata.py
    python scripts/02_extract_metadata.py --topic github-portfolio
    python scripts/02_extract_metadata.py --dry-run   # report counts, no writes
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

import yaml

RAW_DIR     = Path(__file__).parent.parent / "01-raw"
CLEANED_DIR = Path(__file__).parent.parent / "02-cleaned"
BATCH_QUEUE = Path(__file__).parent.parent / "02-cleaned" / "batch_queue.json"

MIN_WORD_COUNT      = 200
MIN_LINK_RATIO      = 0.30

# ── Topic vocab (folder name → canonical topic) ───────────────────────────────

FOLDER_TO_TOPIC: dict[str, str] = {
    "github-portfolio":    "github-portfolio",
    "career-gap":          "career-gap",
    "career-change":       "career-change",
    "ats-optimization":    "ats-optimization",
    "salary-negotiation":  "salary-negotiation",
    "senior-level-resume": "senior-level-resume",
    "executive-resume":    "executive-resume",
    "remote-work-resume":  "remote-work-resume",
    "linkedin-profile":    "linkedin-profile",
    "cover-letter":        "cover-letter",
    "git-first-job":       "git-first-job",
    "claude-code-workflow":"claude-code-workflow",
}

TOPIC_KEYWORDS: dict[str, list[str]] = {
    "github-portfolio":   ["github", "open.source", "portfolio", "repository", "pinned repo"],
    "career-gap":         ["career gap", "employment gap", "career break", "returning to work"],
    "career-change":      ["career change", "career switch", "bootcamp", "non-cs", "transferable"],
    "ats-optimization":   ["ats", "applicant tracking", "keyword", "resume scan"],
    "salary-negotiation": ["salary", "negotiat", "compensation", "offer", "stock option", "esop"],
    "senior-level-resume":["senior engineer", "staff engineer", "principal", "tech lead", "10 year"],
    "executive-resume":   ["cto", "vp engineering", "director", "c-suite", "head of engineering"],
    "remote-work-resume": ["remote", "distributed team", "async", "work from home"],
    "linkedin-profile":   ["linkedin", "linkedin profile", "linkedin headline", "open to work"],
    "cover-letter":         ["cover letter", "covering letter"],
    "git-first-job":        ["git commit", "git branch", "pull request", "git merge", "git rebase",
                              "git workflow", "first pr", "open source contribution", "git for beginners"],
    "claude-code-workflow": ["claude code", "claude cli", "agentic coding", "ai pair programming",
                              "ai coding assistant", "anthropic claude", "copilot vs claude"],
    "resume-basics":      ["resume", "cv", "curriculum vitae"],
    "resume-formatting":  ["resume format", "resume layout", "resume design", "font", "margin"],
    "work-experience":    ["work experience", "job description", "bullet point", "accomplishment"],
    "skills-section":     ["skills section", "technical skills", "hard skills", "soft skills"],
    "education-section":  ["education", "degree", "university", "gpa", "certification"],
    "projects-section":   ["projects section", "side project", "personal project"],
    "interview-prep":     ["interview", "behavioral", "technical interview", "leetcode"],
    "job-search-strategy":["job search", "job board", "networking", "recruiter", "cold outreach"],
}

# ── Career level keyword rules ────────────────────────────────────────────────

LEVEL_RULES: dict[str, list[str]] = {
    "entry":     ["entry.level", "new grad", "first job", r"0.2 year", "junior", "internship",
                  "fresh graduate", "early career", "no experience", "recent graduate"],
    "mid":       ["mid.level", r"2.5 year", r"3.7 year", r"3.5 year", "individual contributor",
                  "associate engineer", "mid career"],
    "senior":    ["senior engineer", "senior developer", "senior software", "staff engineer",
                  "principal engineer", r"7\+? year", r"10\+? year", "tech lead", "architect"],
    "executive": ["director", r"\bvp\b", "vice president", "c.suite", "cto", "ceo",
                  r"head of engineering", r"15\+? year", "leadership role", "engineering manager"],
}

# ── Tag keyword rules ─────────────────────────────────────────────────────────

TAG_RULES: dict[str, list[str]] = {
    "remote":         ["remote", "distributed", "async", "work from home"],
    "open-source":    ["open.source", "github", "contribution"],
    "career-change":  ["career change", "career switch", "bootcamp"],
    "ats":            [r"\bats\b", "applicant tracking"],
    "salary":         ["salary", "negotiat", "compensation"],
    "cover-letter":   ["cover letter"],
    "linkedin":       ["linkedin"],
    "gap":            ["career gap", "employment gap", "career break"],
    "senior":         ["senior", "staff", "principal", "tech lead"],
    "executive":      ["cto", "director", r"\bvp\b", "c.suite"],
}


# ── Metrics ───────────────────────────────────────────────────────────────────

def compute_metrics(text: str) -> dict:
    lines = text.splitlines()
    word_count = 0
    total_chars = 0
    link_chars = 0
    heading_count = 0

    for line in lines:
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            heading_count += 1
            continue
        word_count += len(stripped.split())
        total_chars += len(stripped)
        for m in re.finditer(r'\[([^\]]*)\]\([^)]*\)', stripped):
            link_chars += len(m.group(0))

    text_to_link_ratio = round((total_chars - link_chars) / total_chars, 4) if total_chars else 0.0
    return {
        "word_count": word_count,
        "text_to_link_ratio": text_to_link_ratio,
        "heading_count": heading_count,
    }


def signal_score(metrics: dict, is_curated: bool) -> float:
    score = metrics["text_to_link_ratio"]
    if is_curated:
        score += 0.2
    hc = metrics["heading_count"]
    wc = metrics["word_count"]
    if hc > 0 and wc / hc > 100:
        score += 0.1
    return round(max(0.0, min(1.0, score)), 4)


# ── Deterministic extractors ──────────────────────────────────────────────────

def extract_title(text: str) -> str | None:
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("# "):
            return s[2:].strip()
    return None


def infer_topic(folder: str, text: str) -> str | None:
    if folder in FOLDER_TO_TOPIC:
        return FOLDER_TO_TOPIC[folder]
    low = text.lower()
    for topic, keywords in TOPIC_KEYWORDS.items():
        if any(re.search(kw, low) for kw in keywords):
            return topic
    return None


def infer_career_levels(text: str) -> list[str]:
    low = text.lower()
    found = []
    for level, patterns in LEVEL_RULES.items():
        if any(re.search(p, low) for p in patterns):
            found.append(level)
    return found or []


def infer_tags(text: str) -> list[str]:
    low = text.lower()
    return [tag for tag, patterns in TAG_RULES.items()
            if any(re.search(p, low) for p in patterns)]


def source_url_from_path(md_path: Path, raw_dir: Path) -> tuple[str, str]:
    """Reconstruct source URL and domain from file path under 01-raw/<topic>/<domain>/..."""
    try:
        rel = md_path.relative_to(raw_dir)  # <topic>/<domain>/path/file.md
        parts = rel.parts                    # ('github-portfolio', 'github.com', 'path', 'file.md')
        if len(parts) >= 2:
            domain_and_path = "/".join(parts[1:]).removesuffix(".md")
            url = "https://" + domain_and_path
            domain = parts[1]
            return url, domain
    except Exception:
        pass
    return "", ""


# ── Frontmatter builder ───────────────────────────────────────────────────────

def build_frontmatter(fields: dict) -> str:
    lines = ["---"]
    for k, v in fields.items():
        if isinstance(v, list):
            if v:
                lines.append(f"{k}:")
                for item in v:
                    lines.append(f"  - {item}")
            else:
                lines.append(f"{k}: []")
        elif isinstance(v, bool):
            lines.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, float):
            lines.append(f"{k}: {v}")
        elif isinstance(v, int):
            lines.append(f"{k}: {v}")
        else:
            safe = str(v).replace('"', '\\"')
            lines.append(f'{k}: "{safe}"')
    lines.append("---")
    return "\n".join(lines) + "\n"


# ── Per-file processing ───────────────────────────────────────────────────────

def process_file(
    src: Path,
    raw_dir: Path,
    out_dir: Path,
    dry_run: bool,
) -> dict:
    text = src.read_text(encoding="utf-8", errors="replace")

    # Strip existing frontmatter if present
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            text = text[end + 4:].lstrip()

    metrics = compute_metrics(text)
    wc      = metrics["word_count"]
    ratio   = metrics["text_to_link_ratio"]

    # Quality gate
    if wc < MIN_WORD_COUNT or ratio < MIN_LINK_RATIO:
        return {"status": "dropped", "path": str(src), "word_count": wc, "ratio": ratio}

    # Folder = topic hint
    try:
        folder = src.relative_to(raw_dir).parts[0]
    except Exception:
        folder = ""

    source_url, source_domain = source_url_from_path(src, raw_dir)

    title          = extract_title(text)
    topic          = infer_topic(folder, text)
    career_levels  = infer_career_levels(text)
    tags           = infer_tags(text)
    score          = signal_score(metrics, is_curated=False)

    needs_haiku = (title is None) or (not career_levels)

    fields = {
        "title":              title or "",
        "topic":              topic or "",
        "career_level":       career_levels,
        "source_url":         source_url,
        "source_domain":      source_domain,
        "word_count":         wc,
        "text_to_link_ratio": ratio,
        "signal_score":       score,
        "is_curated":         False,
        "tags":               tags,
        "ingested_at":        str(date.today()),
    }

    if not dry_run:
        # Compute output path mirroring 01-raw structure under 02-cleaned
        rel = src.relative_to(raw_dir)
        dest = out_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(build_frontmatter(fields) + "\n" + text, encoding="utf-8")

    return {
        "status":       "haiku_queue" if needs_haiku else "ok",
        "path":         str(src),
        "out_path":     str(out_dir / src.relative_to(raw_dir)) if not dry_run else "",
        "needs_haiku":  needs_haiku,
        "fields":       fields,
    }


# ── Main ──────────────────────────────────────────────────────────────────────

def main(only: str | None, dry_run: bool) -> None:
    if only:
        topic_dirs = [RAW_DIR / only]
        if not topic_dirs[0].exists():
            print(f"Topic dir not found: {topic_dirs[0]}")
            sys.exit(1)
    else:
        topic_dirs = [d for d in sorted(RAW_DIR.iterdir()) if d.is_dir()]

    md_files = []
    for td in topic_dirs:
        md_files.extend(td.rglob("*.md"))

    print(f"\nPhase 2 — Metadata extraction: {len(md_files)} files from {len(topic_dirs)} topic(s)\n")

    stats   = {"ok": 0, "dropped": 0, "haiku_queue": 0}
    haiku_q = []

    for src in sorted(md_files):
        result = process_file(src, RAW_DIR, CLEANED_DIR, dry_run)
        status = result["status"]
        stats[status] = stats.get(status, 0) + 1
        if status == "haiku_queue":
            haiku_q.append({
                "path":   result["path"],
                "fields": result["fields"],
                "snippet": src.read_text(encoding="utf-8", errors="replace")[:2000],
            })

    # Save batch queue for 02_haiku_batch.py
    if not dry_run and haiku_q:
        CLEANED_DIR.mkdir(parents=True, exist_ok=True)
        BATCH_QUEUE.write_text(json.dumps(haiku_q, indent=2, ensure_ascii=False))

    print(f"  OK (deterministic):  {stats.get('ok', 0)}")
    print(f"  Haiku queue:         {stats.get('haiku_queue', 0)}")
    print(f"  Dropped (quality):   {stats.get('dropped', 0)}")
    if not dry_run and haiku_q:
        print(f"\n  Batch queue → {BATCH_QUEUE}")
        print("  Next: python scripts/02_haiku_batch.py")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Phase 2: Extract metadata + frontmatter")
    parser.add_argument("--topic", metavar="NAME", help="Process single topic only")
    parser.add_argument("--dry-run", action="store_true", help="Report counts, no writes")
    args = parser.parse_args()
    main(only=args.topic, dry_run=args.dry_run)

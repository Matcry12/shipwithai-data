#!/usr/bin/env python3
"""Regenerate keyword-frequency-analysis.md from 03-categorized/ (773 files)."""
from __future__ import annotations

import re
import json
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path

CATEGORIZED = Path(__file__).parent.parent / "03-categorized"
MANIFEST    = CATEGORIZED / "manifest.json"
OUT_FILE    = Path(__file__).parent.parent / "keyword-frequency-analysis.md"

STOPWORDS = {
    "the", "and", "for", "are", "that", "this", "with", "have", "you", "your",
    "from", "they", "will", "can", "not", "but", "all", "been", "has", "its",
    "was", "were", "when", "what", "how", "who", "which", "their", "there",
    "about", "into", "than", "also", "more", "some", "one", "two", "three",
    "use", "used", "using", "make", "made", "get", "got", "just", "like",
    "would", "could", "should", "may", "might", "need", "want", "our", "out",
    "any", "each", "both", "even", "most", "such", "those", "these", "them",
    "then", "now", "new", "first", "last", "next", "well", "way", "other",
    "many", "much", "very", "so", "as", "at", "by", "do", "if", "in", "is",
    "it", "my", "of", "on", "or", "to", "up", "we", "be", "an", "a",
}

DOMAIN_BIGRAMS = [
    "resume template", "cover letter", "job description", "applicant tracking",
    "ats optimization", "career gap", "career change", "open source",
    "linkedin profile", "github portfolio", "salary negotiation", "job search",
    "senior engineer", "staff engineer", "tech lead", "pull request",
    "git workflow", "git rebase", "git merge", "commit message", "code review",
    "pair programming", "ai coding", "claude code", "career level",
    "keyword optimization", "executive resume", "remote work", "work from home",
    "first job", "entry level", "mid level", "technical interview",
]


def strip_frontmatter(text: str) -> str:
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip()
    return text


def clean_text(text: str) -> str:
    text = strip_frontmatter(text)
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"`[^`]+`", " ", text)
    text = re.sub(r"https?://\S+", " ", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    return text.lower()


def extract_words(text: str) -> list[str]:
    return [w for w in text.split() if len(w) >= 3 and w not in STOPWORDS]


def count_bigrams(text: str, phrases: list[str]) -> Counter:
    counts: Counter = Counter()
    for phrase in phrases:
        counts[phrase] = len(re.findall(re.escape(phrase), text))
    return counts


def main() -> None:
    records = json.loads(MANIFEST.read_text())

    # Group manifest entries by topic, resolve file paths
    topic_files: dict[str, list[Path]] = defaultdict(list)
    for rec in records:
        topic = rec.get("topic", "").strip()
        file_rel = rec.get("file", "")
        if topic and file_rel:
            topic_files[topic].append(CATEGORIZED / file_rel)

    total_files = sum(len(v) for v in topic_files.values())
    topic_data: dict[str, dict] = {}

    for topic in sorted(topic_files):
        files = topic_files[topic]
        words: list[str] = []
        full_text = ""
        for f in files:
            if not f.exists():
                continue
            raw = f.read_text(encoding="utf-8", errors="replace")
            cleaned = clean_text(raw)
            full_text += " " + cleaned
            words.extend(extract_words(cleaned))
        topic_data[topic] = {
            "files": len(files),
            "word_freq": Counter(words),
            "bigram_freq": count_bigrams(full_text, DOMAIN_BIGRAMS),
        }

    # Build markdown
    lines = [
        "# Keyword Frequency Analysis\n\n",
        "Top keywords extracted from cleaned article content per topic.\n",
        "Bigrams (2-word phrases) shown where they add signal beyond single words.\n\n",
        f"**Files analyzed:** {total_files}  \n",
        f"**Topics:** {len(topic_data)}  \n",
        f"**Generated:** {date.today()}\n\n",
        "---\n\n",
        "## Summary Table — Top 5 Keywords per Topic\n\n",
        "| Topic | Files | Top Keywords |\n",
        "|-------|-------|----------|\n",
    ]
    for topic, data in topic_data.items():
        top5 = ", ".join(w for w, _ in data["word_freq"].most_common(5))
        lines.append(f"| {topic} | {data['files']} | {top5} |\n")

    lines.append("\n---\n\n")

    for topic, data in topic_data.items():
        lines.append(f"## {topic}\n\n")
        lines.append(f"**{data['files']} files**\n\n")
        lines.append("### Top 30 Keywords\n\n")
        lines.append("| Rank | Keyword | Count |\n")
        lines.append("|------|---------|-------|\n")
        for rank, (word, count) in enumerate(data["word_freq"].most_common(30), 1):
            lines.append(f"| {rank} | {word} | {count} |\n")

        lines.append("\n### Key Phrases (domain bigrams)\n\n")
        lines.append("| Phrase | Count |\n")
        lines.append("|--------|-------|\n")
        relevant = [(p, c) for p, c in data["bigram_freq"].most_common() if c > 0]
        for phrase, count in relevant:
            lines.append(f"| {phrase} | {count} |\n")
        lines.append("\n")

    OUT_FILE.write_text("".join(lines), encoding="utf-8")
    print(f"Written → {OUT_FILE}")
    print(f"Files analyzed: {total_files} | Topics: {len(topic_data)}")


if __name__ == "__main__":
    main()

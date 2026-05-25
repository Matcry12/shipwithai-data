#!/usr/bin/env python3
import os
import json
from collections import defaultdict

def analyze_frequency(manifest_file):
    """Generate frequency analysis and gap scoring"""

    with open(manifest_file, 'r') as f:
        manifest = json.load(f)

    # Cross-tabulation
    matrix = defaultdict(lambda: {'entry': 0, 'mid': 0, 'senior': 0, 'executive': 0})
    word_counts = defaultdict(lambda: {'min': float('inf'), 'max': 0, 'total': 0, 'count': 0})

    for topic, articles in manifest.items():
        for article in articles:
            for level in article['career_level']:
                matrix[topic][level] += 1

    # Generate report
    report = "# CV Knowledge Base Frequency Analysis\n\n"
    report += "## Topic × Career Level Cross-Tabulation\n\n"
    report += "| Topic | Entry | Mid | Senior | Executive | Total |\n"
    report += "|---|---|---|---|---|---|\n"

    topics_sorted = sorted(matrix.keys())
    totals_by_level = {'entry': 0, 'mid': 0, 'senior': 0, 'executive': 0}
    grand_total = 0

    for topic in topics_sorted:
        row = matrix[topic]
        total = sum(row.values())
        grand_total += total

        for level in ['entry', 'mid', 'senior', 'executive']:
            totals_by_level[level] += row[level]

        report += f"| {topic} | {row['entry']} | {row['mid']} | {row['senior']} | {row['executive']} | {total} |\n"

    report += f"| **TOTAL** | **{totals_by_level['entry']}** | **{totals_by_level['mid']}** | **{totals_by_level['senior']}** | **{totals_by_level['executive']}** | **{grand_total}** |\n"

    # Gap scoring
    report += "\n## Gap Analysis (by Cell)\n\n"
    report += "Gap Score = 1 / (count + 1), normalized\n\n"
    report += "Sparse cells (highest gap scores):\n\n"

    gaps = []
    for topic in topics_sorted:
        for level in ['entry', 'mid', 'senior', 'executive']:
            count = matrix[topic][level]
            gap_score = 1 / (count + 1)
            gaps.append((gap_score, topic, level, count))

    gaps.sort(reverse=True)

    for gap_score, topic, level, count in gaps[:20]:
        report += f"- {topic} × {level}: {count} articles (gap: {gap_score:.3f})\n"

    report += "\n## Coverage Summary\n\n"
    report += f"- Total articles: {grand_total}\n"
    report += f"- Total topics: {len(topics_sorted)}\n"
    report += f"- Average articles per topic: {grand_total / len(topics_sorted):.1f}\n"

    return report, {
        'matrix': dict(matrix),
        'totals_by_level': totals_by_level,
        'totals_by_topic': {t: sum(matrix[t].values()) for t in topics_sorted},
        'grand_total': grand_total,
    }

if __name__ == '__main__':
    manifest_file = '03-categorized/manifest.json'

    if os.path.exists(manifest_file):
        report, data = analyze_frequency(manifest_file)

        # Write report
        with open('04-frequency/frequency_report.md', 'w') as f:
            f.write(report)

        # Write JSON data
        os.makedirs('04-frequency', exist_ok=True)
        with open('04-frequency/frequency_report.json', 'w') as f:
            json.dump(data, f, indent=2)

        print("✓ Frequency analysis complete")
        print(f"  - Total articles analyzed: {data['grand_total']}")
        print(f"  - Topics: {len(data['totals_by_topic'])}")
        print(f"  - Reports saved to 04-frequency/")
    else:
        print(f"Error: {manifest_file} not found")

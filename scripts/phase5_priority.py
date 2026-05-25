#!/usr/bin/env python3
import os
import json

# Team relevance weights (from PLAN.md)
TEAM_WEIGHTS = {
    'entry': 0.6,
    'mid': 1.0,
    'senior': 1.2,
    'executive': 0.4,
}

def calculate_priority(frequency_data):
    """Calculate priority scores for topics"""

    matrix = frequency_data['matrix']
    priorities = []

    for topic, levels in matrix.items():
        for level in ['entry', 'mid', 'senior', 'executive']:
            count = levels[level]
            # Gap score: higher gap = more sparse = higher priority
            gap_score = 1 / (count + 1)
            # Apply team weight
            weight = TEAM_WEIGHTS[level]
            # Priority score
            priority = gap_score * weight

            priorities.append({
                'topic': topic,
                'career_level': level,
                'article_count': count,
                'gap_score': round(gap_score, 3),
                'weight': weight,
                'priority_score': round(priority, 3),
            })

    # Sort by priority score (descending)
    priorities.sort(key=lambda x: -x['priority_score'])

    return priorities[:30]  # Top 30

def generate_priority_list(priorities):
    """Generate human-readable priority list"""

    report = "# CV Micro-Course: Priority Topics (Top 30)\n\n"
    report += "## Rationale\n\n"
    report += "Priority Score = Gap Score × Team Relevance Weight\n\n"
    report += "- Gap Score: 1/(count+1) — measures sparsity (higher = more needed)\n"
    report += "- Team Weights: entry=0.6, mid=1.0, senior=1.2, executive=0.4\n"
    report += "- Team focus: mid-to-senior level engineers\n\n"

    report += "## Recommended Topics for Micro-Courses\n\n"
    report += "| # | Topic | Level | Count | Gap | Priority |\n"
    report += "|---|---|---|---|---|---|\n"

    for i, item in enumerate(priorities[:15], 1):
        report += f"| {i} | {item['topic']} | {item['career_level']} | {item['article_count']} | {item['gap_score']} | {item['priority_score']} |\n"

    report += "\n## Detailed Rankings (Top 30)\n\n"

    for i, item in enumerate(priorities, 1):
        report += f"{i}. **{item['topic']}** ({item['career_level']})\n"
        report += f"   - Articles: {item['article_count']}\n"
        report += f"   - Gap Score: {item['gap_score']}\n"
        report += f"   - Priority: {item['priority_score']}\n\n"

    return report

if __name__ == '__main__':
    freq_file = '04-frequency/frequency_report.json'

    if os.path.exists(freq_file):
        with open(freq_file, 'r') as f:
            frequency_data = json.load(f)

        priorities = calculate_priority(frequency_data)

        # Write priority list
        os.makedirs('05-priority', exist_ok=True)
        report = generate_priority_list(priorities)

        with open('05-priority/priority_list.md', 'w') as f:
            f.write(report)

        with open('05-priority/priority_scores.json', 'w') as f:
            json.dump(priorities, f, indent=2)

        print("✓ Priority analysis complete")
        print(f"\nTop 5 Topics:")
        for i, p in enumerate(priorities[:5], 1):
            print(f"  {i}. {p['topic']} ({p['career_level']}): {p['priority_score']}")
    else:
        print(f"Error: {freq_file} not found")

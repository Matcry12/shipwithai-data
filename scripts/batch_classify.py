#!/usr/bin/env python3
import os
import json
import re
from pathlib import Path

# Topic mapping from folder paths
TOPIC_MAP = {
    'github-portfolio': 'github-portfolio',
    'career-gap': 'career-gap',
    'career-change': 'career-change',
    'ats-optimization': 'ats-optimization',
    'salary-negotiation': 'salary-negotiation',
    'senior-level-resume': 'senior-level-resume',
    'executive-resume': 'executive-resume',
    'remote-work-resume': 'remote-work-resume',
    'cover-letter': 'cover-letter',
    'linkedin-profile': 'linkedin-profile',
}

# Career level inference patterns
def infer_career_level(folder_path, filename):
    """Infer career level from folder and filename"""
    lower_path = folder_path.lower()
    lower_name = filename.lower()

    # Explicit signals
    if 'senior' in lower_path or 'senior' in lower_name:
        return ['senior', 'executive']
    if 'executive' in lower_path:
        return ['executive']
    if 'entry' in lower_name or 'first-job' in lower_name or 'bootcamp' in lower_name:
        return ['entry']
    if 'career-change' in lower_path or 'no-experience' in lower_name:
        return ['entry']
    if 'career-gap' in lower_path:
        return ['entry', 'mid', 'senior', 'executive']
    if 'salary-negotiation' in lower_path:
        return ['entry', 'mid', 'senior', 'executive']
    if 'ats-optimization' in lower_path:
        return ['mid', 'senior']
    if 'github' in lower_path or 'open-source' in lower_path:
        return ['entry', 'mid', 'senior', 'executive']
    if 'cover-letter' in lower_path:
        return ['entry', 'mid', 'senior', 'executive']
    if 'linkedin' in lower_path:
        return ['entry', 'mid', 'senior', 'executive']

    # Default to all levels if unsure
    return ['entry', 'mid', 'senior', 'executive']

def extract_title(filepath):
    """Extract title from H1 or filename"""
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read(2000)

        # Look for H1
        match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        if match:
            return match.group(1).strip()

        # Look for title in frontmatter
        match = re.search(r'title:\s*["\']?(.+?)["\']?\n', content)
        if match:
            return match.group(1).strip()
    except:
        pass

    # Fallback: use filename
    filename = os.path.basename(filepath)
    # Clean up filename
    title = filename.replace('.md', '').replace('-', ' ').replace('_', ' ')
    return title.title()

def classify_articles(raw_dir, output_file):
    """Classify all articles in raw directory"""
    classifications = []

    for root, dirs, files in os.walk(raw_dir):
        for filename in files:
            if not filename.endswith('.md'):
                continue

            filepath = os.path.join(root, filename)
            relative_path = os.path.relpath(filepath, raw_dir)

            # Infer topic from folder path
            topic = None
            for key, value in TOPIC_MAP.items():
                if key in root:
                    topic = value
                    break

            if not topic:
                continue  # Skip if no topic match

            title = extract_title(filepath)
            career_level = infer_career_level(root, filename)

            classification = {
                'file': f'01-raw/{relative_path}',
                'title': title,
                'topic': topic,
                'career_level': career_level
            }

            classifications.append(classification)

    # Write to JSONL
    with open(output_file, 'a', encoding='utf-8') as f:
        for item in classifications:
            f.write(json.dumps(item) + '\n')

    return len(classifications)

if __name__ == '__main__':
    raw_dir = '/home/matcry/Documents/Knowledge/shipwithai-data/01-raw'
    output_file = '/home/matcry/Documents/Knowledge/shipwithai-data/02-cleaned/CLASSIFICATIONS.jsonl'

    count = classify_articles(raw_dir, output_file)
    print(f"Classified {count} articles")

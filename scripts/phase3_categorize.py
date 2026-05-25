#!/usr/bin/env python3
import os
import json
import shutil
from pathlib import Path

def categorize_articles(input_jsonl, source_dir, target_dir):
    """Organize articles into topic folders and create manifest"""

    os.makedirs(target_dir, exist_ok=True)
    manifest = {}
    topic_dirs = set()

    with open(input_jsonl, 'r') as f:
        for line in f:
            data = json.loads(line)

            source_file = os.path.join(source_dir, data['file'].replace('01-raw/', ''))
            topic = data['topic']

            # Create topic directory
            topic_dir = os.path.join(target_dir, topic)
            os.makedirs(topic_dir, exist_ok=True)
            topic_dirs.add(topic)

            # Copy file
            if os.path.exists(source_file):
                target_file = os.path.join(topic_dir, os.path.basename(data['file']))
                shutil.copy2(source_file, target_file)

            # Add to manifest
            if topic not in manifest:
                manifest[topic] = []

            manifest[topic].append({
                'filename': os.path.basename(data['file']),
                'title': data['title'],
                'career_level': data['career_level'],
                'source_url': '',  # Can be extracted from original file if needed
            })

    # Write manifest
    manifest_file = os.path.join(target_dir, 'manifest.json')
    with open(manifest_file, 'w') as f:
        json.dump(manifest, f, indent=2)

    return len(manifest), sum(len(v) for v in manifest.values()), list(topic_dirs)

if __name__ == '__main__':
    source_dir = '01-raw'
    target_dir = '03-categorized'
    input_jsonl = '02-cleaned/CLASSIFICATIONS.jsonl'

    topics, count, topic_list = categorize_articles(input_jsonl, source_dir, target_dir)

    print(f"Categorized {count} articles into {topics} topic folders")
    print(f"\nTopics created:")
    for topic in sorted(topic_list):
        print(f"  - {topic}")

import json
import re
import subprocess
from .models import ClassificationInput, ClassificationResult

SYSTEM_PROMPT = """You are a resume content classifier. Given a snippet of a web article, extract:
1. title: a short descriptive title (max 80 chars), inferred from content if no H1 present
2. topic: the single best-fit topic from this list: resume-basics, resume-formatting, work-experience, skills-section, education-section, projects-section, github-portfolio, open-source-contributions, cover-letter, linkedin-profile, career-gap, career-change, salary-negotiation, ats-optimization, job-search-strategy, interview-prep, senior-level-resume, executive-resume, remote-work-resume
3. career_level: array of applicable levels from [entry, mid, senior, executive]

Respond ONLY with valid JSON: {"title": "...", "topic": "...", "career_level": ["..."]}"""

def build_prompt(input: ClassificationInput) -> str:
    """Build user message with hints and article snippet (first 3000 chars)."""
    snippet = input.text[:3000]

    context_parts = []
    if input.existing_title:
        context_parts.append(f"Existing title hint: {input.existing_title}")
    if input.existing_topic:
        context_parts.append(f"Existing topic hint: {input.existing_topic}")
    if input.existing_career_levels:
        context_parts.append(f"Existing career_level hint: {input.existing_career_levels}")

    context = "\n".join(context_parts) if context_parts else ""

    message = f"""Article snippet:
---
{snippet}
---

{context}"""

    return message

def parse_llm_response(raw: str) -> dict | None:
    """Extract JSON object from LLM response text."""
    # Try to find JSON in response
    json_match = re.search(r'\{[^{}]+\}', raw, re.DOTALL)

    if not json_match:
        return None

    try:
        return json.loads(json_match.group(0))
    except json.JSONDecodeError:
        return None

def classify_with_llm(input: ClassificationInput) -> ClassificationResult | None:
    """Call claude CLI with system prompt + snippet. Parse JSON response."""
    try:
        prompt = build_prompt(input)

        # Call claude CLI
        result = subprocess.run(
            ["claude", "run", "--system", SYSTEM_PROMPT],
            input=prompt,
            capture_output=True,
            text=True,
            timeout=30
        )

        if result.returncode != 0:
            return None

        # Parse JSON from response
        response_data = parse_llm_response(result.stdout)

        if not response_data:
            return None

        # Validate required fields
        if not all(k in response_data for k in ["title", "topic", "career_level"]):
            return None

        return ClassificationResult(
            title=response_data["title"],
            topic=response_data["topic"],
            career_level=response_data["career_level"],
            confidence="llm"
        )

    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.SubprocessError) as e:
        return None

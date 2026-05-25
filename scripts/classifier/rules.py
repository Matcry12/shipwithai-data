import re
from .constants import VALID_TOPICS, TOPIC_KEYWORDS, LEVEL_RULES
from .models import ClassificationInput, ClassificationResult
from .title_extractor import extract_title

def infer_topic(text: str, folder_hint: str = "") -> str | None:
    """Infer topic from folder hint or keyword matching.

    Returns topic name if detected, None otherwise.
    """
    # Priority 1: folder_hint is a direct mapping
    if folder_hint and folder_hint in VALID_TOPICS:
        return folder_hint

    if not text:
        return None

    # Priority 2: keyword regex matching
    text_lower = text.lower()
    scores = {}

    for topic, pattern in TOPIC_KEYWORDS.items():
        try:
            matches = len(re.findall(pattern, text_lower, re.IGNORECASE))
            if matches > 0:
                scores[topic] = matches
        except re.error:
            continue

    if not scores:
        return None

    # Return topic with highest keyword count
    best_topic = max(scores.items(), key=lambda x: x[1])[0]
    return best_topic if scores[best_topic] >= 2 else None

def infer_career_levels(text: str) -> list[str]:
    """Infer applicable career levels from keyword patterns.

    Returns list of matched levels, empty list if none match.
    """
    if not text:
        return []

    matched_levels = []
    text_lower = text.lower()

    for level, pattern in LEVEL_RULES.items():
        try:
            if re.search(pattern, text_lower, re.IGNORECASE):
                matched_levels.append(level)
        except re.error:
            continue

    return matched_levels

def classify_deterministic(input: ClassificationInput) -> ClassificationResult | None:
    """Attempt full deterministic classification.

    Returns ClassificationResult if ALL three fields can be determined,
    None if any field is ambiguous/missing (signals LLM fallback needed).
    """
    # Priority: use existing values from input if provided
    topic = input.existing_topic if input.existing_topic else infer_topic(input.text, input.folder_hint)

    if not topic:
        return None

    title = input.existing_title if input.existing_title else extract_title(input.text)

    if not title:
        return None

    # Career level: use existing or infer
    if input.existing_career_levels:
        career_level = input.existing_career_levels
    else:
        career_level = infer_career_levels(input.text)

    if not career_level:
        return None

    return ClassificationResult(
        title=title,
        topic=topic,
        career_level=career_level,
        confidence="deterministic"
    )

from .constants import VALID_TOPICS, VALID_CAREER_LEVELS, MAX_TITLE_LENGTH
from .models import ClassificationResult
from .title_extractor import truncate_title

def validate_result(result: ClassificationResult) -> ClassificationResult:
    """Validate and normalize classification output.

    Raises ValueError if output cannot be corrected to valid state.
    """
    # Validate title
    if not result.title or not isinstance(result.title, str):
        raise ValueError(f"Invalid title: {result.title}")

    result.title = truncate_title(result.title, MAX_TITLE_LENGTH)

    # Validate topic
    if result.topic not in VALID_TOPICS:
        raise ValueError(f"Invalid topic '{result.topic}'. Must be one of: {VALID_TOPICS}")

    # Validate career_level array
    if not isinstance(result.career_level, list):
        raise ValueError(f"career_level must be a list, got {type(result.career_level)}")

    # Filter invalid career levels
    valid_levels = [level for level in result.career_level if level in VALID_CAREER_LEVELS]

    # If all levels were invalid, default to all levels
    if not valid_levels:
        valid_levels = VALID_CAREER_LEVELS.copy()

    result.career_level = valid_levels

    return result

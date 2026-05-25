"""Resume content classifier package.

Public API:
  - classify(input: ClassificationInput) -> ClassificationResult
  - classify_batch(inputs: list[ClassificationInput]) -> list[ClassificationResult]
"""

import logging

from .models import ClassificationInput, ClassificationResult
from .rules import classify_deterministic
from .llm_fallback import classify_with_llm
from .validator import validate_result

logger = logging.getLogger(__name__)

__all__ = ["classify", "classify_batch", "ClassificationInput", "ClassificationResult"]

def classify(input: ClassificationInput) -> ClassificationResult:
    """Classify a resume article snippet.

    Attempts deterministic classification first, falls back to LLM if ambiguous.
    Always returns validated output.

    Args:
        input: ClassificationInput with article text and optional hints

    Returns:
        ClassificationResult with title, topic, and career_level

    Raises:
        ValueError: If output cannot be validated
    """
    # Step 1: Try deterministic classification
    result = classify_deterministic(input)

    # Step 2: If ambiguous, try LLM
    if result is None:
        result = classify_with_llm(input)

    # Step 3: If both failed, raise error
    if result is None:
        raise ValueError("Could not classify article: both deterministic and LLM approaches failed")

    # Step 4: Always validate before returning
    result = validate_result(result)

    return result

def classify_batch(inputs: list[ClassificationInput]) -> list[ClassificationResult | None]:
    """Classify multiple articles.

    Args:
        inputs: List of ClassificationInput objects

    Returns:
        List of ClassificationResult objects in same order as inputs
    """
    results = []
    for input_item in inputs:
        try:
            result = classify(input_item)
            results.append(result)
        except ValueError:
            logger.warning("Classification failed for article", exc_info=False)
            results.append(None)

    return results

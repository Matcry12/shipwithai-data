import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import pytest
from scripts.classifier import classify, ClassificationInput, ClassificationResult
from scripts.classifier.title_extractor import extract_title, truncate_title
from scripts.classifier.rules import infer_topic, infer_career_levels, classify_deterministic
from scripts.classifier.validator import validate_result
from scripts.classifier.constants import VALID_TOPICS, VALID_CAREER_LEVELS

class TestTitleExtraction:
    """Test title extraction from various formats."""

    def test_h1_extraction(self):
        """Extract title from markdown H1."""
        text = "# My Resume Title\n\nBody text here."
        title = extract_title(text)
        assert title == "My Resume Title"

    def test_frontmatter_extraction(self):
        """Extract title from YAML frontmatter."""
        text = '---\ntitle: Frontmatter Title\n---\nBody'
        title = extract_title(text)
        assert title == "Frontmatter Title"

    def test_title_truncation(self):
        """Truncate long titles at word boundary."""
        long_title = "This is a very long title that exceeds the maximum character limit and should be truncated"
        truncated = truncate_title(long_title, max_length=80)
        assert len(truncated) <= 82  # Allow for "..."
        assert truncated.endswith("...")
        assert truncated[-4] != " "  # No space before "..."

    def test_no_title_returns_none(self):
        """Return None when no title found."""
        text = "Just some body text without a title."
        title = extract_title(text)
        assert title is None

    def test_empty_string_returns_none(self):
        """Return None for empty string."""
        title = extract_title("")
        assert title is None


class TestTopicInference:
    """Test topic classification from keywords."""

    def test_topic_from_folder_hint(self):
        """Folder hint takes priority."""
        result = infer_topic("generic text", folder_hint="github-portfolio")
        assert result == "github-portfolio"

    def test_topic_from_keywords(self):
        """Infer topic from article keywords."""
        text = "Learn how to build a GitHub portfolio that gets you hired. GitHub portfolio tips."
        topic = infer_topic(text)
        assert topic == "github-portfolio"

    def test_ats_optimization_keywords(self):
        """Detect ATS optimization from keywords."""
        text = "Optimize your resume for ATS systems and applicant tracking. ATS optimization tips."
        topic = infer_topic(text)
        assert topic == "ats-optimization"

    def test_no_matching_topic(self):
        """Return None if no topic keywords found."""
        text = "random text about something else entirely"
        topic = infer_topic(text)
        assert topic is None


class TestCareerLevelInference:
    """Test career level classification."""

    def test_entry_level_detection(self):
        """Detect entry-level keywords."""
        text = "Entry-level resume tips for recent graduates"
        levels = infer_career_levels(text)
        assert "entry" in levels

    def test_senior_level_detection(self):
        """Detect senior-level keywords."""
        text = "Resume tips for senior engineers and staff leads"
        levels = infer_career_levels(text)
        assert "senior" in levels

    def test_multi_level_match(self):
        """Match multiple applicable levels."""
        text = "Resume guide for junior to senior positions"
        levels = infer_career_levels(text)
        assert len(levels) >= 1

    def test_no_matching_level(self):
        """Return empty list if no level keywords found."""
        text = "generic article text"
        levels = infer_career_levels(text)
        assert levels == []


class TestDeterministicClassification:
    """Test deterministic (non-LLM) classification."""

    def test_full_deterministic_classification(self):
        """Classify when all fields are deterministic."""
        text = """# GitHub Portfolio Guide
        Learn how to build a GitHub portfolio that impresses senior engineers.
        GitHub portfolio tips for experienced developers with 7+ years in the field.
        """
        input_obj = ClassificationInput(text=text)
        result = classify_deterministic(input_obj)

        assert result is not None
        assert result.title == "GitHub Portfolio Guide"
        assert result.topic == "github-portfolio"
        assert "senior" in result.career_level

    def test_missing_title_returns_none(self):
        """Return None if title cannot be extracted."""
        text = "No title here. Just body text about GitHub portfolios."
        input_obj = ClassificationInput(text=text)
        result = classify_deterministic(input_obj)

        assert result is None

    def test_hint_passthrough(self):
        """Use provided hints without re-inference."""
        text = "generic text"
        input_obj = ClassificationInput(
            text=text,
            existing_title="Custom Title",
            existing_topic="career-gap",
            existing_career_levels=["senior", "executive"]
        )
        result = classify_deterministic(input_obj)

        assert result.title == "Custom Title"
        assert result.topic == "career-gap"
        assert result.career_level == ["senior", "executive"]


class TestValidation:
    """Test output validation and normalization."""

    def test_title_too_long_truncated(self):
        """Truncate titles exceeding max length."""
        result = ClassificationResult(
            title="This is a very long title that exceeds the maximum length allowed for titles in this system",
            topic="resume-basics",
            career_level=["entry"]
        )
        validated = validate_result(result)
        assert len(validated.title) <= 82  # 80 + "..."

    def test_invalid_topic_rejected(self):
        """Reject invalid topic."""
        result = ClassificationResult(
            title="Title",
            topic="invalid-topic",
            career_level=["entry"]
        )
        with pytest.raises(ValueError):
            validate_result(result)

    def test_invalid_career_level_filtered(self):
        """Filter invalid career levels."""
        result = ClassificationResult(
            title="Title",
            topic="resume-basics",
            career_level=["entry", "invalid-level", "senior"]
        )
        validated = validate_result(result)
        assert "entry" in validated.career_level
        assert "senior" in validated.career_level
        assert "invalid-level" not in validated.career_level

    def test_empty_career_levels_default_to_all(self):
        """Default to all levels if none provided."""
        result = ClassificationResult(
            title="Title",
            topic="resume-basics",
            career_level=[]
        )
        validated = validate_result(result)
        assert set(validated.career_level) == set(VALID_CAREER_LEVELS)


class TestPublicAPI:
    """Test the public classify() API."""

    def test_classify_with_deterministic_input(self):
        """Classify an article that can be deterministically classified."""
        text = """# How to Build a GitHub Portfolio
        GitHub portfolios are essential for software engineers.
        GitHub portfolio tips for senior-level engineers with 7+ years experience."""

        input_obj = ClassificationInput(text=text)
        result = classify(input_obj)

        assert isinstance(result, ClassificationResult)
        assert result.title == "How to Build a GitHub Portfolio"
        assert result.topic == "github-portfolio"
        assert "senior" in result.career_level
        assert result.confidence == "deterministic"

    def test_classify_returns_validated_output(self):
        """Ensure classify() always returns validated output."""
        text = "# Title\nContent about career gaps in your resume. Career gaps explained."
        input_obj = ClassificationInput(
            text=text,
            existing_career_levels=["entry"]
        )
        result = classify(input_obj)

        assert len(result.title) <= 82
        assert result.topic in VALID_TOPICS
        assert all(level in VALID_CAREER_LEVELS for level in result.career_level)

    def test_to_dict_method(self):
        """Test JSON serialization."""
        result = ClassificationResult(
            title="Test Title",
            topic="resume-basics",
            career_level=["entry", "mid"]
        )
        output = result.to_dict()

        assert output == {
            "title": "Test Title",
            "topic": "resume-basics",
            "career_level": ["entry", "mid"]
        }


if __name__ == "__main__":
    pytest.main([__file__, "-v"])

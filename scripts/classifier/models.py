from dataclasses import dataclass, field


@dataclass
class ClassificationInput:
    text: str
    source_url: str = ""
    source_domain: str = ""
    folder_hint: str = ""
    existing_title: str = ""
    existing_topic: str = ""
    existing_career_levels: list[str] = field(default_factory=list)


@dataclass
class ClassificationResult:
    title: str
    topic: str
    career_level: list[str]
    confidence: str = "deterministic"

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "topic": self.topic,
            "career_level": self.career_level,
        }

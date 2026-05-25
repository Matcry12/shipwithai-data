VALID_TOPICS: list[str] = [
    "resume-basics", "resume-formatting", "work-experience", "skills-section",
    "education-section", "projects-section", "github-portfolio",
    "open-source-contributions", "cover-letter", "linkedin-profile",
    "career-gap", "career-change", "salary-negotiation", "ats-optimization",
    "job-search-strategy", "interview-prep", "senior-level-resume",
    "executive-resume", "remote-work-resume",
]

VALID_CAREER_LEVELS: list[str] = ["entry", "mid", "senior", "executive"]
MAX_TITLE_LENGTH: int = 80

# Topic keyword patterns (extracted from existing code at scripts/02_extract_metadata.py:52-75)
TOPIC_KEYWORDS: dict = {
    "resume-basics": r"resume\s+(basics|fundamentals|essentials)",
    "resume-formatting": r"resume\s+(formatting|format|layout|structure)",
    "work-experience": r"(work\s+experience|employment|job\s+history|professional\s+experience)",
    "skills-section": r"(skills\s+section|skills\s+to\s+include)",
    "education-section": r"education\s+(section|background)",
    "projects-section": r"projects?\s+(section|portfolio)",
    "github-portfolio": r"(github\s+portfolio|github\s+profile)",
    "open-source-contributions": r"open\s+source",
    "cover-letter": r"cover\s+letter",
    "linkedin-profile": r"linkedin\s+(profile|resume)",
    "career-gap": r"career\s+(gap|gaps)",
    "career-change": r"career\s+(change|switching)",
    "salary-negotiation": r"(salary|compensation|negotiat)",
    "ats-optimization": r"(ATS|applicant\s+tracking|keyword\s+optim|ats\s+keyword|resume\s+optim)",
    "job-search-strategy": r"job\s+search",
    "interview-prep": r"(interview|interviewing|technical\s+interview)",
    "senior-level-resume": r"(senior|staff|lead|principal)",
    "executive-resume": r"(executive|director|VP|C-suite|leadership)",
    "remote-work-resume": r"(remote|work\s+from\s+home|distributed)",
}

# Career level keyword patterns (extracted from existing code at scripts/02_extract_metadata.py:79-88)
LEVEL_RULES: dict = {
    "entry": r"(entry-level|entry\s+level|junior|first\s+job|new\s+grad|recent\s+graduate)",
    "mid": r"(mid-level|mid\s+level|intermediate|2[-–]7\s+years)",
    "senior": r"(senior|staff|lead|7\+|7-\+|principal|architect)",
    "executive": r"(director|VP|C-suite|C-level|executive|president)",
}

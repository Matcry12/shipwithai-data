import re
from .constants import MAX_TITLE_LENGTH

def extract_title(text: str, max_length: int = MAX_TITLE_LENGTH) -> str | None:
    """Extract title from H1 heading or frontmatter. Return None if not found."""
    if not text:
        return None

    # Try H1 markdown heading (# Title)
    h1_match = re.search(r'^\s*#\s+(.+?)$', text, re.MULTILINE)
    if h1_match:
        title = h1_match.group(1).strip()
        return truncate_title(title, max_length)

    # Try YAML frontmatter
    frontmatter_match = re.search(r'^---\s*\n.*?title:\s*(.+?)$', text, re.MULTILINE | re.DOTALL)
    if frontmatter_match:
        title = frontmatter_match.group(1).strip()
        # Remove quotes if present
        title = re.sub(r'^["\']|["\']$', '', title)
        return truncate_title(title, max_length)

    return None

def truncate_title(title: str, max_length: int = MAX_TITLE_LENGTH) -> str:
    """Truncate title at word boundary if exceeds max_length."""
    if len(title) <= max_length:
        return title

    # Truncate and find last space
    truncated = title[:max_length]
    last_space = truncated.rfind(' ')

    if last_space > 0:
        truncated = truncated[:last_space]

    return truncated.rstrip() + "..."

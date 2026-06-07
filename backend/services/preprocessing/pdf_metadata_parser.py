import re
from typing import Dict, List, Optional


# -----------------------------
# Regex patterns (RBI-specific)
# -----------------------------

DATE_PATTERN = re.compile(
    r"(January|February|March|April|May|June|July|August|September|October|November|December)"
    r"\s+\d{1,2},\s+\d{4}"
)

CIRCULAR_NO_PATTERN = re.compile(
    r"RBI/\d{4}-\d{2}/\d+"
)

DEPARTMENT_PATTERN = re.compile(
    r"Department of ([A-Za-z ]+)"
)

RELATIONSHIP_PATTERNS = {
    "supersedes": r"in supersession of|supersedes",
    "amends": r"in partial modification of|amends",
    "withdraws": r"stands withdrawn|withdrawn",
}


# -----------------------------
# Core parser
# -----------------------------

def extract_pdf_metadata(pages: List[Dict]) -> Dict:
    """
    Extract metadata from RBI PDF pages.
    Input: [{page: int, text: str}]
    """

    if not pages:
        return {}

    first_text = "\n".join(p["text"] for p in pages[:2])

    title = extract_title(first_text)
    issue_date = extract_issue_date(first_text)
    circular_no = extract_circular_number(first_text)
    department = extract_department(first_text)
    relationships = detect_relationships(first_text)

    return {
        "title": title,
        "issue_date": issue_date,
        "circular_number": circular_no,
        "department": department,
        "relationships": relationships,
    }


# -----------------------------
# Individual extractors
# -----------------------------

def extract_title(text: str) -> Optional[str]:
    lines = [l.strip() for l in text.splitlines() if len(l.strip()) > 5]

    for line in lines[:10]:
        if any(k in line.upper() for k in ["MASTER", "CIRCULAR", "DIRECTION"]):
            return line.title()

    return None


def extract_issue_date(text: str) -> Optional[str]:
    match = DATE_PATTERN.search(text)
    return match.group(0) if match else None


def extract_circular_number(text: str) -> Optional[str]:
    match = CIRCULAR_NO_PATTERN.search(text)
    return match.group(0) if match else None


def extract_department(text: str) -> Optional[str]:
    match = DEPARTMENT_PATTERN.search(text)
    return match.group(1).strip() if match else None


def detect_relationships(text: str) -> List[str]:
    found = []
    for label, pattern in RELATIONSHIP_PATTERNS.items():
        if re.search(pattern, text, re.IGNORECASE):
            found.append(label)
    return found

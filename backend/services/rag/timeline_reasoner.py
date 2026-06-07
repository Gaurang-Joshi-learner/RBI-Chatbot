# app/services/rag/timeline_reasoner.py

from datetime import datetime
import re
from typing import List, Dict


DATE_FORMATS = [
    "%B %d, %Y",   # July 2, 2018
    "%d %B %Y",    # 2 July 2018
]


def parse_date(date_str: str | None) -> datetime | None:
    if not date_str:
        return None

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue

    return None


def detect_relationships(text: str) -> List[str]:
    patterns = {
        "supersedes": r"supersedes|in supersession of",
        "amends": r"amended by|in partial modification of",
        "withdraws": r"withdrawn|stands withdrawn",
    }

    relationships = []

    for label, pattern in patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            relationships.append(label)

    return relationships


def build_timeline(documents: List[Dict]) -> List[Dict]:
    """
    Takes grouped documents and returns them sorted with relationship info.
    """

    enriched = []

    for doc in documents:
        parsed_date = parse_date(doc.get("issue_date"))

        enriched.append({
            **doc,
            "parsed_date": parsed_date,
            "relationships": detect_relationships(doc.get("combined_text", "")),
        })

    # Sort oldest → newest
    enriched.sort(
        key=lambda d: d["parsed_date"] or datetime.min
    )

    return enriched

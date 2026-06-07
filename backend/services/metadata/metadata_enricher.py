import re
from datetime import datetime
from typing import Dict, List


# -----------------------------
# Department extraction
# -----------------------------
def extract_department(text: str) -> str | None:
    patterns = {
        "DBR": r"Department of Banking Regulation|DBR",
        "DEPR": r"Department of Economic.*Research|DEPR",
        "DPSS": r"Payment.*Settlement|DPSS",
        "DOS": r"Department of Supervision|DOS",
    }

    for dept, pattern in patterns.items():
        if re.search(pattern, text, re.IGNORECASE):
            return dept

    return None


# -----------------------------
# Subject category classification
# -----------------------------
def classify_subject(text: str) -> str:
    text_lower = text.lower()

    if "nbfc" in text_lower:
        return "NBFC"
    if "payment" in text_lower or "settlement" in text_lower:
        return "Payment Systems"
    if "bank" in text_lower or "deposit" in text_lower:
        return "Banking Regulation"
    if "kyc" in text_lower or "aml" in text_lower:
        return "KYC/AML"

    return "General Regulation"


# -----------------------------
# Key topics extraction
# -----------------------------
def extract_key_topics(text: str, max_topics: int = 8) -> List[str]:
    candidates = re.findall(r"\b[A-Z][a-zA-Z]{4,}\b", text)
    return list(dict.fromkeys(candidates))[:max_topics]


# -----------------------------
# Date extraction
# -----------------------------
def extract_dates(text: str) -> Dict[str, str | None]:
    issue_date = None
    effective_date = None

    issue_match = re.search(
        r"(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}",
        text
    )
    if issue_match:
        issue_date = issue_match.group(0)

    eff_match = re.search(
        r"(with effect from|effective from)\s+([A-Za-z]+\s+\d{1,2},\s+\d{4})",
        text,
        re.IGNORECASE
    )
    if eff_match:
        effective_date = eff_match.group(2)

    return {
        "issue_date": issue_date,
        "effective_date": effective_date
    }


# -----------------------------
# CORE metadata enricher (your original function)
# -----------------------------
def enrich_document_metadata(
    *,
    doc_id: str,
    title: str,
    full_text: str,
    document_type: str,
    source: str,
    url: str
) -> Dict:

    department = extract_department(full_text)
    subject_category = classify_subject(full_text)
    key_topics = extract_key_topics(full_text)
    dates = extract_dates(full_text)

    return {
        "doc_id": doc_id,
        "title": title,
        "document_type": document_type,
        "department": department,
        "subject_category": subject_category,
        "key_topics": key_topics,
        "issue_date": dates["issue_date"],
        "effective_date": dates["effective_date"],
        "source": source,
        "url": url,
        "ingested_at": datetime.utcnow().isoformat()
    }


# -----------------------------
# ✅ ADAPTER FUNCTION (THIS FIXES EVERYTHING)
# -----------------------------
def extract_metadata(
    *,
    doc_id: str,
    title: str,
    text: str,
    document_type: str,
    source: str,
    url: str
) -> Dict:
    """
    Adapter used by chunker / indexer / RAG pipeline
    """

    return enrich_document_metadata(
        doc_id=doc_id,
        title=title,
        full_text=text,
        document_type=document_type,
        source=source,
        url=url
    )

# app/services/rag/answer_confidence.py

import re
from typing import List, Dict


STOPWORDS = {
    "the", "is", "are", "for", "to", "of", "and", "a", "in", "on", "what",
    "about", "how", "does", "do", "this", "that", "it"
}


def tokenize(text: str) -> set:
    """
    Normalize and tokenize text
    """
    tokens = re.findall(r"[a-zA-Z]{3,}", text.lower())
    return {t for t in tokens if t not in STOPWORDS}


def compute_relevance_score(
    *,
    question: str,
    grouped_documents: List[Dict]
) -> float:
    """
    Returns a relevance score between 0 and 1
    """

    question_tokens = tokenize(question)
    if not question_tokens:
        return 0.0

    matched_tokens = set()

    for doc in grouped_documents:
        doc_text = doc.get("combined_text", "")
        doc_tokens = tokenize(doc_text)
        matched_tokens |= (question_tokens & doc_tokens)

    return len(matched_tokens) / len(question_tokens)


def is_answer_confident(
    *,
    question: str,
    grouped_documents: List[Dict],
    threshold: float = 0.35
) -> bool:
    """
    Determines if answer confidence is sufficient
    """

    score = compute_relevance_score(
        question=question,
        grouped_documents=grouped_documents
    )

    return score >= threshold

# app/services/context/topic_tracker.py

import re


TOPIC_KEYWORDS = {
    "KYC": ["kyc", "customer identification", "aml"],
    "ACCOUNTS": ["savings account", "current account", "deposit"],
    "NBFC": ["nbfc", "non banking"],
    "BONDS": ["bond", "relief savings bond", "sovereign gold bond"],
}


def detect_topic(question: str) -> str | None:
    q = question.lower()

    for topic, keywords in TOPIC_KEYWORDS.items():
        for kw in keywords:
            if kw in q:
                return topic

    return None


def is_followup(question: str) -> bool:
    """
    Detects pronoun-based or short followups
    """
    followups = [
        "what about",
        "and",
        "those",
        "these",
        "it",
        "them"
    ]

    q = question.lower()
    return any(q.startswith(f) or f in q for f in followups)

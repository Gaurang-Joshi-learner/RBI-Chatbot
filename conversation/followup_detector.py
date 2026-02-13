# app/services/conversation/followup_detector.py

FOLLOWUP_KEYWORDS = {
    "it", "that", "those", "these", "such", "what about", "and for",
    "does this", "do they", "is it applicable"
}


def is_followup(question: str) -> bool:
    q = question.lower()
    return any(k in q for k in FOLLOWUP_KEYWORDS)

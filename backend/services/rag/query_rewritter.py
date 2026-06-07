# app/services/rag/query_rewriter.py

from app.services.conversation.followup_detector import is_followup


def rewrite_query(
    *,
    question: str,
    previous_question: str | None,
    current_topic: str | None
) -> str:
    """
    Rewrites follow-up questions into full queries
    """

    # If not a follow-up → return as-is
    if not is_followup(question):
        return question

    # If no context → return as-is
    if not previous_question and not current_topic:
        return question

    # Case 1: Topic exists
    if current_topic:
        return f"What are the {current_topic.lower()} requirements for {question.replace('what about', '').strip()}?"

    # Case 2: Fallback to previous question
    return f"{previous_question} ({question})"

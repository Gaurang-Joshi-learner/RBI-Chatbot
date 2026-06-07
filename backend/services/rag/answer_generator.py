# app/services/rag/answer_generator.py

from typing import List, Dict


def generate_rag_answer(
    question: str,
    retrieved_chunks: List[Dict]
) -> Dict:
    """
    Simple extractive RAG answer generator (no LLM yet)
    """

    if not retrieved_chunks:
        return {
            "question": question,
            "answer": "The answer is not found in the provided RBI documents.",
            "sources": []
        }

    # Combine text
    answer_sentences = []
    sources = []

    for chunk in retrieved_chunks:
        text = chunk.get("text", "").strip()
        metadata = chunk.get("metadata", {})

        if text:
            answer_sentences.append(text)

        sources.append(
            f"{metadata.get('title')} | "
            f"{metadata.get('issue_date')} | "
            f"{metadata.get('source', 'RBI')}"
        )

    # Deduplicate
    answer_text = " ".join(dict.fromkeys(answer_sentences))
    sources = list(dict.fromkeys(sources))

    return {
        "question": question,
        "answer": answer_text,
        "sources": sources
    }

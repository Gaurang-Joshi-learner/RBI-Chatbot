# app/services/rag/timeline_answer_generator.py

from typing import List, Dict


def build_timeline_context(timeline_docs: List[Dict]) -> str:
    """
    Converts timeline documents into evolution-style context.
    """

    context_blocks = []

    for i, doc in enumerate(timeline_docs):
        if i == 0:
            prefix = "Initially"
        elif i == len(timeline_docs) - 1:
            prefix = "Currently"
        else:
            prefix = "Subsequently"

        block = f"""
{prefix} ({doc.get("issue_date", "Unknown date")}):
Title: {doc.get("title")}
Document Type: {doc.get("document_type", "Unknown")}
Department: {doc.get("department", "Unknown")}
Source: {doc.get("source", "RBI")}

Content:
{doc.get("combined_text")}
"""
        context_blocks.append(block.strip())

    return "\n\n".join(context_blocks)


def generate_timeline_answer(question: str, timeline_docs: List[Dict]) -> Dict:
    """
    Generates a structured timeline-based answer (LLM-ready).
    """

    context = build_timeline_context(timeline_docs)

    prompt = f"""
You are an expert RBI regulatory assistant.

Rules you MUST follow:
1. Answer ONLY using the provided RBI document context.
2. Explain changes over time clearly.
3. Do NOT use outside knowledge.
4. Cite document titles and issue dates.
5. If information is missing, say so explicitly.

Timeline Context:
{context}

Question:
{question}

Answer:
""".strip()

    sources = [
        f"{doc.get('title')} | {doc.get('issue_date')} | {doc.get('source', 'RBI')}"
        for doc in timeline_docs
    ]

    return {
        "question": question,
        "prompt": prompt,
        "sources": sources
    }

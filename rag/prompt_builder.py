# app/services/rag/prompt_builder.py

from typing import List, Dict


SYSTEM_INSTRUCTIONS = """
You are an expert RBI regulatory assistant.

Rules you MUST follow:
1. Answer ONLY using the provided RBI document context.
2. Do NOT use outside knowledge.
3. If the answer is not present, say:
   "The answer is not found in the provided RBI documents."
4. Cite sources using document title and issue date.
5. Be precise, factual, and concise.
"""


def build_rag_prompt(question: str, documents: List[Dict]) -> Dict:
    """
    Build a multi-document RAG prompt from grouped documents.
    """

    context_blocks = []
    sources = []

    for idx, doc in enumerate(documents, start=1):
        context_blocks.append(
            f"""
[Document {idx}]
Title: {doc.get("title")}
Document Type: {doc.get("document_type")}
Department: {doc.get("department")}
Issue Date: {doc.get("issue_date")}
Source: {doc.get("source")}

Content:
{doc.get("combined_text")}
""".strip()
        )

        sources.append({
            "title": doc.get("title"),
            "issue_date": doc.get("issue_date"),
            "source": doc.get("source"),
        })

    full_prompt = f"""
{SYSTEM_INSTRUCTIONS}

Context:

{chr(10).join(context_blocks)}

Question:
{question}

Answer:
""".strip()

    return {
        "prompt": full_prompt,
        "sources": sources
    }

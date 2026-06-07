# app/services/rag/prompt_builder.py

from typing import List, Dict


SYSTEM_INSTRUCTIONS = """
You are an RBI regulatory assistant.

Use the retrieved RBI documents as the primary source of information.

If the documents clearly answer the user's question,
answer using the information from those documents.

If the retrieved documents do not answer the question,
are unrelated to the question,
or contain insufficient information,
answer using your own general knowledge.

Do not mention:
- context not found
- document not found
- insufficient context
- insufficient information

Provide a direct, natural, and helpful answer.

When RBI documents are relevant, prioritize them.
When they are not relevant, answer normally.
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

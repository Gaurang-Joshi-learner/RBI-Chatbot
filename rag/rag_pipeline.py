# app/services/rag/rag_pipeline.py

from app.services.vectorstore.retriever import retrieve_similar_chunks
from app.services.rag.prompt_builder import build_rag_prompt
from app.services.llm.ollama_client import generate_with_ollama
from app.services.rag.doc_grouper import group_chunks_by_document


def run_rag_pipeline(question: str, topic: str | None = None) -> dict:
    """
    Hybrid RAG:
    - If RBI context exists → grounded answer
    - Else → normal LLM answer
    """

    retrieved_chunks = retrieve_similar_chunks(
        query=question,
        topic=topic,
        top_k=5
    )

    # ----------------------------
    # Case 1: No relevant RBI context found
    # ----------------------------
    if not retrieved_chunks:
        answer_text = generate_with_ollama(
            f"""
You are a helpful assistant.

Answer this question normally using your own knowledge:

Question: {question}

Answer:
"""
        )

        return {
            "answer": answer_text,
            "sources": [],
            "mode": "general"
        }

    # ----------------------------
    # Case 2: RBI context found → use RAG
    # ----------------------------
    documents = group_chunks_by_document(retrieved_chunks)

    prompt_payload = build_rag_prompt(
        question=question,
        documents=documents
    )

    answer_text = generate_with_ollama(prompt_payload["prompt"])

    return {
        "answer": answer_text,
        "sources": prompt_payload["sources"],
        "mode": "rbi"
    }

from app.services.vectorstore.retriever import retrieve_similar_chunks
from app.services.rag.prompt_builder import build_rag_prompt
from app.services.llm.ollama_client import generate_with_ollama
from app.services.rag.doc_grouper import group_chunks_by_document
import time


def generate_llm_answer(
    question: str,
    mode: str = "general"
) -> dict:

    prompt = f"""
You are a helpful assistant.

Answer naturally using your own knowledge.

Question:
{question}
"""
    llm_start = time.time()
    answer_text = generate_with_ollama(prompt)
    print(
    "LLM TIME:",
    time.time() - llm_start
)

    return {
        "answer": answer_text,
        "sources": [],
        "mode": mode
    }


def run_rag_pipeline(
    question: str,
    topic: str | None = None
) -> dict:
    start = time.time()
    retrieved_results = retrieve_similar_chunks(
        query=question,
        topic=topic,
        top_k=1
    )
    print(
    "RETRIEVAL TIME:",
    time.time() - start
)

    if not retrieved_results:
        return generate_llm_answer(
            question,
            mode="general"
        )

    best_score = retrieved_results[0]["score"]
    best_distance = retrieved_results[0]["distance"]

    print("BEST SCORE:", best_score)
    print("BEST DISTANCE:", best_distance)

    if best_distance > 1.0:
        return generate_llm_answer(
            question,
            mode="general"
        )

    retrieved_chunks = [
        r["record"]
        for r in retrieved_results
    ]

    documents = group_chunks_by_document(
        retrieved_chunks
    )

    prompt_payload = build_rag_prompt(
        question=question,
        documents=documents
    )

    answer_text = generate_with_ollama(
        prompt_payload["prompt"]
    )
    print(
    "TOTAL PIPELINE TIME:",
    time.time() - start
)
    return {
        "answer": answer_text,
        "sources": prompt_payload["sources"],
        "mode": "rbi"
    }
from fastapi import APIRouter
from app.services.rag.rag_pipeline import run_rag_pipeline

router = APIRouter(prefix="/ask", tags=["Ask"])


@router.post("/")
def ask_question(payload: dict):
    question = payload.get("question")
    topic = payload.get("topic")

    if not question:
        return {"error": "Question is required"}

    return run_rag_pipeline(question, topic)

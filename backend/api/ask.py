from fastapi import APIRouter
from app.services.rag.rag_pipeline import run_rag_pipeline
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.chat import ChatSession, Message
from app.core.auth import get_current_user

router = APIRouter(prefix="/ask", tags=["Ask"])


@router.post("/")
def ask_question(
    payload: dict,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    question = payload.get("question")
    topic = payload.get("topic")
    session_id = payload.get("session_id")
    print("SESSION ID RECEIVED:", session_id)

    if not question:
        return {"error": "Question is required"}

    # --------------------------------
    # USE EXISTING SESSION
    # --------------------------------

    if session_id:

        chat_session = db.query(ChatSession).filter(
            ChatSession.id == session_id
        ).first()

        if not chat_session:
            return {
                "error": "Session not found"
            }

    # --------------------------------
    # CREATE NEW SESSION
    # --------------------------------

    else:

        chat_session = ChatSession(
            title=question[:50],
             user_id=current_user["sub"]
            
        )

        db.add(chat_session)
        db.commit()
        db.refresh(chat_session)

    # --------------------------------
    # STORE USER MESSAGE
    # --------------------------------

    user_message = Message(
        session_id=chat_session.id,
        role="user",
        content=question
    )

    db.add(user_message)
    db.commit()

    # --------------------------------
    # GENERATE RESPONSE
    # --------------------------------

    response = run_rag_pipeline(
        question,
        topic
    )

    # --------------------------------
    # STORE ASSISTANT MESSAGE
    # --------------------------------

    assistant_message = Message(
        session_id=chat_session.id,
        role="assistant",
        content=response["answer"]
    )

    db.add(assistant_message)
    db.commit()

    # --------------------------------
    # RETURN RESPONSE
    # --------------------------------

    return {
        **response,
        "session_id": chat_session.id
    }
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.deps import get_db
from app.models.chat import ChatSession
from app.core.auth import get_current_user

router = APIRouter(
    prefix="/sessions",
    tags=["sessions"]
)


@router.get("/")
def get_sessions(
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    sessions = db.query(ChatSession).filter(
        ChatSession.user_id == current_user["sub"]
    ).order_by(
        ChatSession.created_at.desc()
    ).all()

    return sessions


@router.get("/{session_id}/messages")
def get_session_messages(
    session_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    session = db.query(ChatSession).filter(
        ChatSession.id == session_id,
        ChatSession.user_id == current_user["sub"]
    ).first()

    if not session:
        return {
            "error": "Session not found"
        }

    messages = []

    for message in session.messages:
        messages.append({
            "id": message.id,
            "role": message.role,
            "content": message.content,
            "created_at": message.created_at
        })

    return messages


@router.delete("/{session_id}")
def delete_session(
    session_id: int,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    session = db.query(ChatSession).filter(
        ChatSession.id == session_id,
        ChatSession.user_id == current_user["sub"]
    ).first()

    if not session:
        return {
            "error": "Session not found"
        }

    db.delete(session)
    db.commit()

    return {
        "message": "Session deleted"
    }
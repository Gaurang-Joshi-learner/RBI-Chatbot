from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DateTime,
    Text
)

from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.db.session import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class ChatSession(Base):

    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String, nullable=True)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )
    user_id = Column(
        Integer,
        ForeignKey("users.id")
    )

    user = relationship(
        "User",
        back_populates="sessions"
    )
    messages = relationship(
        "Message",
        back_populates="session",
        cascade="all, delete"
    )


class Message(Base):

    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)

    session_id = Column(
        Integer,
        ForeignKey("chat_sessions.id")
    )

    role = Column(String)

    content = Column(Text)

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    session = relationship(
        "ChatSession",
        back_populates="messages"
    )
from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime
)

from sqlalchemy.orm import relationship

from app.db.session import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        index=True
    )

    email = Column(
        String,
        unique=True,
        index=True
    )

    hashed_password = Column(
        String
    )

    otp = Column(
        String,
        nullable=True
    )

    otp_expiry = Column(
        DateTime,
        nullable=True
    )

    sessions = relationship(
        "ChatSession",
        back_populates="user"
    )
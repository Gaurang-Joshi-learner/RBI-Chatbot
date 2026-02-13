from sqlalchemy import Column, Integer, String, Date, ForeignKey, Enum
from sqlalchemy.sql import func
from sqlalchemy import DateTime
from app.db.base import Base
import enum

class DocumentStatus(enum.Enum):
    ACTIVE = "ACTIVE"
    SUPERSEDED = "SUPERSEDED"

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    circular_number = Column(String, unique=True, index=True)
    title = Column(String, nullable=False)
    issue_date = Column(Date)
    department = Column(String)
    document_type = Column(String)

    status = Column(Enum(DocumentStatus), default=DocumentStatus.ACTIVE)
    supersedes_document_id = Column(Integer, ForeignKey("documents.id"), nullable=True)

    pdf_path = Column(String)
    source_url = Column(String)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

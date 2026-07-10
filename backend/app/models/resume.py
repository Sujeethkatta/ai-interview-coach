"""
Resume database model.
"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

from app.db.base import Base


class Resume(Base):
    """
    Resume database model.
    """
    __tablename__ = "resumes"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    
    filename = Column(String(255), nullable=False)
    file_path = Column(String(255), nullable=False)
    file_type = Column(String(50), nullable=False)  # pdf, docx, txt
    file_size = Column(String(50), nullable=True)
    
    # Parsed data
    parsed_content = Column(JSONB, nullable=True)
    
    # Extracted information
    name = Column(String(255), nullable=True)
    email = Column(String(255), nullable=True)
    phone = Column(String(20), nullable=True)
    location = Column(String(255), nullable=True)
    summary = Column(Text, nullable=True)
    
    # Career information
    skills = Column(JSONB, nullable=True)  # List of skills
    experience = Column(JSONB, nullable=True)  # List of experiences
    education = Column(JSONB, nullable=True)  # List of education
    certifications = Column(JSONB, nullable=True)  # List of certifications
    
    # Analysis
    is_analyzed = Column(Boolean, default=False)
    analysis_score = Column(String(50), nullable=True)
    
    # Metadata
    is_primary = Column(Boolean, default=False)
    is_archived = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Resume {self.filename}>"

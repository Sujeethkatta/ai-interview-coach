"""
Feedback database model.
"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, Float, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import uuid

from app.db.base import Base


class Feedback(Base):
    """
    Feedback database model for storing AI-generated feedback.
    """
    __tablename__ = "feedback"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    answer_id = Column(UUID(as_uuid=True), ForeignKey("interview_answers.id"), nullable=False, index=True)
    interview_id = Column(UUID(as_uuid=True), ForeignKey("interviews.id"), nullable=False, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    
    # Scores
    content_score = Column(Float, nullable=True)  # 0-100
    delivery_score = Column(Float, nullable=True)  # 0-100
    confidence_score = Column(Float, nullable=True)  # 0-100
    overall_score = Column(Float, nullable=True)  # 0-100
    
    # Feedback
    strengths = Column(Text, nullable=True)
    areas_for_improvement = Column(Text, nullable=True)
    suggestions = Column(Text, nullable=True)
    detailed_feedback = Column(Text, nullable=True)
    
    # Analysis
    keyword_match = Column(Float, nullable=True)  # 0-100
    sentiment = Column(String(50), nullable=True)  # positive, neutral, negative
    
    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<Feedback {self.id}>"

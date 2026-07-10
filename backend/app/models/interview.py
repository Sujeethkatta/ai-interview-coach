"""
Interview-related database models.
"""
from datetime import datetime
from sqlalchemy import Column, String, Integer, Float, DateTime, Text, ForeignKey, Enum as SQLEnum, Boolean
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.orm import relationship
import uuid
import enum

from app.db.base import Base


class InterviewType(str, enum.Enum):
    """Interview type enumeration."""
    BEHAVIORAL = "behavioral"
    TECHNICAL = "technical"
    CODING = "coding"
    HR = "hr"
    CASE_STUDY = "case_study"


class DifficultyLevel(str, enum.Enum):
    """Difficulty level enumeration."""
    BEGINNER = "beginner"
    INTERMEDIATE = "intermediate"
    ADVANCED = "advanced"
    EXPERT = "expert"


class Interview(Base):
    """
    Interview database model.
    """
    __tablename__ = "interviews"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    interview_type = Column(SQLEnum(InterviewType), nullable=False)
    difficulty = Column(SQLEnum(DifficultyLevel), default=DifficultyLevel.INTERMEDIATE)
    category = Column(String(100), nullable=True, index=True)
    
    # Status
    is_completed = Column(Boolean, default=False)
    is_submitted = Column(Boolean, default=False)
    
    # Metadata
    duration_minutes = Column(Integer, nullable=True)
    score = Column(Float, nullable=True)  # 0-100
    feedback = Column(Text, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False, index=True)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    completed_at = Column(DateTime, nullable=True)
    
    def __repr__(self) -> str:
        return f"<Interview {self.title}>"


class InterviewQuestion(Base):
    """
    Interview question database model.
    """
    __tablename__ = "interview_questions"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    interview_id = Column(UUID(as_uuid=True), ForeignKey("interviews.id"), nullable=False, index=True)
    
    question = Column(Text, nullable=False)
    question_type = Column(String(50), nullable=True)  # text, coding, mcq, etc.
    expected_answer = Column(Text, nullable=True)
    question_index = Column(Integer, nullable=False)
    
    # For coding questions
    code_template = Column(Text, nullable=True)
    test_cases = Column(JSONB, nullable=True)
    
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __repr__(self) -> str:
        return f"<InterviewQuestion {self.question_index}>"


class InterviewAnswer(Base):
    """
    Interview answer database model.
    """
    __tablename__ = "interview_answers"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column(UUID(as_uuid=True), ForeignKey("interview_questions.id"), nullable=False, index=True)
    interview_id = Column(UUID(as_uuid=True), ForeignKey("interviews.id"), nullable=False, index=True)
    
    answer_text = Column(Text, nullable=True)
    code_answer = Column(Text, nullable=True)
    audio_url = Column(String(255), nullable=True)
    
    # Evaluation
    score = Column(Float, nullable=True)  # 0-100
    feedback = Column(Text, nullable=True)
    is_correct = Column(Boolean, nullable=True)
    
    # Metadata
    time_spent_seconds = Column(Integer, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<InterviewAnswer {self.id}>"

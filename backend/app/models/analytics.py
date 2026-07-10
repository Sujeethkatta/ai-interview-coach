"""
Analytics database model.
"""
from datetime import datetime
from sqlalchemy import Column, String, DateTime, ForeignKey, Float, Integer, Date
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid

from app.db.base import Base


class UserAnalytics(Base):
    """
    User analytics database model.
    """
    __tablename__ = "user_analytics"
    
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False, index=True)
    
    # Statistics
    total_interviews = Column(Integer, default=0)
    completed_interviews = Column(Integer, default=0)
    average_score = Column(Float, nullable=True)
    
    # Performance metrics
    best_score = Column(Float, nullable=True)
    worst_score = Column(Float, nullable=True)
    
    # Skills
    top_skills = Column(JSONB, nullable=True)  # List of top skills
    weak_skills = Column(JSONB, nullable=True)  # List of weak skills
    
    # Category performance
    category_performance = Column(JSONB, nullable=True)  # Dict of category: score
    
    # Trends
    weekly_stats = Column(JSONB, nullable=True)
    monthly_stats = Column(JSONB, nullable=True)
    
    # Date
    date = Column(Date, nullable=False, index=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __repr__(self) -> str:
        return f"<UserAnalytics {self.user_id}>"

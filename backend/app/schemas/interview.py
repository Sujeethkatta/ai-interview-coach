"""
Interview schemas.
"""
from pydantic import BaseModel
from typing import Optional


class InterviewCreate(BaseModel):
    """Interview creation schema."""
    title: Optional[str] = None
    interview_type: str
    difficulty: Optional[str] = "intermediate"
    category: Optional[str] = None
    description: Optional[str] = None


class InterviewResponse(BaseModel):
    """Interview response schema."""
    id: str
    title: str
    interview_type: str
    difficulty: str
    category: Optional[str] = None
    score: Optional[float] = None


class InterviewListResponse(BaseModel):
    """Interview list response schema."""
    total: int
    interviews: list[InterviewResponse]

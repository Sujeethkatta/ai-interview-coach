"""
Resume schemas.
"""
from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ResumeResponse(BaseModel):
    """Resume response schema."""
    id: str
    filename: str
    created_at: str
    is_primary: Optional[bool] = False


class ResumeListResponse(BaseModel):
    """Resume list response schema."""
    total: int
    resumes: list[ResumeResponse]

"""
Report endpoints.
"""
import logging
from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.interview import Interview
from app.models.feedback import Feedback

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/{interview_id}", response_model=dict[str, Any])
async def get_interview_report(
    interview_id: str,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    """
    Get interview report.
    
    Args:
        interview_id: Interview ID
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        Interview report
    """
    interview = db.query(Interview).filter(
        Interview.id == UUID(interview_id),
        Interview.user_id == UUID(current_user_id),
    ).first()
    
    if not interview:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Interview not found",
        )
    
    # Get feedback
    feedback = db.query(Feedback).filter(
        Feedback.interview_id == UUID(interview_id)
    ).all()
    
    return {
        "interview_id": str(interview.id),
        "title": interview.title,
        "interview_type": interview.interview_type.value,
        "score": interview.score,
        "feedback_count": len(feedback),
        "is_completed": interview.is_completed,
    }

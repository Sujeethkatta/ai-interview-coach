"""
Analytics endpoints.
"""
import logging
from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.interview import Interview
from app.models.analytics import UserAnalytics

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/dashboard", response_model=dict[str, Any])
async def get_analytics_dashboard(
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    """
    Get user analytics dashboard.
    
    Args:
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        Analytics dashboard data
    """
    # Get interview statistics
    total_interviews = db.query(Interview).filter(
        Interview.user_id == UUID(current_user_id)
    ).count()
    
    completed_interviews = db.query(Interview).filter(
        Interview.user_id == UUID(current_user_id),
        Interview.is_completed == True,
    ).count()
    
    # Calculate average score
    interviews = db.query(Interview).filter(
        Interview.user_id == UUID(current_user_id),
        Interview.score.isnot(None),
    ).all()
    
    average_score = (
        sum(i.score for i in interviews) / len(interviews)
        if interviews
        else 0
    )
    
    return {
        "total_interviews": total_interviews,
        "completed_interviews": completed_interviews,
        "average_score": average_score,
        "interviews": [
            {
                "id": str(i.id),
                "title": i.title,
                "type": i.interview_type.value,
                "score": i.score,
            }
            for i in interviews[:10]  # Last 10
        ],
    }

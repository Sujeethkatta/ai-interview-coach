"""
Interview endpoints.
"""
import logging
from typing import Any, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.interview import Interview, InterviewType, DifficultyLevel
from app.schemas.interview import InterviewCreate, InterviewResponse, InterviewListResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/start", response_model=InterviewResponse)
async def start_interview(
    request: InterviewCreate,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> InterviewResponse:
    """
    Start a new interview.
    
    Args:
        request: Interview creation request
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        Created interview
    """
    interview = Interview(
        user_id=UUID(current_user_id),
        title=request.title or f"{request.interview_type.value} Interview",
        interview_type=request.interview_type,
        difficulty=request.difficulty or DifficultyLevel.INTERMEDIATE,
        category=request.category,
        description=request.description,
    )
    
    db.add(interview)
    db.commit()
    db.refresh(interview)
    
    logger.info(f"Interview started: {interview.id}")
    
    return InterviewResponse(
        id=str(interview.id),
        title=interview.title,
        interview_type=interview.interview_type.value,
        difficulty=interview.difficulty.value,
        category=interview.category,
    )


@router.get("/list", response_model=InterviewListResponse)
async def list_interviews(
    skip: int = 0,
    limit: int = 20,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> InterviewListResponse:
    """
    List user's interviews.
    
    Args:
        skip: Skip count
        limit: Limit count
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        List of interviews
    """
    interviews = db.query(Interview).filter(
        Interview.user_id == UUID(current_user_id)
    ).offset(skip).limit(limit).all()
    
    total = db.query(Interview).filter(
        Interview.user_id == UUID(current_user_id)
    ).count()
    
    return InterviewListResponse(
        total=total,
        interviews=[
            InterviewResponse(
                id=str(i.id),
                title=i.title,
                interview_type=i.interview_type.value,
                difficulty=i.difficulty.value,
                category=i.category,
                score=i.score,
            )
            for i in interviews
        ],
    )


@router.get("/{interview_id}", response_model=InterviewResponse)
async def get_interview(
    interview_id: str,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> InterviewResponse:
    """
    Get interview details.
    
    Args:
        interview_id: Interview ID
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        Interview details
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
    
    return InterviewResponse(
        id=str(interview.id),
        title=interview.title,
        interview_type=interview.interview_type.value,
        difficulty=interview.difficulty.value,
        category=interview.category,
        score=interview.score,
    )

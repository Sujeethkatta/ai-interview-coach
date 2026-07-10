"""
Resume endpoints.
"""
import logging
from typing import Any
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File
from sqlalchemy.orm import Session

from app.core.security import get_current_user
from app.db.session import get_db
from app.models.resume import Resume
from app.schemas.resume import ResumeResponse, ResumeListResponse

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/upload", response_model=ResumeResponse)
async def upload_resume(
    file: UploadFile = File(...),
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ResumeResponse:
    """
    Upload a resume.
    
    Args:
        file: Resume file
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        Uploaded resume info
    """
    # Create resume record
    resume = Resume(
        user_id=UUID(current_user_id),
        filename=file.filename or "resume",
        file_path=f"resumes/{current_user_id}/{file.filename}",
        file_type=file.filename.split(".")[-1] if file.filename else "pdf",
    )
    
    db.add(resume)
    db.commit()
    db.refresh(resume)
    
    logger.info(f"Resume uploaded: {resume.id}")
    
    return ResumeResponse(
        id=str(resume.id),
        filename=resume.filename,
        created_at=resume.created_at.isoformat(),
    )


@router.get("/list", response_model=ResumeListResponse)
async def list_resumes(
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> ResumeListResponse:
    """
    List user's resumes.
    
    Args:
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        List of resumes
    """
    resumes = db.query(Resume).filter(
        Resume.user_id == UUID(current_user_id),
        Resume.is_archived == False,
    ).all()
    
    return ResumeListResponse(
        total=len(resumes),
        resumes=[
            ResumeResponse(
                id=str(r.id),
                filename=r.filename,
                created_at=r.created_at.isoformat(),
                is_primary=r.is_primary,
            )
            for r in resumes
        ],
    )

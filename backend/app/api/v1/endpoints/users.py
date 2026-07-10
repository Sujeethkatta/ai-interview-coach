"""
User endpoints.
"""
import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import get_current_user, hash_password
from app.db.session import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UserUpdate

logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/profile", response_model=UserResponse)
async def get_profile(
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> UserResponse:
    """
    Get user profile.
    
    Args:
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        User profile
    """
    user = db.query(User).filter(User.id == current_user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    return UserResponse(
        id=str(user.id),
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        bio=user.bio,
        is_verified=user.is_verified,
    )


@router.put("/profile", response_model=UserResponse)
async def update_profile(
    update_data: UserUpdate,
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> UserResponse:
    """
    Update user profile.
    
    Args:
        update_data: Update data
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        Updated user profile
    """
    user = db.query(User).filter(User.id == current_user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    # Update fields
    if update_data.full_name:
        user.full_name = update_data.full_name
    if update_data.bio is not None:
        user.bio = update_data.bio
    
    db.commit()
    db.refresh(user)
    
    logger.info(f"User profile updated: {user.email}")
    
    return UserResponse(
        id=str(user.id),
        email=user.email,
        username=user.username,
        full_name=user.full_name,
        bio=user.bio,
        is_verified=user.is_verified,
    )

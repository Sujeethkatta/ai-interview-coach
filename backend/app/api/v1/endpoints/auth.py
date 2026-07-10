"""
Authentication endpoints.
"""
import logging
from datetime import timedelta
from typing import Any

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.auth import TokenResponse, LoginRequest, RegisterRequest
from app.core.security import (
    hash_password,
    verify_password,
    create_access_token,
    get_current_user,
)
from app.db.session import get_db
from app.models.user import User
from app.core.config import settings

logger = logging.getLogger(__name__)

router = APIRouter()


@router.post("/register", response_model=dict[str, Any])
async def register(
    request: RegisterRequest,
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    """
    Register a new user.
    
    Args:
        request: Registration request
        db: Database session
        
    Returns:
        Registration response with user info
    """
    # Check if user exists
    existing_user = db.query(User).filter(
        (User.email == request.email) | (User.username == request.username)
    ).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email or username already exists",
        )
    
    # Create new user
    user = User(
        email=request.email,
        username=request.username,
        full_name=request.full_name or request.username,
        hashed_password=hash_password(request.password),
    )
    
    db.add(user)
    db.commit()
    db.refresh(user)
    
    logger.info(f"User registered: {user.email}")
    
    return {
        "message": "User registered successfully",
        "user_id": str(user.id),
        "email": user.email,
    }


@router.post("/login", response_model=TokenResponse)
async def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
) -> TokenResponse:
    """
    User login.
    
    Args:
        request: Login request
        db: Database session
        
    Returns:
        Access token
    """
    # Find user
    user = db.query(User).filter(User.email == request.email).first()
    
    if not user or not verify_password(request.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )
    
    if not user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive",
        )
    
    # Create token
    access_token = create_access_token(
        subject=user.id,
        expires_delta=timedelta(hours=settings.JWT_EXPIRATION_HOURS),
    )
    
    logger.info(f"User logged in: {user.email}")
    
    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
    )


@router.get("/me", response_model=dict[str, Any])
async def get_me(
    current_user_id: str = Depends(get_current_user),
    db: Session = Depends(get_db),
) -> dict[str, Any]:
    """
    Get current user info.
    
    Args:
        current_user_id: Current user ID
        db: Database session
        
    Returns:
        User info
    """
    user = db.query(User).filter(User.id == current_user_id).first()
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found",
        )
    
    return {
        "id": str(user.id),
        "email": user.email,
        "username": user.username,
        "full_name": user.full_name,
        "bio": user.bio,
    }

"""
User schemas.
"""
from pydantic import BaseModel, EmailStr
from datetime import datetime


class UserResponse(BaseModel):
    """User response schema."""
    id: str
    email: EmailStr
    username: str
    full_name: str | None = None
    bio: str | None = None
    is_verified: bool = False


class UserUpdate(BaseModel):
    """User update schema."""
    full_name: str | None = None
    bio: str | None = None

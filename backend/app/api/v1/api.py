"""
API v1 router configuration.
"""
from fastapi import APIRouter
from app.api.v1.endpoints import auth, users, interviews, resumes, reports, analytics

api_router = APIRouter()

# Include endpoint routers
api_router.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"],
)
api_router.include_router(
    users.router,
    prefix="/users",
    tags=["users"],
)
api_router.include_router(
    interviews.router,
    prefix="/interviews",
    tags=["interviews"],
)
api_router.include_router(
    resumes.router,
    prefix="/resumes",
    tags=["resumes"],
)
api_router.include_router(
    reports.router,
    prefix="/reports",
    tags=["reports"],
)
api_router.include_router(
    analytics.router,
    prefix="/analytics",
    tags=["analytics"],
)

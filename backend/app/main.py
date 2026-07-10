"""
Main FastAPI application factory and configuration.
"""
import logging
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging_config import setup_logging
from app.api.v1.api import api_router

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Lifespan context manager for startup and shutdown events.
    """
    # Startup
    logger.info("Application starting up...")
    logger.info(f"Environment: {settings.ENVIRONMENT}")
    logger.info(f"Debug: {settings.DEBUG}")
    
    yield
    
    # Shutdown
    logger.info("Application shutting down...")


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    
    Returns:
        FastAPI: Configured FastAPI application instance
    """
    # Setup logging
    setup_logging()
    
    # Create app
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description="AI-powered Interview Coach Application",
        version=settings.VERSION,
        docs_url="/docs",
        redoc_url="/redoc",
        openapi_url="/openapi.json",
        lifespan=lifespan,
    )
    
    # CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    
    # Trusted host middleware
    app.add_middleware(
        TrustedHostMiddleware,
        allowed_hosts=settings.ALLOWED_HOSTS
    )
    
    # Include routers
    app.include_router(
        api_router,
        prefix=settings.API_V1_STR,
    )
    
    # Health check endpoint
    @app.get("/health")
    async def health_check() -> dict[str, Any]:
        """Health check endpoint."""
        return {
            "status": "healthy",
            "version": settings.VERSION,
        }
    
    # Root endpoint
    @app.get("/")
    async def root() -> dict[str, str]:
        """Root endpoint."""
        return {
            "message": "Welcome to AI Interview Coach API",
            "docs": "/docs",
            "redoc": "/redoc",
        }
    
    # Exception handlers
    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Any, exc: Exception
    ) -> JSONResponse:
        """Global exception handler."""
        logger.error(
            f"Unhandled exception: {exc}",
            exc_info=True
        )
        return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )
    
    logger.info("FastAPI application created successfully")
    return app


app = create_app()


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.DEBUG,
        log_level="info",
    )

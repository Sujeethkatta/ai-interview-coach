"""
Application configuration using Pydantic settings.
"""
from typing import Any
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application settings from environment variables.
    """
    # Project
    PROJECT_NAME: str = "AI Interview Coach"
    VERSION: str = "1.0.0"
    API_V1_STR: str = "/api/v1"
    DEBUG: bool = False
    ENVIRONMENT: str = "development"
    
    # Server
    ALLOWED_HOSTS: list[str] = ["localhost", "127.0.0.1"]
    CORS_ORIGINS: list[str] = [
        "http://localhost:3000",
        "http://localhost:8000",
    ]
    
    # Database
    DATABASE_URL: str = (
        "postgresql://interview_coach:secure_password@localhost:5432/interview_coach"
    )
    SQLALCHEMY_ECHO: bool = False
    
    # Redis
    REDIS_URL: str = "redis://localhost:6379/0"
    
    # JWT
    JWT_SECRET_KEY: str = "your-secret-key-change-in-production"
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRATION_HOURS: int = 24
    
    # OAuth2
    GOOGLE_CLIENT_ID: str = ""
    GOOGLE_CLIENT_SECRET: str = ""
    GITHUB_CLIENT_ID: str = ""
    GITHUB_CLIENT_SECRET: str = ""
    
    # Email
    SMTP_HOST: str = "smtp.gmail.com"
    SMTP_PORT: int = 587
    SMTP_USER: str = ""
    SMTP_PASSWORD: str = ""
    FROM_EMAIL: str = "noreply@interviewcoach.ai"
    
    # AI/ML
    OLLAMA_API_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama2"
    HUGGINGFACE_API_KEY: str = ""
    
    # Vector DB
    CHROMA_PERSIST_DIR: str = "./chroma_data"
    FAISS_INDEX_PATH: str = "./faiss_index"
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    
    # File Upload
    MAX_UPLOAD_SIZE: int = 10 * 1024 * 1024  # 10MB
    UPLOAD_DIR: str = "./uploads"
    ALLOWED_EXTENSIONS: set[str] = {"pdf", "doc", "docx", "txt"}
    
    # Audio
    AUDIO_UPLOAD_DIR: str = "./audio_uploads"
    MAX_AUDIO_SIZE: int = 50 * 1024 * 1024  # 50MB
    ALLOWED_AUDIO_FORMATS: set[str] = {"mp3", "wav", "m4a", "webm"}
    
    # Pagination
    DEFAULT_PAGE_SIZE: int = 20
    MAX_PAGE_SIZE: int = 100
    
    # API Rate Limiting
    RATE_LIMIT_ENABLED: bool = True
    RATE_LIMIT_REQUESTS: int = 100
    RATE_LIMIT_PERIOD: int = 60  # seconds
    
    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()

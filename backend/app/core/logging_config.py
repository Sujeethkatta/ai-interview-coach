"""
Logging configuration for the application.
"""
import logging
import logging.config
from pathlib import Path
from pythonjsonlogger import jsonlogger


def setup_logging() -> None:
    """
    Setup logging configuration for the application.
    """
    # Create logs directory
    logs_dir = Path("logs")
    logs_dir.mkdir(exist_ok=True)
    
    # Configure logging
    logging_config = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": (
                    "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                ),
            },
            "json": {
                "class": "pythonjsonlogger.jsonlogger.JsonFormatter",
                "format": (
                    "%(asctime)s %(name)s %(levelname)s %(message)s"
                ),
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "INFO",
                "formatter": "default",
                "stream": "ext://sys.stdout",
            },
            "file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "INFO",
                "formatter": "json",
                "filename": "logs/app.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 10,
            },
            "error_file": {
                "class": "logging.handlers.RotatingFileHandler",
                "level": "ERROR",
                "formatter": "json",
                "filename": "logs/error.log",
                "maxBytes": 10485760,  # 10MB
                "backupCount": 10,
            },
        },
        "root": {
            "level": "INFO",
            "handlers": ["console", "file", "error_file"],
        },
        "loggers": {
            "uvicorn": {
                "level": "INFO",
                "handlers": ["console", "file"],
            },
            "uvicorn.access": {
                "level": "INFO",
                "handlers": ["console", "file"],
            },
            "sqlalchemy": {
                "level": "WARNING",
                "handlers": ["console"],
            },
        },
    }
    
    logging.config.dictConfig(logging_config)

"""
File handling utilities.
"""
import logging
from pathlib import Path
from typing import Optional
import shutil

logger = logging.getLogger(__name__)


class FileHandler:
    """
    File handling utilities.
    """

    @staticmethod
    def save_upload_file(file_content: bytes, filename: str, upload_dir: str) -> Optional[str]:
        """
        Save uploaded file.

        Args:
            file_content: File content
            filename: Original filename
            upload_dir: Upload directory

        Returns:
            File path or None
        """
        try:
            upload_path = Path(upload_dir)
            upload_path.mkdir(parents=True, exist_ok=True)
            
            file_path = upload_path / filename
            with open(file_path, 'wb') as f:
                f.write(file_content)
            
            logger.info(f"File saved: {file_path}")
            return str(file_path)
        except Exception as e:
            logger.error(f"Error saving file: {e}")
            return None

    @staticmethod
    def delete_file(file_path: str) -> bool:
        """
        Delete a file.

        Args:
            file_path: Path to file

        Returns:
            Success status
        """
        try:
            path = Path(file_path)
            if path.exists():
                path.unlink()
                logger.info(f"File deleted: {file_path}")
                return True
            return False
        except Exception as e:
            logger.error(f"Error deleting file: {e}")
            return False

    @staticmethod
    def get_file_size(file_path: str) -> Optional[int]:
        """
        Get file size in bytes.

        Args:
            file_path: Path to file

        Returns:
            File size or None
        """
        try:
            return Path(file_path).stat().st_size
        except Exception:
            return None

    @staticmethod
    def get_file_extension(filename: str) -> Optional[str]:
        """
        Get file extension.

        Args:
            filename: Filename

        Returns:
            Extension (without dot) or None
        """
        try:
            return filename.split('.')[-1].lower()
        except Exception:
            return None

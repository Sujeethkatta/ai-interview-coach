"""
Validation utilities.
"""
import logging
from typing import Optional
import re

logger = logging.getLogger(__name__)


class Validator:
    """
    Validation utilities.
    """

    @staticmethod
    def validate_email(email: str) -> bool:
        """
        Validate email format.

        Args:
            email: Email address

        Returns:
            True if valid
        """
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))

    @staticmethod
    def validate_password(password: str) -> bool:
        """
        Validate password strength.

        Args:
            password: Password

        Returns:
            True if strong enough
        """
        # At least 8 characters, 1 uppercase, 1 lowercase, 1 digit
        if len(password) < 8:
            return False
        if not re.search(r'[A-Z]', password):
            return False
        if not re.search(r'[a-z]', password):
            return False
        if not re.search(r'\d', password):
            return False
        return True

    @staticmethod
    def validate_username(username: str) -> bool:
        """
        Validate username format.

        Args:
            username: Username

        Returns:
            True if valid
        """
        # 3-50 characters, alphanumeric and underscore
        pattern = r'^[a-zA-Z0-9_]{3,50}$'
        return bool(re.match(pattern, username))

    @staticmethod
    def validate_file_extension(filename: str, allowed_extensions: set[str]) -> bool:
        """
        Validate file extension.

        Args:
            filename: Filename
            allowed_extensions: Set of allowed extensions

        Returns:
            True if valid
        """
        ext = filename.split('.')[-1].lower()
        return ext in allowed_extensions

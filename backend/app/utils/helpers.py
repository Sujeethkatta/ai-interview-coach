"""
Helper functions.
"""
import logging
from typing import Any, Optional
import json
from datetime import datetime

logger = logging.getLogger(__name__)


class Helpers:
    """
    Helper functions.
    """

    @staticmethod
    def safe_json_loads(json_str: str) -> Optional[dict[str, Any]]:
        """
        Safely load JSON string.

        Args:
            json_str: JSON string

        Returns:
            Parsed JSON or None
        """
        try:
            return json.loads(json_str)
        except Exception as e:
            logger.error(f"JSON parse error: {e}")
            return None

    @staticmethod
    def safe_json_dumps(obj: Any) -> Optional[str]:
        """
        Safely dump object to JSON string.

        Args:
            obj: Object to dump

        Returns:
            JSON string or None
        """
        try:
            return json.dumps(obj, default=str)
        except Exception as e:
            logger.error(f"JSON dump error: {e}")
            return None

    @staticmethod
    def format_datetime(dt: datetime) -> str:
        """
        Format datetime to ISO string.

        Args:
            dt: Datetime object

        Returns:
            ISO format string
        """
        try:
            return dt.isoformat()
        except Exception:
            return ""

    @staticmethod
    def paginate(
        items: list[Any],
        page: int = 1,
        page_size: int = 20,
    ) -> dict[str, Any]:
        """
        Paginate a list.

        Args:
            items: List of items
            page: Page number (1-indexed)
            page_size: Items per page

        Returns:
            Pagination result
        """
        total = len(items)
        start = (page - 1) * page_size
        end = start + page_size
        
        return {
            "total": total,
            "page": page,
            "page_size": page_size,
            "total_pages": (total + page_size - 1) // page_size,
            "items": items[start:end],
        }

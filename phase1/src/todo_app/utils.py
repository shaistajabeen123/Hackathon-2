"""
Utility functions for the Console Todo App.
"""
import uuid


def is_valid_uuid(val):
    """
    Check if a value is a valid UUID.
    """
    try:
        uuid.UUID(str(val))
        return True
    except ValueError:
        return False


def validate_uuid_format(item_id: str) -> bool:
    """
    Validate that the given string is in a valid UUID format.

    Args:
        item_id: The ID to validate

    Returns:
        True if the ID is a valid UUID, False otherwise
    """
    return is_valid_uuid(item_id)
"""
Domain-specific exceptions for the Console Todo App.
"""


class TodoNotFoundError(Exception):
    """Raised when a requested todo item is not found."""
    pass


class InvalidTodoError(Exception):
    """Raised when a todo item is invalid."""
    pass


class EmptyTitleError(ValueError):
    """Raised when a todo title is empty or contains only whitespace."""
    pass
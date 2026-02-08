"""
Data Transfer Objects for the Console Todo App.
Used for transferring data between application layers.
"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class TodoItemDTO:
    """DTO for transferring todo data between application layers."""
    id: str
    title: str
    description: str
    priority: int
    completed: bool
    created_at: str  # ISO format string

    @classmethod
    def from_domain(cls, todo_item):
        """Create a DTO from a domain TodoItem."""
        return cls(
            id=todo_item.id,
            title=todo_item.title,
            description=todo_item.description,
            priority=todo_item.priority,
            completed=todo_item.completed,
            created_at=todo_item.created_at.isoformat()
        )


@dataclass
class CreateTodoRequest:
    """DTO for requests to create a new todo."""
    title: str
    description: str = ""
    priority: int = 1


@dataclass
class UpdateTodoRequest:
    """DTO for requests to update an existing todo."""
    id: str
    title: str


@dataclass
class UpdateTodoDetailsRequest:
    """DTO for requests to update a todo's description and priority."""
    id: str
    description: str = ""
    priority: int = None


@dataclass
class ToggleCompleteRequest:
    """DTO for requests to mark a todo as complete/incomplete."""
    id: str
    completed: bool
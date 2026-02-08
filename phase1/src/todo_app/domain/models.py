"""
Domain models for the Console Todo App.
Contains the TodoItem and TodoList entities.
"""
import uuid
from datetime import datetime
from typing import Dict, List, Optional


class TodoItem:
    """Represents a single task in the todo list."""

    MAX_TITLE_LENGTH = 500  # Maximum length for a todo title
    MAX_DESCRIPTION_LENGTH = 2000  # Maximum length for a todo description

    def __init__(self, title: str, description: Optional[str] = None, priority: int = 1, item_id: Optional[str] = None):
        if not title or not title.strip():
            raise ValueError("Todo title cannot be empty")

        if len(title) > self.MAX_TITLE_LENGTH:
            raise ValueError(f"Todo title exceeds maximum length of {self.MAX_TITLE_LENGTH} characters")

        if priority < 1 or priority > 5:
            raise ValueError("Priority must be between 1 and 5")

        self.id = item_id or str(uuid.uuid4())
        self.title = title.strip()
        self.description = description.strip() if description else ""
        self.priority = priority
        self.completed = False
        self.created_at = datetime.now()

    def mark_complete(self):
        """Mark the todo item as complete."""
        self.completed = True

    def mark_incomplete(self):
        """Mark the todo item as incomplete."""
        self.completed = False

    def update_title(self, new_title: str):
        """Update the title of the todo item."""
        if not new_title or not new_title.strip():
            raise ValueError("Todo title cannot be empty")

        if len(new_title) > self.MAX_TITLE_LENGTH:
            raise ValueError(f"Todo title exceeds maximum length of {self.MAX_TITLE_LENGTH} characters")

        self.title = new_title.strip()

    def update_description(self, new_description: str):
        """Update the description of the todo item."""
        if new_description and len(new_description) > self.MAX_DESCRIPTION_LENGTH:
            raise ValueError(f"Todo description exceeds maximum length of {self.MAX_DESCRIPTION_LENGTH} characters")

        self.description = new_description.strip() if new_description else ""

    def update_priority(self, new_priority: int):
        """Update the priority of the todo item."""
        if new_priority < 1 or new_priority > 5:
            raise ValueError("Priority must be between 1 and 5")

        self.priority = new_priority

    def to_dict(self):
        """Convert the todo item to a dictionary."""
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "completed": self.completed,
            "created_at": self.created_at.isoformat()
        }


class TodoList:
    """Represents a collection of TodoItem objects."""
    
    def __init__(self):
        self.items: Dict[str, TodoItem] = {}

    def add_item(self, title: str, description: Optional[str] = None, priority: int = 1) -> str:
        """Add a new todo item to the list and return its ID."""
        item = TodoItem(title, description, priority)
        self.items[item.id] = item
        return item.id

    def get_all_items(self) -> List[TodoItem]:
        """Return all items in the list."""
        return list(self.items.values())

    def get_item(self, item_id: str) -> Optional[TodoItem]:
        """Return a specific item by ID."""
        return self.items.get(item_id)

    def update_item(self, item_id: str, title: str) -> bool:
        """Update the title of an existing item."""
        item = self.items.get(item_id)
        if not item:
            return False

        item.update_title(title)
        return True

    def update_item_details(self, item_id: str, description: str = None, priority: int = None) -> bool:
        """Update the description and/or priority of an existing item."""
        item = self.items.get(item_id)
        if not item:
            return False

        if description is not None:
            item.update_description(description)

        if priority is not None:
            item.update_priority(priority)

        return True

    def delete_item(self, item_id: str) -> bool:
        """Remove an item from the list."""
        if item_id in self.items:
            del self.items[item_id]
            return True
        return False

    def mark_complete(self, item_id: str) -> bool:
        """Mark an item as complete."""
        item = self.items.get(item_id)
        if item:
            item.mark_complete()
            return True
        return False

    def mark_incomplete(self, item_id: str) -> bool:
        """Mark an item as incomplete."""
        item = self.items.get(item_id)
        if item:
            item.mark_incomplete()
            return True
        return False
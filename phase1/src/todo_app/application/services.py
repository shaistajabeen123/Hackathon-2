"""
Application services for the Console Todo App.
Coordinates business operations and orchestrates domain models.
"""
from typing import List
from todo_app.domain.models import TodoList, TodoItem
from todo_app.application.dtos import (
    TodoItemDTO, CreateTodoRequest, UpdateTodoRequest, ToggleCompleteRequest, UpdateTodoDetailsRequest
)


class TodoAppService:
    """Main application service for todo operations."""
    
    def __init__(self, todo_list: TodoList):
        self.todo_list = todo_list

    def add_todo(self, request: CreateTodoRequest) -> str:
        """Add a new todo item."""
        return self.todo_list.add_item(request.title, request.description, request.priority)

    def get_todos(self) -> List[TodoItemDTO]:
        """Get all todo items."""
        items = self.todo_list.get_all_items()
        return [TodoItemDTO.from_domain(item) for item in items]

    def update_todo(self, request: UpdateTodoRequest) -> bool:
        """Update an existing todo item."""
        return self.todo_list.update_item(request.id, request.title)

    def update_todo_details(self, request: UpdateTodoDetailsRequest) -> bool:
        """Update the description and/or priority of an existing todo item."""
        return self.todo_list.update_item_details(request.id, request.description, request.priority)

    def delete_todo(self, item_id: str) -> bool:
        """Delete a todo item."""
        return self.todo_list.delete_item(item_id)

    def toggle_completion(self, request: ToggleCompleteRequest) -> bool:
        """Toggle the completion status of a todo item."""
        if request.completed:
            return self.todo_list.mark_complete(request.id)
        else:
            return self.todo_list.mark_incomplete(request.id)
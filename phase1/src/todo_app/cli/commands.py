"""
CLI command handlers for the Console Todo App.
"""
import sys
from typing import List, Optional
from todo_app.domain.exceptions import TodoNotFoundError
from todo_app.domain.models import TodoList
from todo_app.application.services import TodoAppService
from todo_app.application.dtos import (
    CreateTodoRequest, UpdateTodoRequest, ToggleCompleteRequest, UpdateTodoDetailsRequest
)


class TodoCommandHandler:
    """Handles CLI commands for todo operations."""
    
    def __init__(self, app_service: TodoAppService):
        self.app_service = app_service

    def handle_add(self, args: List[str]) -> str:
        """Handle the 'add' command."""
        if len(args) < 2:
            return "Error: Missing todo title. Usage: add \"todo title\" [\"description\"] [priority]"

        title = args[1]
        description = args[2] if len(args) > 2 else ""
        priority = int(args[3]) if len(args) > 3 and args[3].isdigit() else 1

        # Validate priority range
        if priority < 1 or priority > 5:
            priority = 1  # Default to 1 if invalid

        if not title.strip():
            return "Error: Todo title cannot be empty"

        try:
            item_id = self.app_service.add_todo(
                CreateTodoRequest(title=title, description=description, priority=priority)
            )
            return f"Todo added successfully with ID: {item_id}"
        except ValueError as e:
            return f"Error: {str(e)}"

    def handle_list(self) -> str:
        """Handle the 'list' or 'view' command."""
        todos = self.app_service.get_todos()

        if not todos:
            return "Your todo list is empty."

        output_lines = ["Todos:"]
        for i, todo in enumerate(todos, 1):
            status = "x" if todo.completed else " "
            priority_indicator = "*" * todo.priority
            output_lines.append(f"{i}. [{status}] {priority_indicator} {todo.id} - {todo.title}")
            if todo.description:
                output_lines.append(f"    Description: {todo.description}")

        return "\n".join(output_lines)

    def handle_update(self, args: List[str]) -> str:
        """Handle the 'update' command."""
        if len(args) < 3:
            return "Error: Missing ID or new title. Usage: update <id> \"new title\""

        item_id = args[1]
        new_title = " ".join(args[2:])

        if not new_title.strip():
            return "Error: New title cannot be empty"

        success = self.app_service.update_todo(
            UpdateTodoRequest(id=item_id, title=new_title)
        )

        if success:
            return "Todo updated successfully"
        else:
            return f"Error: Todo with ID {item_id} not found"

    def handle_update_details(self, args: List[str]) -> str:
        """Handle the 'updatedetails' command to update description and priority."""
        if len(args) < 3:
            return "Error: Missing ID and description. Usage: updatedetails <id> \"description\" [priority]"

        item_id = args[1]
        new_description = args[2] if len(args) > 2 else ""
        new_priority = int(args[3]) if len(args) > 3 and args[3].isdigit() else None

        if new_priority is not None and (new_priority < 1 or new_priority > 5):
            return "Error: Priority must be between 1 and 5"

        success = self.app_service.update_todo_details(
            UpdateTodoDetailsRequest(id=item_id, description=new_description, priority=new_priority)
        )

        if success:
            return "Todo details updated successfully"
        else:
            return f"Error: Todo with ID {item_id} not found"

    def handle_delete(self, args: List[str]) -> str:
        """Handle the 'delete' command."""
        if len(args) < 2:
            return "Error: Missing ID. Usage: delete <id>"
        
        item_id = args[1]
        success = self.app_service.delete_todo(item_id)
        
        if success:
            return "Todo deleted successfully"
        else:
            return f"Error: Todo with ID {item_id} not found"

    def handle_complete(self, args: List[str]) -> str:
        """Handle the 'complete' command."""
        if len(args) < 2:
            return "Error: Missing ID. Usage: complete <id>"
        
        item_id = args[1]
        success = self.app_service.toggle_completion(
            ToggleCompleteRequest(id=item_id, completed=True)
        )
        
        if success:
            return "Todo marked as complete"
        else:
            return f"Error: Todo with ID {item_id} not found"

    def handle_incomplete(self, args: List[str]) -> str:
        """Handle the 'incomplete' command."""
        if len(args) < 2:
            return "Error: Missing ID. Usage: incomplete <id>"
        
        item_id = args[1]
        success = self.app_service.toggle_completion(
            ToggleCompleteRequest(id=item_id, completed=False)
        )
        
        if success:
            return "Todo marked as incomplete"
        else:
            return f"Error: Todo with ID {item_id} not found"

    def handle_help(self) -> str:
        """Handle the 'help' command."""
        help_text = """
Available commands:
  add "title" ["description"] [priority] - Add a new todo (priority: 1-5)
  list                 - View all todos
  view                 - View all todos
  update <id> "title"  - Update a todo's title
  updatedetails <id> "description" [priority] - Update description and priority
  delete <id>          - Delete a todo
  complete <id>        - Mark a todo as complete
  incomplete <id>      - Mark a todo as incomplete
  help                 - Show this help message
  exit                 - Exit the application
  quit                 - Exit the application
        """.strip()
        return help_text

    def handle_exit(self) -> str:
        """Handle the 'exit' or 'quit' command."""
        return "Goodbye!"
#!/usr/bin/env python3
"""
Test script to demonstrate the Console Todo App functionality.
"""
import sys
import os
# Add the src directory to the Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from todo_app.domain.models import TodoList
from todo_app.application.services import TodoAppService
from todo_app.cli.commands import TodoCommandHandler


def demo_app():
    """Demonstrate the functionality of the Console Todo App."""
    print("=== Console Todo App Demo ===\n")
    
    # Initialize the application components
    todo_list = TodoList()
    app_service = TodoAppService(todo_list)
    command_handler = TodoCommandHandler(app_service)
    
    # Demo: Add todos
    print("1. Adding todos...")
    result = command_handler.handle_add(["add", "Buy groceries"])
    print(f"   {result}")
    
    result = command_handler.handle_add(["add", "Walk the dog"])
    print(f"   {result}")
    
    result = command_handler.handle_add(["add", "Finish project"])
    print(f"   {result}")
    
    # Demo: List todos
    print("\n2. Listing all todos...")
    result = command_handler.handle_list()
    print(f"   {result}")
    
    # Demo: Mark a todo as complete
    print("\n3. Marking 'Buy groceries' as complete...")
    # We'll need to get the ID of the 'Buy groceries' todo
    todos = app_service.get_todos()
    groceries_todo = next((todo for todo in todos if todo.title == "Buy groceries"), None)
    if groceries_todo:
        result = command_handler.handle_complete(["complete", groceries_todo.id])
        print(f"   {result}")
    
    # Demo: List todos again to see the change
    print("\n4. Listing all todos after marking one as complete...")
    result = command_handler.handle_list()
    print(f"   {result}")
    
    # Demo: Update a todo
    print("\n5. Updating 'Walk the dog' to 'Walk the dog and buy treats'...")
    dog_todo = next((todo for todo in todos if todo.title == "Walk the dog"), None)
    if dog_todo:
        result = command_handler.handle_update(["update", dog_todo.id, "Walk the dog and buy treats"])
        print(f"   {result}")
    
    # Demo: List todos again to see the change
    print("\n6. Listing all todos after updating one...")
    result = command_handler.handle_list()
    print(f"   {result}")
    
    # Demo: Delete a todo
    print("\n7. Deleting 'Finish project'...")
    project_todo = next((todo for todo in todos if todo.title == "Finish project"), None)
    if project_todo:
        result = command_handler.handle_delete(["delete", project_todo.id])
        print(f"   {result}")
    
    # Demo: List todos again to see the change
    print("\n8. Listing all todos after deleting one...")
    result = command_handler.handle_list()
    print(f"   {result}")
    
    print("\n=== Demo completed successfully! ===")


if __name__ == "__main__":
    demo_app()
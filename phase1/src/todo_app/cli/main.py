"""
Main CLI entry point for the Console Todo App.
"""
import sys
import argparse
from todo_app.domain.models import TodoList
from todo_app.application.services import TodoAppService
from todo_app.cli.commands import TodoCommandHandler


def main():
    """Main entry point for the CLI application."""
    # Initialize the application components
    todo_list = TodoList()
    app_service = TodoAppService(todo_list)
    command_handler = TodoCommandHandler(app_service)
    
    print("Welcome to the Console Todo App!")
    print("Type 'help' for available commands.")
    
    while True:
        try:
            # Get user input
            user_input = input("> ").strip()
            
            if not user_input:
                continue
            
            # Parse the command
            args = user_input.split()
            command = args[0].lower()
            
            # Handle different commands
            if command in ['add']:
                result = command_handler.handle_add(args)
                print(result)
                
            elif command in ['list', 'view']:
                result = command_handler.handle_list()
                print(result)
                
            elif command in ['update']:
                result = command_handler.handle_update(args)
                print(result)

            elif command in ['updatedetails']:
                result = command_handler.handle_update_details(args)
                print(result)

            elif command in ['delete']:
                result = command_handler.handle_delete(args)
                print(result)
                
            elif command in ['complete']:
                result = command_handler.handle_complete(args)
                print(result)
                
            elif command in ['incomplete']:
                result = command_handler.handle_incomplete(args)
                print(result)
                
            elif command in ['help']:
                result = command_handler.handle_help()
                print(result)
                
            elif command in ['exit', 'quit']:
                result = command_handler.handle_exit()
                print(result)
                break
                
            else:
                print(f"Error: Unknown command '{command}'. Type 'help' for available commands.")
                
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break
        except EOFError:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()
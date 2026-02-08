# Console Todo App

A simple command-line todo application built with Python, storing all data in memory.

## Features

- Add new todo items
- View all todo items with completion status
- Mark todo items as complete/incomplete
- Update todo item descriptions
- Delete todo items
- Clear error messages and user-friendly interface

## Requirements

- Python 3.13+

## Installation

1. Clone or download the repository
2. Navigate to the project directory
3. The application uses only Python standard library, so no additional installation is required

## Usage

Run the application with:

```bash
python run.py
```

Once running, you can use the following commands:

- `add "Your todo description"` - Add a new todo
- `list` or `view` - View all todos
- `update <id> "New description"` - Update a todo
- `delete <id>` - Delete a todo
- `complete <id>` - Mark a todo as complete
- `incomplete <id>` - Mark a todo as incomplete
- `help` - Show available commands
- `exit` or `quit` - Exit the application

## Architecture

The application follows a layered architecture:

- **Domain Layer**: Contains business logic and entities (TodoItem, TodoList)
- **Application Layer**: Orchestrates business operations (TodoAppService)
- **CLI Layer**: Handles user interaction (TodoCommandHandler)

## Testing

Run the unit tests with:

```bash
PYTHONPATH=src python -m unittest tests.unit.domain.test_models
```

Run the integration tests with:

```bash
PYTHONPATH=src python -m unittest tests.integration.cli.test_commands
```

## Data Storage

All data is stored in memory only and will be lost when the application exits. This is by design for this specific implementation.
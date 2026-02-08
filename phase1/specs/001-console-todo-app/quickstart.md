# Quickstart Guide: Console Todo App

## Overview
This guide will help you get started with the Console Todo App, including how to run it and use its features.

## Prerequisites
- Python 3.13 or higher
- No additional dependencies required (uses only standard library)

## Running the Application

1. Clone or download the repository
2. Navigate to the project directory
3. Run the application using the command:
   ```
   python run.py
   ```

## Available Commands

Once the application is running, you can use the following commands:

### Add a new todo
```
add "Your todo description here"
```
Example:
```
add Buy groceries
```

### View all todos
```
list
```
or
```
view
```

### Update a todo
```
update <id> "New description"
```
Example:
```
update 123e4567-e89b-12d3-a456-426614174000 "Updated todo description"
```

### Delete a todo
```
delete <id>
```
Example:
```
delete 123e4567-e89b-12d3-a456-426614174000
```

### Mark a todo as complete
```
complete <id>
```
Example:
```
complete 123e4567-e89b-12d3-a456-426614174000
```

### Mark a todo as incomplete
```
incomplete <id>
```
Example:
```
incomplete 123e4567-e89b-12d3-a456-426614174000
```

### Get help
```
help
```

### Exit the application
```
exit
```
or
```
quit
```

## Example Usage Session

```
$ python run.py
Welcome to the Console Todo App!
Type 'help' for available commands.
> add Buy groceries
Todo added successfully with ID: 123e4567-e89b-12d3-a456-426614174000
> add Walk the dog
Todo added successfully with ID: 123e4567-e89b-12d3-a456-426614174001
> list
Todos:
1. [ ] 123e4567-e89b-12d3-a456-426614174000 - Buy groceries
2. [ ] 123e4567-e89b-12d3-a456-426614174001 - Walk the dog
> complete 123e4567-e89b-12d3-a456-426614174000
Todo marked as complete.
> list
Todos:
1. [x] 123e4567-e89b-12d3-a456-426614174000 - Buy groceries
2. [ ] 123e4567-e89b-12d3-a456-426614174001 - Walk the dog
> exit
Goodbye!
```

## Error Handling

The application provides clear error messages when invalid commands or parameters are entered. Common error scenarios include:

- Attempting to update/delete/mark complete a todo that doesn't exist
- Providing an invalid command
- Missing required arguments for a command
- Empty or whitespace-only todo descriptions

## Architecture Overview

The application follows a layered architecture:

- **CLI Layer**: Handles user input/output using argparse
- **Application Layer**: Coordinates commands and business logic
- **Domain Layer**: Manages Todo entities and in-memory TodoList

All data is stored in memory only and will be lost when the application exits.
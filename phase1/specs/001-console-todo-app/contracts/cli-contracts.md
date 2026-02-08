# CLI Command Contracts: Console Todo App

## Overview
This document specifies the command-line interface contracts for the Console Todo App.

## Command Structure
The application accepts commands in the format:
```
command [arguments...]
```

## Available Commands

### 1. Add Todo
**Command**: `add`
**Arguments**: `<title>`
**Description**: Adds a new todo item with the specified title
**Success Response**: Confirmation message with the ID of the created todo
**Error Responses**:
- "Error: Todo title cannot be empty" (if title is empty or whitespace)
- "Error: Invalid command format" (if no title provided)

**Example**:
```
add "Buy groceries"
# Response: Todo added successfully with ID: 123e4567-e89b-12d3-a456-426614174000
```

### 2. List Todos
**Command**: `list` or `view`
**Arguments**: None
**Description**: Displays all todos with their completion status
**Success Response**: Formatted list of all todos
**Error Responses**: None

**Example**:
```
list
# Response:
# Todos:
# 1. [ ] 123e4567-e89b-12d3-a456-426614174000 - Buy groceries
# 2. [x] 123e4567-e89b-12d3-a456-426614174001 - Walk the dog
```

### 3. Update Todo
**Command**: `update`
**Arguments**: `<id> <new_title>`
**Description**: Updates the title of an existing todo
**Success Response**: Confirmation message
**Error Responses**:
- "Error: Todo with ID <id> not found" (if the todo doesn't exist)
- "Error: Todo title cannot be empty" (if new title is empty)
- "Error: Invalid command format" (if missing arguments)

**Example**:
```
update 123e4567-e89b-12d3-a456-426614174000 "Buy groceries and cook dinner"
# Response: Todo updated successfully
```

### 4. Delete Todo
**Command**: `delete`
**Arguments**: `<id>`
**Description**: Deletes a todo by its ID
**Success Response**: Confirmation message
**Error Responses**:
- "Error: Todo with ID <id> not found" (if the todo doesn't exist)
- "Error: Invalid command format" (if no ID provided)

**Example**:
```
delete 123e4567-e89b-12d3-a456-426614174000
# Response: Todo deleted successfully
```

### 5. Mark Todo Complete
**Command**: `complete`
**Arguments**: `<id>`
**Description**: Marks a todo as complete
**Success Response**: Confirmation message
**Error Responses**:
- "Error: Todo with ID <id> not found" (if the todo doesn't exist)
- "Error: Invalid command format" (if no ID provided)

**Example**:
```
complete 123e4567-e89b-12d3-a456-426614174000
# Response: Todo marked as complete
```

### 6. Mark Todo Incomplete
**Command**: `incomplete`
**Arguments**: `<id>`
**Description**: Marks a todo as incomplete
**Success Response**: Confirmation message
**Error Responses**:
- "Error: Todo with ID <id> not found" (if the todo doesn't exist)
- "Error: Invalid command format" (if no ID provided)

**Example**:
```
incomplete 123e4567-e89b-12d3-a456-426614174000
# Response: Todo marked as incomplete
```

### 7. Help
**Command**: `help`
**Arguments**: None
**Description**: Displays available commands and their usage
**Success Response**: Help text with command descriptions
**Error Responses**: None

**Example**:
```
help
# Response: (Displays help text)
```

### 8. Exit
**Command**: `exit` or `quit`
**Arguments**: None
**Description**: Exits the application
**Success Response**: Goodbye message
**Error Responses**: None

**Example**:
```
exit
# Response: Goodbye!
```

## Error Handling
All error responses follow the format:
```
Error: [descriptive message]
```

## Data Formats
- IDs are represented as UUID strings in the format: `123e4567-e89b-12d3-a456-426614174000`
- Todo titles are strings that may contain spaces
- Completion status is represented as `[ ]` for incomplete and `[x]` for complete in list views
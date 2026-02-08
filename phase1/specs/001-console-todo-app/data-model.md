# Data Model: Console Todo App

## Overview
This document describes the data structures and models for the Console Todo App.

## Domain Entities

### TodoItem
Represents a single task in the todo list.

**Attributes**:
- `id` (UUID): Unique identifier for the todo item
- `title` (str): The description/text of the todo item
- `completed` (bool): Whether the todo item has been completed
- `created_at` (datetime): Timestamp when the todo was created

**Validation Rules**:
- `title` must not be empty or consist only of whitespace
- `title` must be a string
- `completed` must be a boolean
- `id` must be a valid UUID

**State Transitions**:
- `incomplete` → `completed` (when marked as complete)
- `completed` → `incomplete` (when marked as incomplete)

### TodoList
Represents a collection of TodoItem objects.

**Attributes**:
- `items` (dict): Dictionary mapping UUIDs to TodoItem objects

**Operations**:
- `add_item(title: str) -> UUID`: Adds a new todo item to the list and returns its ID
- `get_all_items() -> List[TodoItem]`: Returns all items in the list
- `get_item(item_id: UUID) -> TodoItem`: Returns a specific item by ID
- `update_item(item_id: UUID, title: str) -> bool`: Updates the title of an existing item
- `delete_item(item_id: UUID) -> bool`: Removes an item from the list
- `mark_complete(item_id: UUID) -> bool`: Marks an item as complete
- `mark_incomplete(item_id: UUID) -> bool`: Marks an item as incomplete

**Validation Rules**:
- Cannot add an item with an empty title
- Cannot update an item that doesn't exist
- Cannot delete an item that doesn't exist
- Cannot mark complete/incomplete an item that doesn't exist

## Application DTOs (Data Transfer Objects)

### TodoItemDTO
Used for transferring todo data between application layers.

**Attributes**:
- `id` (str): String representation of the UUID
- `title` (str): The description/text of the todo item
- `completed` (bool): Whether the todo item has been completed
- `created_at` (str): ISO format string of the creation timestamp

### CreateTodoRequest
Used for requests to create a new todo.

**Attributes**:
- `title` (str): The description/text of the new todo item

### UpdateTodoRequest
Used for requests to update an existing todo.

**Attributes**:
- `id` (str): String representation of the UUID
- `title` (str): The new description/text for the todo item

### ToggleCompleteRequest
Used for requests to mark a todo as complete/incomplete.

**Attributes**:
- `id` (str): String representation of the UUID
- `completed` (bool): The completion status to set
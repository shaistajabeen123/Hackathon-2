# Todo Backend API Documentation

## Overview

The Todo Backend API provides RESTful endpoints for managing personal tasks. It supports creating, reading, updating, and deleting tasks while ensuring data isolation between users.

## API Endpoints

### Tasks

- `POST /api/v1/tasks` - Create a new task
- `GET /api/v1/tasks` - Get all tasks for the authenticated user
- `GET /api/v1/tasks/{task_id}` - Get a specific task by ID
- `PUT /api/v1/tasks/{task_id}` - Update a specific task
- `DELETE /api/v1/tasks/{task_id}` - Delete a specific task

### Users

- `POST /api/v1/users` - Create a new user
- `GET /api/v1/users/{user_id}` - Get user details by ID

## Authentication

All endpoints (except user creation) require a valid JWT token in the Authorization header:

```
Authorization: Bearer <token>
```

## Task Object

```json
{
  "id": "uuid-string",
  "title": "Task title",
  "description": "Optional task description",
  "completed": false,
  "user_id": "uuid-string",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

## Error Responses

All error responses follow this format:

```json
{
  "detail": "Error message"
}
```
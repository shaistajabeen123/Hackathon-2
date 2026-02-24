# Todo Backend API

This is the backend component of the Todo Full-Stack Web Application, built with FastAPI and SQLModel.

## Features

- RESTful API for task management
- User authentication and authorization (placeholder implementation)
- Data isolation between users
- PostgreSQL database with SQLModel ORM
- Alembic for database migrations

## Installation

1. Clone the repository
2. Navigate to the backend directory
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Copy the example environment file and update the values:

```bash
cp .env.example .env
```

## Running the Application

```bash
cd src
python main.py
```

Or using uvicorn:

```bash
cd src
uvicorn main:app --reload
```

## API Documentation

Once the application is running, visit `http://localhost:8000/docs` for interactive API documentation.

## Database Migrations

Coming soon with the authentication implementation.

## Project Structure

```
backend/
├── src/
│   ├── models/     # Database models
│   ├── services/   # Business logic
│   ├── api/        # API routes and dependencies
│   └── main.py     # Application entry point
├── docs/           # Documentation
├── tests/          # Test files
├── requirements.txt # Dependencies
├── alembic.ini     # Migration configuration
└── .env.example    # Environment variables example
```
# Research: Console Todo App

## Overview
This document captures the research and decisions made during the planning phase for the Console Todo App.

## Decision: Architecture Pattern
**What was chosen**: Layered architecture following Domain-Driven Design principles
- Domain layer: Contains business logic and entities
- Application layer: Orchestrates business operations
- Presentation/CLI layer: Handles user interaction

**Rationale**: This pattern provides clear separation of concerns, making the code easier to understand, test, and maintain. It also aligns with the requirement for clean code and clear project structure.

**Alternatives considered**:
- Monolithic approach: All code in a single file/module - rejected as it would violate the clean code requirement
- MVC pattern: More complex than needed for a simple CLI application

## Decision: Data Storage Approach
**What was chosen**: In-memory storage using Python objects
- TodoItem class to represent individual tasks
- TodoList class to manage collections of TodoItems
- UUID for unique identification of todos

**Rationale**: This directly satisfies the requirement for in-memory only storage with no files or databases. It's simple and efficient for the intended use case.

**Alternatives considered**:
- File-based storage: Would violate the in-memory only requirement
- Database storage: Would violate the in-memory only requirement

## Decision: CLI Framework
**What was chosen**: Built-in `argparse` module from Python standard library

**Rationale**: Since we're restricted to standard library only, `argparse` is the most appropriate choice for creating a command-line interface. It's well-documented and provides all necessary functionality for this application.

**Alternatives considered**:
- `sys.argv` directly: Would require more manual parsing logic
- Third-party libraries like Click: Not allowed as we can only use standard library

## Decision: Error Handling Strategy
**What was chosen**: Custom domain-specific exceptions with user-friendly error messages

**Rationale**: This ensures clear error messages for users while maintaining proper error handling internally. It aligns with the requirement for clear prompts and error handling.

**Alternatives considered**:
- Generic exception handling: Would not provide clear feedback to users
- Exit codes only: Would not provide descriptive error messages

## Decision: Testing Approach
**What was chosen**: Unit testing with Python's built-in `unittest` module

**Rationale**: This follows the constraint of using only the Python standard library. The layered architecture allows for good test coverage of each layer independently.

**Alternatives considered**:
- PyTest: Would require external dependencies
- No testing: Would violate quality standards
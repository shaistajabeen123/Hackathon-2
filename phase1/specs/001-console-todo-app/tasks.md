---

description: "Task list template for feature implementation"
---

# Tasks: Console Todo App

**Input**: Design documents from `/specs/001-console-todo-app/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The examples below include test tasks. Tests are OPTIONAL - only include them if explicitly requested in the feature specification.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- **Web app**: `backend/src/`, `frontend/src/`
- **Mobile**: `api/src/`, `ios/src/` or `android/src/`
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Create project structure per implementation plan
- [X] T002 [P] Create src/todo_app/__init__.py
- [X] T003 [P] Create src/todo_app/domain/__init__.py
- [X] T004 [P] Create src/todo_app/application/__init__.py
- [X] T005 [P] Create src/todo_app/cli/__init__.py
- [X] T006 [P] Create tests/unit/__init__.py
- [X] T007 [P] Create tests/integration/__init__.py
- [X] T008 Create run.py entry point file
- [X] T009 [P] Create requirements.txt (though using standard library only)

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

Examples of foundational tasks (adjust based on your project):

- [X] T010 Create TodoItem domain model in src/todo_app/domain/models.py
- [X] T011 Create TodoList domain model in src/todo_app/domain/models.py
- [X] T012 Create domain-specific exceptions in src/todo_app/domain/exceptions.py
- [X] T013 Create DTOs in src/todo_app/application/dtos.py
- [X] T014 Create application services base in src/todo_app/application/services.py
- [X] T015 Create CLI command handlers in src/todo_app/cli/commands.py
- [X] T016 Create main CLI entry point in src/todo_app/cli/main.py
- [X] T017 Create UUID utility functions in src/todo_app/utils.py

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add Todo Item (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new todo items to their list so that they can keep track of tasks they need to complete.

**Independent Test**: The user can successfully add a new todo item via the command-line interface and see it appear in their list of todos.

### Tests for User Story 1 (OPTIONAL - only if tests requested) ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [X] T018 [P] [US1] Unit test for TodoItem creation in tests/unit/domain/test_models.py
- [X] T019 [P] [US1] Unit test for TodoList.add_item method in tests/unit/domain/test_models.py
- [X] T020 [P] [US1] Integration test for add command in tests/integration/cli/test_commands.py

### Implementation for User Story 1

- [X] T021 [P] [US1] Implement TodoItem model with id, title, completed, created_at in src/todo_app/domain/models.py
- [X] T022 [P] [US1] Implement TodoList model with add_item method in src/todo_app/domain/models.py
- [X] T023 [P] [US1] Implement CreateTodoRequest DTO in src/todo_app/application/dtos.py
- [X] T024 [US1] Implement add_todo service in src/todo_app/application/services.py
- [X] T025 [US1] Implement add command handler in src/todo_app/cli/commands.py
- [X] T026 [US1] Connect add command to CLI in src/todo_app/cli/main.py
- [X] T027 [US1] Add validation for empty todo titles in src/todo_app/domain/models.py

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View Todo List (Priority: P1)

**Goal**: Allow users to view their list of todos so that they can see what tasks they need to complete.

**Independent Test**: The user can successfully view their list of todos with clear formatting showing task descriptions and completion status.

### Tests for User Story 2 (OPTIONAL - only if tests requested) ⚠️

- [X] T028 [P] [US2] Unit test for TodoList.get_all_items method in tests/unit/domain/test_models.py
- [X] T029 [P] [US2] Integration test for list/view command in tests/integration/cli/test_commands.py

### Implementation for User Story 2

- [X] T030 [P] [US2] Implement get_all_items method in TodoList model in src/todo_app/domain/models.py
- [X] T031 [P] [US2] Implement TodoItemDTO in src/todo_app/application/dtos.py
- [X] T032 [US2] Implement get_todos service in src/todo_app/application/services.py
- [X] T033 [US2] Implement list/view command handler in src/todo_app/cli/commands.py
- [X] T034 [US2] Connect list/view command to CLI in src/todo_app/cli/main.py

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Todo as Complete (Priority: P2)

**Goal**: Allow users to mark todos as complete so that they can track their progress and distinguish completed tasks from pending ones.

**Independent Test**: The user can successfully mark a specific todo as complete and see the updated status when viewing the list.

### Tests for User Story 3 (OPTIONAL - only if tests requested) ⚠️

- [X] T035 [P] [US3] Unit test for TodoList.mark_complete method in tests/unit/domain/test_models.py
- [X] T036 [P] [US3] Unit test for TodoList.mark_incomplete method in tests/unit/domain/test_models.py
- [X] T037 [P] [US3] Integration test for complete/incomplete command in tests/integration/cli/test_commands.py

### Implementation for User Story 3

- [X] T038 [P] [US3] Implement mark_complete and mark_incomplete methods in TodoList model in src/todo_app/domain/models.py
- [X] T039 [P] [US3] Implement ToggleCompleteRequest DTO in src/todo_app/application/dtos.py
- [X] T040 [US3] Implement toggle_completion service in src/todo_app/application/services.py
- [X] T041 [US3] Implement complete/incomplete command handlers in src/todo_app/cli/commands.py
- [X] T042 [US3] Connect complete/incomplete commands to CLI in src/todo_app/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Todo Description (Priority: P3)

**Goal**: Allow users to update the description of their todos so that they can correct mistakes or clarify task details.

**Independent Test**: The user can successfully update the description of a specific todo and see the change reflected when viewing the list.

### Tests for User Story 4 (OPTIONAL - only if tests requested) ⚠️

- [X] T043 [P] [US4] Unit test for TodoList.update_item method in tests/unit/domain/test_models.py
- [X] T044 [P] [US4] Integration test for update command in tests/integration/cli/test_commands.py

### Implementation for User Story 4

- [X] T045 [P] [US4] Implement update_item method in TodoList model in src/todo_app/domain/models.py
- [X] T046 [P] [US4] Implement UpdateTodoRequest DTO in src/todo_app/application/dtos.py
- [X] T047 [US4] Implement update_todo service in src/todo_app/application/services.py
- [X] T048 [US4] Implement update command handler in src/todo_app/cli/commands.py
- [X] T049 [US4] Connect update command to CLI in src/todo_app/cli/main.py

**Checkpoint**: At this point, User Stories 1, 2, 3, AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Todo (Priority: P3)

**Goal**: Allow users to delete todos that are no longer relevant so that their list stays clean and focused on current tasks.

**Independent Test**: The user can successfully delete a specific todo from their list.

### Tests for User Story 5 (OPTIONAL - only if tests requested) ⚠️

- [X] T050 [P] [US5] Unit test for TodoList.delete_item method in tests/unit/domain/test_models.py
- [X] T051 [P] [US5] Integration test for delete command in tests/integration/cli/test_commands.py

### Implementation for User Story 5

- [X] T052 [P] [US5] Implement delete_item method in TodoList model in src/todo_app/domain/models.py
- [X] T053 [US5] Implement delete_todo service in src/todo_app/application/services.py
- [X] T054 [US5] Implement delete command handler in src/todo_app/cli/commands.py
- [X] T055 [US5] Connect delete command to CLI in src/todo_app/cli/main.py

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T056 [P] Add error handling for invalid commands in src/todo_app/cli/main.py
- [X] T057 [P] Add error handling for invalid command parameters in src/todo_app/cli/commands.py
- [X] T058 [P] Add help command implementation in src/todo_app/cli/commands.py
- [X] T059 [P] Add exit/quit command implementation in src/todo_app/cli/commands.py
- [X] T060 [P] Add proper error messages for all operations in src/todo_app/domain/exceptions.py
- [X] T061 [P] Add validation for very long todo descriptions in src/todo_app/domain/models.py
- [X] T062 [P] Add validation for UUID format in src/todo_app/utils.py
- [X] T063 [P] Add comprehensive unit tests in tests/unit/
- [X] T064 [P] Add comprehensive integration tests in tests/integration/
- [X] T065 [P] Documentation updates in docs/
- [X] T066 [P] Code cleanup and refactoring
- [X] T067 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together (if tests requested):
Task: "Unit test for TodoItem creation in tests/unit/domain/test_models.py"
Task: "Unit test for TodoList.add_item method in tests/unit/domain/test_models.py"
Task: "Integration test for add command in tests/integration/cli/test_commands.py"

# Launch all models for User Story 1 together:
Task: "Implement TodoItem model with id, title, completed, created_at in src/todo_app/domain/models.py"
Task: "Implement TodoList model with add_item method in src/todo_app/domain/models.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
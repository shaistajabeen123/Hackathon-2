from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from ..models.task import Task, TaskRead, TaskCreate, TaskUpdate
from ..services.task_service import (
    create_task,
    get_tasks_for_user,
    get_task_by_id,
    update_task,
    delete_task
)
from .deps import get_current_user_dep
from ..models.user import User
import uuid

router = APIRouter()

@router.post("/tasks", response_model=TaskRead)
async def create_new_task(task: TaskCreate, current_user: User = Depends(get_current_user_dep), db_session: AsyncSession = Depends(get_async_session)):
    # Validate user_id format
    try:
        user_uuid = uuid.UUID(task.user_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid user ID format")

    # Ensure user can only create tasks for themselves
    if str(current_user.id) != str(user_uuid):
        raise HTTPException(status_code=403, detail="Not authorized to create tasks for this user")

    created_task = await create_task(task, db_session)
    return created_task

@router.get("/tasks", response_model=List[TaskRead])
async def get_tasks(current_user: User = Depends(get_current_user_dep), db_session: AsyncSession = Depends(get_async_session)):
    # Get tasks for the authenticated user
    user_id = str(current_user.id)
    tasks = await get_tasks_for_user(user_id, db_session)
    return tasks

@router.get("/tasks/{task_id}", response_model=TaskRead)
async def get_task(task_id: str, current_user: User = Depends(get_current_user_dep), db_session: AsyncSession = Depends(get_async_session)):
    # Validate task_id format
    try:
        task_uuid = uuid.UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid task ID format")

    task = await get_task_by_id(task_id, db_session)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    # Check if the task belongs to the current user
    if str(task.user_id) != str(current_user.id):
        raise HTTPException(status_code=404, detail="Task not found")

    return task

@router.put("/tasks/{task_id}", response_model=TaskRead)
async def update_task_endpoint(task_id: str, task_update: TaskUpdate, current_user: User = Depends(get_current_user_dep), db_session: AsyncSession = Depends(get_async_session)):
    # Validate task_id format
    try:
        task_uuid = uuid.UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid task ID format")

    # First, check if the task exists and belongs to the current user
    existing_task = await get_task_by_id(task_id, db_session)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if str(existing_task.user_id) != str(current_user.id):
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = await update_task(task_id, task_update, db_session)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@router.delete("/tasks/{task_id}")
async def delete_task_endpoint(task_id: str, current_user: User = Depends(get_current_user_dep), db_session: AsyncSession = Depends(get_async_session)):
    # Validate task_id format
    try:
        task_uuid = uuid.UUID(task_id)
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid task ID format")

    # First, check if the task exists and belongs to the current user
    existing_task = await get_task_by_id(task_id, db_session)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if str(existing_task.user_id) != str(current_user.id):
        raise HTTPException(status_code=404, detail="Task not found")

    deleted = await delete_task(task_id, db_session)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
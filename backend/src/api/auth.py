from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession
from ..database import get_async_session
from ..models.auth import Token, UserRegister
from ..services.auth_service import authenticate_user, register_user, create_access_token
from datetime import timedelta

router = APIRouter()

@router.post("/auth/login", response_model=Token, tags=["authentication"])
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db_session: AsyncSession = Depends(get_async_session)):
    """
    Authenticate user and return access token
    
    - **username**: Email address of the user
    - **password**: Plain text password
    """
    user = await authenticate_user(form_data.username, form_data.password, db_session)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Create access token
    access_token_expires = timedelta(minutes=30)  # You can make this configurable
    access_token = create_access_token(
        data={"sub": str(user.id)}, expires_delta=access_token_expires
    )
    
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/auth/register", response_model=dict, tags=["authentication"])
async def register(user_data: UserRegister, db_session: AsyncSession = Depends(get_async_session)):
    """
    Register a new user account
    
    - **email**: Email address for the new account
    - **username**: Unique username for the new account
    - **password**: Password for the new account
    """
    # Register the new user
    user = await register_user(user_data, db_session)
    
    # Return success message (without sensitive info)
    return {"message": "User registered successfully", "user_id": str(user.id)}
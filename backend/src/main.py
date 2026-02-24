import logging
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from .api.tasks import router as tasks_router
from .api.users import router as users_router
from .api.auth import router as auth_router
import uvicorn # type: ignore
import os
from sqlmodel import SQLModel # type: ignore
from .database import engine
from .config import settings

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Todo Backend API",
    description="REST API for the Todo Full-Stack Web Application",
    version="1.0.0"
)

# Include routers
app.include_router(tasks_router, prefix="/api/v1", tags=["tasks"])
app.include_router(users_router, prefix="/api/v1", tags=["users"])
app.include_router(auth_router, prefix="/api/v1", tags=["authentication"])

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"{request.method} {request.url}")
    response = await call_next(request)
    logger.info(f"Response status: {response.status_code}")
    return response

@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}", exc_info=True)
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"}
    )

@app.on_event("startup")
async def startup():
    # Create tables
    logger.info("Initializing database tables...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    logger.info("Database tables initialized.")

@app.get("/")
def read_root():
    logger.info("Root endpoint accessed")
    return {"message": "Todo Backend API", "version": "1.0.0"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))
    logger.info(f"Starting server on port {port}")
    uvicorn.run(app, host="0.0.0.0", port=port)
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession # type: ignore
from sqlmodel import SQLModel # pyright: ignore[reportMissingImports]
from .config import settings
from urllib.parse import urlparse

# Get database URL from settings
database_url = settings.database_url

# For Neon PostgreSQL, we need to handle the connection string differently
if database_url.startswith("postgresql://"):
    # Parse the URL to extract components
    parsed = urlparse(database_url)
    username = parsed.username
    password = parsed.password
    hostname = parsed.hostname
    port = parsed.port
    database = parsed.path.lstrip('/')

    # Build the asyncpg-compatible connection string
    DATABASE_CONNECTION_STRING = f"postgresql+asyncpg://{username}:{password}@{hostname}:{port}/{database}"
else:
    # Use SQLite for local development/testing, but with async driver
    # For SQLite async support, we'll use aiosqlite
    if database_url.startswith("sqlite:///"):
        # Convert sqlite URL to use aiosqlite async driver
        DATABASE_CONNECTION_STRING = database_url.replace("sqlite:///", "sqlite+aiosqlite:///")
    else:
        DATABASE_CONNECTION_STRING = database_url

engine: AsyncEngine = create_async_engine(DATABASE_CONNECTION_STRING)


async def get_async_session():
    async with AsyncSession(engine) as session:
        yield session
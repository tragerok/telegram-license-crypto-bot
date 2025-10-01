"""Database module initialization"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
from config import Config

Base = declarative_base()

# Create async engine
config = Config()
engine = create_async_engine(
    config.database_url.replace('postgresql://', 'postgresql+asyncpg://'),
    echo=False,
    future=True
)

# Create async session factory
async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    """Initialize database tables"""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_session() -> AsyncSession:
    """Get database session"""
    async with async_session() as session:
        yield session

__all__ = ['Base', 'engine', 'async_session', 'init_db', 'get_session']

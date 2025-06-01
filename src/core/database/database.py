from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from src.core.config import settings


def get_engine():
    return create_async_engine(settings.database_url, echo=False)


def get_async_session_factory() -> async_sessionmaker[AsyncSession]:
    engine = get_engine()
    return async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

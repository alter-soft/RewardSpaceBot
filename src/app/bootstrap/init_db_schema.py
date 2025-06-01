from sqlalchemy.ext.asyncio import AsyncEngine
from src.core.database.database import get_engine
from sqlalchemy import MetaData

from src.modules.users.infrastructure.models.user_model import UserModel


metadata: MetaData = UserModel.metadata


async def create_all_tables(engine: AsyncEngine | None = None) -> None:
    engine = engine or get_engine()
    async with engine.begin() as conn:
        await conn.run_sync(metadata.create_all)

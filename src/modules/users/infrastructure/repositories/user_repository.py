from typing import Optional, Sequence
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.infrastructure.models.user_model import UserModel


class UserRepository:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def check_exists(self, user_id: int) -> bool:
        stmt = select(UserModel.telegram_user_id).where(UserModel.telegram_user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalar() is not None

    async def save(self, user: UserModel) -> None:
        self._session.add(user)
        await self._session.commit()

    async def find_all(self) -> Sequence[UserModel]:
        stmt = select(UserModel)
        result = await self._session.execute(stmt)
        return result.scalars().all()

    async def find_by_id(self, user_id: int) -> Optional[UserModel]:
        stmt = select(UserModel).where(UserModel.telegram_user_id == user_id)
        result = await self._session.execute(stmt)
        return result.scalar()

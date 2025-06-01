from typing import Callable, Awaitable
from src.modules.users.infrastructure.models.user_model import UserModel


class UpdateIntegrationCodeUseCase:
    def __init__(
            self,
            get_user: Callable[[int], Awaitable[UserModel | None]],
            save_user: Callable[[UserModel], Awaitable[None]]
    ):
        self._get_user = get_user
        self._save_user = save_user

    async def execute(self, user_id: int, new_code: str) -> None:
        user = await self._get_user(user_id)
        if user is None:
            raise ValueError(f"User with id {user_id} not found")

        user.integration_code = new_code
        await self._save_user(user)

from typing import Optional
from src.modules.users.infrastructure.repositories.user_repository import UserRepository
from src.modules.users.application.dtos.user_dtos import ResponseUserDto


class GetUserByIdUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, user_id: int) -> Optional[ResponseUserDto]:
        user = await self._repository.find_by_id(user_id)

        if user is None:
            return None

        return ResponseUserDto(
            id=user.id,
            telegram_user_id=user.telegram_user_id,
            first_name=user.first_name,
            last_name=user.last_name,
            username=user.username,
            language_code=user.language_code,
            integration_code=user.integration_code,
            created_at=user.created_at
        )

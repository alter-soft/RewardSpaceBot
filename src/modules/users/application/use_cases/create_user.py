from datetime import datetime, timezone

from src.modules.users.application.dtos.user_dtos import CreateUserDto, ResponseUserDto
from src.modules.users.infrastructure.models.user_model import UserModel
from src.modules.users.infrastructure.repositories.user_repository import UserRepository


class CreateUserUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, dto: CreateUserDto) -> ResponseUserDto:
        user = UserModel(
            telegram_user_id=dto.telegram_user_id,
            first_name=dto.first_name,
            last_name=dto.last_name,
            username=dto.username,
            language_code=dto.language_code,
            integration_code=dto.integration_code,
            created_at=datetime.now(timezone.utc)
        )

        await self._repository.save(user)

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

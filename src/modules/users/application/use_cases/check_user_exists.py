from src.modules.users.infrastructure.repositories.user_repository import UserRepository


class CheckUserExistsUseCase:
    def __init__(self, repository: UserRepository):
        self._repository = repository

    async def execute(self, user_id: int) -> bool:
        return await self._repository.check_exists(user_id)

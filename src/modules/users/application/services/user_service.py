from src.modules.users.application.use_cases.create_user import CreateUserUseCase
from src.modules.users.application.use_cases.get_all_users import GetAllUsersUseCase
from src.modules.users.application.use_cases.get_user_by_id import GetUserByIdUseCase
from src.modules.users.application.use_cases.check_user_exists import CheckUserExistsUseCase
from src.modules.users.application.use_cases.update_integration_code import UpdateIntegrationCodeUseCase
from src.modules.users.application.dtos.user_dtos import CreateUserDto, ResponseUserDto
from src.modules.users.infrastructure.models.user_model import UserModel


class UserService:
    def __init__(
            self,
            create_use_case: CreateUserUseCase,
            get_all_use_case: GetAllUsersUseCase,
            get_by_id_use_case: GetUserByIdUseCase,
            check_exists_use_case: CheckUserExistsUseCase,
            update_integration_code_use_case: UpdateIntegrationCodeUseCase,
    ):
        self._create = create_use_case
        self._get_all = get_all_use_case
        self._get_by_id = get_by_id_use_case
        self._check_exists = check_exists_use_case
        self._update_integration_code = update_integration_code_use_case

    async def register_user(self, dto: CreateUserDto) -> ResponseUserDto:
        return await self._create.execute(dto)

    async def get_all_users(self) -> list[UserModel]:
        return await self._get_all.execute()

    async def get_user_by_id(self, user_id: int) -> UserModel | None:
        return await self._get_by_id.execute(user_id)

    async def check_user_exists(self, user_id: int) -> bool:
        return await self._check_exists.execute(user_id)

    async def update_integration_code(self, user_id: int, new_code: str) -> None:
        await self._update_integration_code.execute(user_id, new_code)

    async def get_all_user_ids(self) -> list[int]:
        users = await self.get_all_users()
        return [u.telegram_user_id for u in users]

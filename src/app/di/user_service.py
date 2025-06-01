from sqlalchemy.ext.asyncio import AsyncSession

from src.modules.users.application.services.user_service import UserService
from src.modules.users.application.use_cases.create_user import CreateUserUseCase
from src.modules.users.application.use_cases.get_all_users import GetAllUsersUseCase
from src.modules.users.application.use_cases.get_user_by_id import GetUserByIdUseCase
from src.modules.users.application.use_cases.check_user_exists import CheckUserExistsUseCase
from src.modules.users.application.use_cases.update_integration_code import UpdateIntegrationCodeUseCase
from src.modules.users.infrastructure.repositories.user_repository import UserRepository


def provide_user_service(session: AsyncSession) -> UserService:
    repo = UserRepository(session)

    return UserService(
        create_use_case=CreateUserUseCase(repo),
        get_all_use_case=GetAllUsersUseCase(repo),
        get_by_id_use_case=GetUserByIdUseCase(repo),
        check_exists_use_case=CheckUserExistsUseCase(repo),
        update_integration_code_use_case=UpdateIntegrationCodeUseCase(
            get_user=repo.find_by_id,
            save_user=repo.save
        ),
    )

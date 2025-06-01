from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from datetime import datetime, timezone
from src.app.di.user_service import provide_user_service
from src.core.database.database import get_async_session_factory
from src.modules.users.application.dtos.user_dtos import CreateUserDto
from src.app.bot.keyboards.to_site_keyboard import keyboard as to_site_keyboard
from src.app.bot import bot
user_router = Router()


@user_router.message(Command("start"))
async def start_cmd(message: Message):
    session_factory = get_async_session_factory()

    async with session_factory() as session:
        user_service = provide_user_service(session)

        user_exists = await user_service.check_user_exists(message.from_user.id)

        integration_code = message.text[7:]

        if not user_exists:
            await user_service.register_user(CreateUserDto(
                telegram_user_id=message.from_user.id,
                username=message.from_user.username,
                first_name=message.from_user.first_name,
                last_name=message.from_user.last_name,
                language_code=message.from_user.language_code,
                integration_code=integration_code if integration_code != '' else None,
                created_at=datetime.now(timezone.utc)
            ))

            # TODO: API POST integration code : telegram_user_id

    user = await user_service.get_user_by_id(message.from_user.id)

    user_integration_code = user.integration_code

    if user_integration_code:
        await message.answer("Заходьте у сервіс прямо в чаті!", reply_markup=to_site_keyboard)

    elif integration_code and not user_integration_code:
        await user_service.update_integration_code(message.from_user.id, integration_code)
        await message.answer("Ви успішно інтегрували телеграм бота!")
    else:
        await message.answer("Ввійдіть у свій профіль, щоб користуватися ботом:", reply_markup=to_site_keyboard)


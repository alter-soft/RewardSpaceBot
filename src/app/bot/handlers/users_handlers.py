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
        pass

    elif integration_code and not user_integration_code:
        await user_service.update_integration_code(message.from_user.id, integration_code)
        await message.answer("Ви успішно інтегрували телеграм бота!")
    else:
        await message.answer("Ввійдіть у свій профіль, щоб користуватися ботом:", reply_markup=to_site_keyboard)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from src.modules.broadcast.application.services.broadcast_service import BroadcastService

from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from src.app.di.user_service import provide_user_service
from src.app.di.broadcast_service import provide_broadcast_service
from src.core.database.database import get_async_session_factory
from src.modules.broadcast.presentation.states import BroadcastStates

user_router = Router()


@user_router.message(Command("broadcast"))
async def start_broadcast(message: Message, state: FSMContext):
    await message.answer("Введи текст повідомлення:")
    await state.set_state(BroadcastStates.text)


@user_router.message(BroadcastStates.text)
async def get_broadcast_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer("Надішли фото або ❌ якщо без фото:")
    await state.set_state(BroadcastStates.photo)


@user_router.message(BroadcastStates.photo)
async def get_broadcast_photo(message: Message, state: FSMContext):
    if message.photo:
        photo_id = message.photo[-1].file_id
        await state.update_data(photo=photo_id)
    else:
        await state.update_data(photo=None)

    await message.answer("Додати кнопку?\nФормат: `Текст | URL`\nАбо ❌", parse_mode="Markdown")
    await state.set_state(BroadcastStates.button)


@user_router.message(BroadcastStates.button)
async def get_broadcast_button(message: Message, state: FSMContext):
    data = await state.get_data()
    text = data["text"]
    photo = data["photo"]

    button_text, button_url = None, None
    if "|" in message.text:
        try:
            button_text, button_url = map(str.strip, message.text.split("|", 1))
        except:
            pass

    keyboard = None
    if button_text and button_url:
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text=button_text, url=button_url)]]
        )

    await message.answer("🔁 Розсилка почалась...")
    session_factory = get_async_session_factory()
    async with session_factory() as session:
        user_service = provide_user_service(session)
        broadcast_service = provide_broadcast_service()

        user_ids = await user_service.get_all_user_ids()
        await broadcast_service.send_broadcast(
            user_ids=user_ids,
            text=text,
            photo_url=photo,
            reply_markup=keyboard
        )

    await message.answer("✅ Готово!", reply_markup=ReplyKeyboardRemove())
    await state.clear()

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from src.core.config import settings

keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text="Відкрити",
                web_app=WebAppInfo(url=settings.website_url)
            )
        ]
    ]
)


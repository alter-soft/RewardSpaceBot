from aiogram import Bot
from aiogram.types import (
    InputMediaPhoto,
    Message,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardButton,
)
from typing import Optional


class BroadcastService:
    def __init__(self, bot: Bot):
        self.bot = bot

    async def send_broadcast(
            self,
            user_ids: list[int],
            text: str,
            *,
            photo_url: Optional[str] = None,
            parse_mode: str = "HTML",
            reply_markup: Optional[InlineKeyboardMarkup | ReplyKeyboardMarkup] = None,
    ) -> None:
        for user_id in user_ids:
            try:
                if photo_url:
                    await self.bot.send_photo(
                        chat_id=user_id,
                        photo=photo_url,
                        caption=text,
                        parse_mode=parse_mode,
                        reply_markup=reply_markup,
                    )
                else:
                    await self.bot.send_message(
                        chat_id=user_id,
                        text=text,
                        parse_mode=parse_mode,
                        reply_markup=reply_markup,
                    )
            except Exception as e:
                print(f"[Broadcast Error] Failed to send to {user_id}: {e}")

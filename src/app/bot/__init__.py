from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from src.core.config import settings
from aiogram.client.default import DefaultBotProperties as df


bot = Bot(token=settings.bot_api)
dp = Dispatcher(storage=MemoryStorage())
df.parse_mode = "html"

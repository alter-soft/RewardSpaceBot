import asyncio

from src.app.bot import bot, dp
from src.app.bot.handlers.users_handlers import user_router
from src.app.bot.handlers.broadcast_handlers import broadcast_router

from src.app.bootstrap.init_db_schema import create_all_tables

dp.include_router(user_router)
dp.include_router(broadcast_router)


async def main():
    await create_all_tables()

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

from src.modules.broadcast.application.services.broadcast_service import BroadcastService
from src.app.bot import bot


def provide_broadcast_service() -> BroadcastService:
    return BroadcastService(bot)

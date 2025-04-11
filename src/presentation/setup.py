from aiogram import Bot, Dispatcher
from dishka import AsyncContainer
from dishka.integrations.aiogram import setup_dishka

from config import config
from .command.start_command import router as start_command_router


async def setup_bot(container: AsyncContainer) -> None:
    bot = Bot(token=config.TG_TOKEN.get_secret_value())
    dp = Dispatcher()

    setup_dishka(container=container, router=dp, auto_inject=True)

    dp.include_routers(
        start_command_router,
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

from aiogram import Router, F
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(F.data == "chat_with_service")
async def chat_with_service_screen(callback_query: CallbackQuery) -> None:
    pass

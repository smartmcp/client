from aiogram import Router, F
from aiogram.types import CallbackQuery


router = Router()


@router.callback_query(F.data == "publish_swagger")
async def publish_swagger_screen(callback_query: CallbackQuery) -> None:
    pass

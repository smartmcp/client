from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dishka import FromDishka

from src.application.usecase.is_service_active_usecase import IsServiceActiveUsecase
from src.presentation.kb.start_kb import start_kb

router = Router()


@router.message(Command("start"))
async def start_command(
    message: Message, is_service_active_usecase: FromDishka[IsServiceActiveUsecase]
) -> None:
    is_active = await is_service_active_usecase.execute()

    text = (
        "Привет! Я бот для управления сервером SmartMCP.\n\n"
        f"На данный момент сервис {'активен ☑️' if is_active else 'не активен ❌'}"
    )

    kb = start_kb() if is_active else None

    await message.answer(text=text, reply_markup=kb)

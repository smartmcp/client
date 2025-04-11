from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from dishka import FromDishka

from src.application.usecase.is_service_active_usecase import IsServiceActiveUsecase


router = Router()


@router.message(Command("start"))
async def start_command(
    message: Message, is_service_active_usecase: FromDishka[IsServiceActiveUsecase]
) -> None:
    text = (
        "Привет! Я бот для управления сервером SmartMCP.\n\n"
        f"На данный момент сервис {'активен ☑️' if await is_service_active_usecase.execute() else 'не активен ❌'}"
    )

    await message.answer(text=text)

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def start_kb() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text="🔗 Опубликовать Swagger", callback_data="publish_swagger"
                ),
                InlineKeyboardButton(
                    text="💬 Обратиться к сервису", callback_data="chat_with_service"
                ),
            ]
        ]
    )

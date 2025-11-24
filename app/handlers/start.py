from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.keyboards.kb import main_menu

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(
        "Welcome to Protection Bot!\nClick 'Register' to begin.",
        reply_markup=main_menu
    )

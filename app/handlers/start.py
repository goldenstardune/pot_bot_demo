from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from app.keyboards.kb import main_menu

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Witaj w bocie ochronnym Pot Bot!\nKliknij 'Register', aby rozpocząć.",
        reply_markup=main_menu
    )

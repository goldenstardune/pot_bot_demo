from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.register_states import RegisterStates
from .generator import generate_captcha, verify_captcha 
router = Router(name="captcha_router")


@router.message(F.text == "Register")
async def register_start(message: Message, state: FSMContext):
    question, _ = generate_captcha(message.from_user.id)
    await message.answer(question)
    await state.set_state(RegisterStates.waiting_for_captcha)


@router.message(RegisterStates.waiting_for_captcha)
async def captcha_handler(message: Message, state: FSMContext):
    if not verify_captcha(message.from_user.id, message.text.strip()):
        await message.answer("Wrong answer! Try again with /start")
        await state.clear()
        return

    await message.answer("Enter your first name:")
    await state.set_state(RegisterStates.waiting_for_first_name)


__all__ = ["router"]

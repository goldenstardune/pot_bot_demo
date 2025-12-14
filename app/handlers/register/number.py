from aiogram import Router, F
from aiogram.types import Message, ReplyKeyboardRemove 
from aiogram.fsm.context import FSMContext

from app.states.register_states import RegisterStates
from app.captcha.generator import generate_captcha

router = Router()


@router.message(RegisterStates.waiting_for_number, F.contact)
async def number_handler(message: Message, state: FSMContext):
    await state.update_data(number=message.contact.phone_number)

    question, _ = generate_captcha(message.from_user.id)

    await message.answer(
        question,
        reply_markup=ReplyKeyboardRemove()
    )

    await state.set_state(RegisterStates.waiting_for_captcha)

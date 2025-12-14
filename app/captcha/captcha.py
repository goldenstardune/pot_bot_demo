from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.register_states import RegisterStates
from app.captcha.generator import verify_captcha
from app.questions.loader import get_random_question 
from aiogram.utils.keyboard import InlineKeyboardBuilder

from app.middleware.antispam import RegistrationAntiSpamMiddleware

import re

router = Router(name="captcha_handler")


@router.message(RegisterStates.waiting_for_captcha)
async def captcha_handler(message: Message, state: FSMContext, **kwargs):
    middleware_data = kwargs.get("middleware_data", {})

    user_answer = message.text.strip()

    if not re.fullmatch(r"\d+", user_answer):
        await message.answer("Wpisz tylko cyfry! Spróbuj jeszcze raz:")
        return

    if not verify_captcha(message.from_user.id, message.text.strip()):
        await message.answer("Zła odpowiedź! Spróbuj ponownie przez /start")
        await state.clear()
        return

    question_data = get_random_question()

    current_data = await state.get_data()
    await state.set_data({**current_data, "security_question": question_data})


    builder = InlineKeyboardBuilder()
    for key, text in question_data["options"].items():
        builder.button(text=text, callback_data=f"sec_{key}")

    builder.adjust(1)  

    await message.answer(
        f"Pytanie bezpieczeństwa:\n\n{question_data['question']}",
        reply_markup=builder.as_markup()
    )

    await state.set_state(RegisterStates.waiting_for_security_question)

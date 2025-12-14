from aiogram import Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.register_states import RegisterStates
from app.handlers.utils import is_valid_name
from app.keyboards.kb import request_number

router = Router()


@router.message(RegisterStates.waiting_for_second_name)
async def second_name_handler(message: Message, state: FSMContext):
    name = message.text.strip()
    if not is_valid_name(name):
        await message.answer(
         "Nieprawidłowe nazwisko!\n"
         "Dozwolone są tylko litery, spacje, łączniki i apostrofy.\n"
         "Spróbuj ponownie:",
         reply_markup=ReplyKeyboardRemove()
        )
        return

    await state.update_data(second_name=name)
    await message.answer("Podaj swój numer:", reply_markup=request_number)
    await state.set_state(RegisterStates.waiting_for_number)

from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.register_states import RegisterStates
from app.handlers.utils import is_valid_name

router = Router()


@router.message(RegisterStates.waiting_for_first_name)
async def first_name_handler(message: Message, state: FSMContext):
    name = message.text.strip()
    if not is_valid_name(name):
        await message.answer(
           "Nieprawidłowe imię!\n"
           "Dozwolone są tylko litery, spacje, łączniki i apostrofy.\n"
           "Na przykład: Anna-Maria, O'Connor\n"
           "Spróbuj ponownie:"
        )
        return

    await state.update_data(first_name=name)
    await message.answer("Wprowadź swoje nazwisko:")
    await state.set_state(RegisterStates.waiting_for_second_name)

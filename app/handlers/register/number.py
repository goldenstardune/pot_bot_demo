from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext

from app.states.register_states import RegisterStates
from app.database.requests import create_or_update_user
from app.keyboards.kb import main_menu

router = Router()

@router.message(RegisterStates.waiting_for_number, F.contact)
async def number_handler(message: Message, state: FSMContext):
    data = await state.get_data()
    await create_or_update_user(
        tg_id=message.from_user.id,
        first_name=data["first_name"],
        second_name=data["second_name"],
        number=message.contact.phone_number
    )
    await message.answer(
        f"Rejestracja zakończona!\n\n"
        f"Imię: {data['first_name']}\n"
        f"Nazwisko: {data['second_name']}\n"
        f"Numer: {message.contact.phone_number}",
        reply_markup=main_menu
    )
    await state.clear()
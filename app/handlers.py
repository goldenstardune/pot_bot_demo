from aiogram import F, Router #do separacji
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import app.keyboards as kb #importacja kalwiatury
import app.database.requests as rq


router = Router()

class Register(StatesGroup):
	first_name = State()
	second_name = State()
	number = State()

@router.message(CommandStart())
async def cmd_start(message: Message):
	await rq.set_user(message.from_user.id)
	await message.answer('Hi, I\'m Pot Bot!', reply_markup = kb.main)
	await message.reply('Ready to join Cyber Protection of Team? Secure your spot now!')

@router.message(Command('help'))
async def cmd_help(message: Message):
	await message.answer('Can I help you?')

@router.message(F.text == 'Edit profile')
async def calatog(message: Message):
	await message.answer('Select an option to edit your profile', reply_markup = kb.catalog)

@router.callback_query(F.data == 'username')
async def username(callback: CallbackQuery):
	await callback.answer('You\' ve selected the username change option. Enter your new username now!', show_alert=True) #nie jest konieczne; do implementacji bazy danych

@router.message(F.text == 'Register')
async def register(message: Message, state: FSMContext):
	await state.set_state(Register.first_name)
	await message.answer('Please enter your first name', reply_markup=kb.main_no_placeholder)

@router.message(Register.first_name)
async def register_username(message: Message, state: FSMContext):
	await state.update_data(first_name=message.text) #zachowanie informacji pod kluczem username
	await state.set_state(Register.second_name)
	await message.answer('Please enter your second name', reply_markup=kb.main_no_placeholder)


@router.message(Register.second_name)
async def register_second_name(message: Message, state: FSMContext):
	await state.update_data(second_name=message.text) #zachowanie informacji pod kluczem second name
	await state.set_state(Register.number)
	await message.answer('Please enter your number', reply_markup=kb.get_number)

@router.message(Register.number, F.contact)
async def register_number(message: Message, state: FSMContext):
	if not message.contact or not message.contact.phone_number:
		await message.answer("Please share your phone number using the button below to verify your account!")
		return
	await state.update_data(number=message.contact.phone_number)
	data = await state.get_data()
	await rq.save_user_data(
		tg_id=message.from_user.id,
		first_name=data["first_name"],
		second_name=data["second_name"],
		number=data["number"]
	)
	await message.answer(f'Your first name: {data["first_name"]}\nYour second name: {data["second_name"]}\nYour number: +{data["number"]}')
	await message.answer("Registration complete!", reply_markup = kb.main)
	await state.clear()
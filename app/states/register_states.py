from aiogram.fsm.state import State, StatesGroup

class RegisterStates(StatesGroup):
    waiting_for_captcha = State()   
    waiting_for_first_name = State()
    waiting_for_second_name = State()
    waiting_for_number = State()

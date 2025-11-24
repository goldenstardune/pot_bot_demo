from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Register"), KeyboardButton(text="Sign up")],
        [KeyboardButton(text="Edit profile")]
    ],
    resize_keyboard=True,
    input_field_placeholder="Select an action"
)

request_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text="Send number", request_contact=True)]],
    resize_keyboard=True,
    one_time_keyboard=True
)

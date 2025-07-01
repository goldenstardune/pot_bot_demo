from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

main = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Register')],
        [KeyboardButton(text='Sign up')],
        [KeyboardButton(text='Edit profile')],
    ],
    resize_keyboard=True,
    input_field_placeholder='Choose a menu option...'
)

main_no_placeholder = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Register')],
        [KeyboardButton(text='Sign up')],
        [KeyboardButton(text='Edit profile')],
    ],
    resize_keyboard=True
)

catalog = InlineKeyboardMarkup(
    inline_keyboard = [
        [InlineKeyboardButton(text='usermane', callback_data='username')],
        [InlineKeyboardButton(text='first name', callback_data='first_name')],
        [InlineKeyboardButton(text='second name', callback_data='second_name')]
        ] 
 )


get_number = ReplyKeyboardMarkup(
    keyboard=[[KeyboardButton(text='Send your number', request_contact=True)]], 
    resize_keyboard=True
)

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


command_state = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton("/state"))
)


form_name = (
    ReplyKeyboardMarkup(resize_keyboard=True)
    .add(KeyboardButton("/cancel"))
)


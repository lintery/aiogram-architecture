from aiogram.dispatcher.filters.state import State, StatesGroup


class Form(StatesGroup):
    name = State()
    age = State()

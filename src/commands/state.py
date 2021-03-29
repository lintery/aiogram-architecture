from src.config import dp, keyboards
from src.states import Form
from src.database import User

from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext


@dp.message_handler(Command("state", ignore_case=True))
async def state_handler(message: types.Message):
    await message.reply(
        "Введите ваше имя..",
        reply_markup=keyboards.form_name
    )
    await Form.name.set()


@dp.message_handler(Command("cancel", ignore_case=True), state=[Form.name, Form.age])
async def form_cancel(message: types.Message, state: FSMContext):
    await message.reply(
        "Вывожу вас из стейта..",
        reply_markup=keyboards.command_state
    )
    await state.finish()


@dp.message_handler(state=Form.name)
async def form_name(message: types.Message, state: FSMContext):
    if len(message.text) > 30:
        await message.reply("Имя не может быть длиннее 30 символов!")
        return

    user = await User.get(uid=message.from_user.id)
    user.name = message.text
    await user.save()

    await message.reply(
        "Имя успешно установлено!\n"
        "Введите ваш возраст"
    )
    await Form.next()


@dp.message_handler(state=Form.age)
async def form_name(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.reply("Возраст должнен состоять только из цифр!")
        return
    elif int(message.text) > 150 or int(message.text) < 0:
        await message.reply("Возраст не может быть отрицательным или слишком большим!")
        return

    user = await User.get(uid=message.from_user.id)
    user.age = int(message.text)
    await user.save()

    await message.reply(
        "Возраст установлен!\n"
        "Вывожу вас из стейта..",
        reply_markup=keyboards.command_state
    )
    await state.finish()

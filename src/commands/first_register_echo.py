from aiogram import types

from src.config import dp, keyboards
from src.database import User
from src.filters import FirstRegister


@dp.message_handler(FirstRegister())
async def first_register_echo_handler(message: types.Message):
    user = await User.get(uid=message.from_user.id)

    await message.reply(
        f"Вы были первый зарегистрированный пользователь! "
        f"За все время вы написали {user.count_messages} сообщений.\n\n"
        f"Крайнее сообщение: {message.text}",
        reply_markup=keyboards.command_state
    )

from src.config import dp, keyboards
from src.database import User

from aiogram import types


@dp.message_handler(state=None)
async def echo_handler(message: types.Message):
    user = await User.get(uid=message.from_user.id)

    await message.answer(
        f"В сумме вы написали {user.count_messages} сообщений\n\n"
        f"Ваше крайнее сообщение:\n{message.text}",
        reply_markup=keyboards.command_state
    )

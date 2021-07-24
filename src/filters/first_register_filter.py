from aiogram import types
from aiogram.dispatcher.filters import Filter

from src.database import User


class FirstRegister(Filter):
    async def check(self, message: types.Message) -> bool:
        user = await User.get(uid=message.from_user.id)
        return user.id == 1

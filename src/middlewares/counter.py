from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from src.database import User


class CounterMiddleware(BaseMiddleware):

    @staticmethod
    async def on_process_message(message: types.Message, data: dict):
        user = await User.get(uid=message.from_user.id)
        user.count_messages += 1
        await user.save()
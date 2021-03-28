from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram import types

from src.database import User


class RegistrationMiddleware(BaseMiddleware):

    @staticmethod
    async def on_process_message(message: types.Message, data: dict):
        user = await User.get_or_none(uid=message.from_user.id)

        if not user:
            await User.create(uid=message.from_user.id)

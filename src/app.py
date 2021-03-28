from aiogram import executor

from commands import dp
from middlewares import CounterMiddleware, RegistrationMiddleware
from database import setup_db


async def on_startup(dispatcher):
    await setup_db()

    dp.middleware.setup(RegistrationMiddleware())
    dp.middleware.setup(CounterMiddleware())


executor.start_polling(dp, on_startup=on_startup)
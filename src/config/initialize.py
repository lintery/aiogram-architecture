from .const import BOT_TOKEN

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

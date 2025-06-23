from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from environs import Env

env = Env()
env.read_env()
TOKEN = env("TOKEN")

bot = Bot(TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: Message):
  await message.answer("Hello!")

if __name__ == "__main__":
  dp.run_polling(bot)
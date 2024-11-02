import asyncio
import random
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import dotenv_values

# Загрузка токена из .env файла
token = dotenv_values(".env")["BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()

# Список случайных имен
names = ["Сергей", "Екатерина", "Александр", "Михаил", "Тамаев", "Ахмет"]

@dp.message(Command("start"))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f'Привет, {name}!'
    await message.answer(msg)

@dp.message(Command("myinfo"))
async def myinfo(message: types.Message):
    user = message.from_user
    info = (
        f"Ваш id: {user.id}\n"
        f"Ваше имя: {user.first_name}\n"
        f"Ваш username: @{user.username if user.username else 'не задан'}"
    )
    await message.answer(info)

@dp.message(Command("random"))
async def random_name(message: types.Message):
    random_choice = random.choice(names)  # Исправлено на random.choice
    await message.answer(f'Случайное имя: {random_choice}')

@dp.message()
async def echo_handler(message: types.Message):
    await message.answer("Привет, дос!")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

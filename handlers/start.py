from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup

start_router = Router()
id_list = []

@start_router.message(Command('start'))
async def start_handler(message: types.Message):
    name = message.from_user.first_name
    msg = f"Привет {name}"
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
        [
            types.InlineKeyboardButton(
                text="my profile inst",
                url="https://www.instagram.com/_ismaev_11/",
            )
        ],
        [
            types.InlineKeyboardButton(
                text="my tg channel",
                url="https://web.telegram.org/a/",
            )
        ]
        ]
    )
    await message.answer(msg, reply_markup=kb)
    us_id = message.from_user.id
    if us_id not in id_list:
        id_list.append(us_id)
    await message.answer(f"my bot was used by {len(id_list)} users")
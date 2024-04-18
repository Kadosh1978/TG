from aiogram import types, Router
from aiogram.filters import CommandStart

user_private_router = Router()

@user_private_router.message(CommandStart())
async def echo_handler(message: types.Message) -> None:
    await message.answer('Это была команда Старт')

@user_private_router.message()
async def echo(message: types.Message) -> None:
    await message.answer(message.text)
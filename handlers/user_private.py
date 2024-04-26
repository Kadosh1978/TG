from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from aiogram.utils.formatting import as_list, as_marked_section, Bold


from filters.chat_types import ChatTypeFilter
from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))

@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message) -> None:
    await message.answer('Привет, я виртуальный помощник', reply_markup=reply.start_kb3.as_markup(
        resize_keyboard = True, input_field_placeholder = 'Что Вас интересует?'
    ))

# @user_private_router.message(F.text.lower() == 'меню')
@user_private_router.message(or_f(Command('menu'), (F.text.lower() == 'меню')))
async def menu_cmd(message: types.Message) -> None:
    await message.answer('Вот меню:', reply_markup=reply.del_kbd)

@user_private_router.message(F.text.lower() == 'о нас')
@user_private_router.message(Command('about'))
async def about_cmd(message: types.Message) -> None:
    await message.answer('О нас')

@user_private_router.message(F.text.lower() == 'варианты оплаты')
@user_private_router.message(Command('payment'))
async def payment_cmd(message: types.Message) -> None:

    text = as_marked_section(
            Bold('Варианты оплаты:'),
            'Картой в боте',
            'При получении карта/кэш',
            'В заведении',
            marker='✅ ',
    )

    await message.answer(text.as_html())

@user_private_router.message((F.text.lower().contains ('доставк')) | (F.text.lower() == 'варианты доставки'))
@user_private_router.message(Command('shipping'))
async def shipping_cmd(message: types.Message) -> None:

    text = as_list(
        as_marked_section(
            Bold('Варианты доставки/заказа:'),
            'Курьер',
            'Самовывоз(Сейчас прибегу заберу)',
            'Покушаю у Вас',
            marker='✅ ',
        ),
        as_marked_section(
            Bold('Нельзя:'),
            'Почта',
            'Голуби',

            marker='❎',
        ),
        sep='\n-----------\n'
    )

    await message.answer(text.as_html())


# @user_private_router.message(F.text)
# async def menu_cmd(message: types.Message) -> None:
#     await message.answer('Магический фильтр2')

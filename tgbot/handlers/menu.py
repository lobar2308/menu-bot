from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove

from tgbot.keyboards.reply import menu_keyboard, type_lavash_keyboard, type_pizza_keyboard, type_shashlik_keyboard


async def show_menu(msg: Message):
    await msg.answer("Menu", reply_markup=await menu_keyboard())


async def lavash(msg: Message):
    await msg.answer("What kind of lavash do you want?", reply_markup=await type_lavash_keyboard())


async def lavash_type(msg: Message):
    await msg.answer("Thankyou",
                     reply_markup=ReplyKeyboardRemove())


async def pizza(msg: Message):
    await msg.answer("What kind of pizza do you want?", reply_markup=await type_pizza_keyboard())


async def pizza_type(msg: Message):
    await msg.answer("Thankyou",
                     reply_markup=ReplyKeyboardRemove())


async def shashlik(msg: Message):
    await msg.answer("What kind of pizza do you want?", reply_markup=await type_shashlik_keyboard())


async def shashlik_type(msg: Message):
    await msg.answer("Thankyou",
                     reply_markup=ReplyKeyboardRemove())


def register_menu(dp: Dispatcher):
    dp.register_message_handler(
        show_menu,
        text=["Menu", "/menu"]
    ),
    dp.register_message_handler(
        lavash,
        text="🌯lavash"
    ),
    dp.register_message_handler(
        lavash_type,
        text=["🌯Pishloqli lavash", "🌯Tandir lavash", "📔Menu"]
    ),
    dp.register_message_handler(
        pizza,
        text="🍕pizza"
    )
    dp.register_message_handler(
        pizza_type,
        text=["🍕Americano pizza", "🍕Margarita pizza", "🍕Milano pizza", "📔Menu"]
    ),
    dp.register_message_handler(
        shashlik,
        text="🍢shashlik"
    )
    dp.register_message_handler(
        shashlik_type,
        text=["🍗Tovuqli shashlik", "🥩Mol go'shtli shashlik", "🍖Qo'y go'shtli shashlik", "📔Menu"]
    )


from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from tgbot.misc.utils import Map


async def phone_number(texts: Map):
    """Phone number inline keyboard"""
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=texts.user.kb.reply.phone,
                            request_contact=True)],
            [KeyboardButton(text=texts.user.kb.reply.close)],
        ],
        resize_keyboard=True,
    )
    return keyboard


async def menu_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='🌯lavash'),
            ],
            [
                KeyboardButton(text="🍕pizza"),
                KeyboardButton(text="🍢shashlik"),
            ]
        ],
        resize_keyboard=True
    )
    return keyboard


async def type_lavash_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🌯Pishloqli lavash"),
                KeyboardButton(text="🌯Tandir lavash"),
            ],
            [
                KeyboardButton(text="📔Menu")
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


async def type_pizza_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🍕Americano pizza"),
            ],
            [
                KeyboardButton(text="🍕Margarita pizza"),
                KeyboardButton(text="🍕Milano pizza"),
            ],
            [
                KeyboardButton(text="📔Menu")
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard


async def type_shashlik_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="🍗Tovuqli shashlik"),
            ],
            [
                KeyboardButton(text="🥩Mol go'shtli shashlik"),
                KeyboardButton(text="🍖Qo'y go'shtli shashlik"),
            ],
            [
                KeyboardButton(text="📔Menu")
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard

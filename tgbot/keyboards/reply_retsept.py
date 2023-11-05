from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from tgbot.misc.utils import Map


async def retsept_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Shirinliklar"),
                KeyboardButton(text="Issiq ovqatlar"),
            ]
        ],
        resize_keyboard=True
    )
    return keyboard


async def type_shirinlik_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="tort"),
                KeyboardButton(text="pirog"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard

async def type_ovqat_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="osh"),
                KeyboardButton(text="manti"),
            ]
        ],
        resize_keyboard=True,
    )
    return keyboard
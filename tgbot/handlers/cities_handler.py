from aiogram import Dispatcher
from aiogram.types import Message, CallbackQuery

from tgbot.keyboards.inline import cities_keyboard
from tgbot.misc.weather import get_weather


async def cities_menu(msg: Message):
    await msg.answer("Menu", reply_markup=await cities_keyboard())

async def city(call: CallbackQuery):
    await call.message.delete()
    weather = get_weather(call.data)
    await call.message.answer(f"Temperature: {(weather['main'].get('temp') - 32) * 0.5}\n"
                              f"Wind speed :{weather['wind'].get('speed')}\n"
                              f"Wind direction:{weather['wind'].get('deg')}\n")

def register_cities_menu(dp: Dispatcher):
    dp.register_message_handler(
        cities_menu,
        commands="cities",
    ),
    dp.register_callback_query_handler(
        city,
        text=["Samarkand","Navai","Bukhara","Tashkent","Khorazm","Andijan"]
    )


from aiogram import Dispatcher
from aiogram.types import Message, ReplyKeyboardRemove

from tgbot.keyboards.reply_retsept import retsept_keyboard, type_shirinlik_keyboard, type_ovqat_keyboard

async def show_retsept(msg: Message):
    await msg.answer("Retsept", reply_markup=await retsept_keyboard())

async def shirinlik(msg: Message):
    await msg.answer("Qanday turdagi shirinlik retsepti kerak?", reply_markup=await type_shirinlik_keyboard())

async def shirinlik_type(msg: Message):
    await msg.answer("Ingredientlar: Yomg'irli shokoladli shabaka:Yumurtalar - 3 dona Sut - 1 stakan Shokolad - 100 gr Toza qand - 1 stakan Undan unum - 2 stakan Kakao to'zi - 2 ta osh qoshiq Soda - 1/2 choy qoshiq Uksus - 1/2 choy qoshiq. Krem:Qaymoq - 1 liter Shokolad - 200 gr Toza qand - 1/2 stakan. Tayyorlash tartibi: Tort uchun yumurtalar va shakarni ayrilgan idishda yaxshi aralashtiring. Shokoladni eritib, sut bilan aralashtiring. Uning ichiga yumurta-shakar massasini qo'shing va yaxshi aralashtiring. Undan unum, sodani (uksus bilan qaynatilgan) va kakao to'zini qo'shing. Yana bir bor yaxshi aralashtiring. Tort formani margarin bilan yopib, undan unum serpib, shabakani to'kib qo'yamiz. O'choqqa joylangan tort formani 180°C ga isitilgan mini-duxovkaga joylaymiz. 25-30 daqiqa pishiramiz. Tayyor shabakani kiyimdan chiqarib, sekin tort formidan chiqarib, to'kkanini 2 qismga kesamiz. Krem uchun ekstrakor krem qaymoqni qaynatib yetkazamiz, ichiga eritilgan shokoladni dam qo'shib tushirib bo'lgan qaymoqni qo'shamiz.Shabakani krem bilan mo'ljallab, yarim soatdan keyin ikkinchi qismni ham kremga moshlab yopamiz.",
                    reply_markup=ReplyKeyboardRemove())

async def ovqat(msg: Message):
    await msg.answer("Qaysi ovqatni retsepti kkerak?", reply_markup=await type_ovqat_keyboard())

async def ovqat_type(msg: Message):
    await msg.answer("Ingredientlar:Devzira - 2 stakan Go'sht (goshtli socha) - 500 gr Piyoz - 2 dona Sabzavotlar (zerdak, piyoz, sabzavot) - 3 ta Morkov - 3 dona Qora zira - 1 choy qoshiq Sahar to'zi  choy qoshiq Kuritilgan tuz  3 choy qoshiq  Non - 1 dona (agar istasangiz, soni ortiqqa chiqishi mumkin) Qaynatilgan suv - 1 liter Qizartma yag'i - 100 ml. Tayyorlash tartibi: Qozonni kattaroq tanlang, go'shtni, piyozni va morkovni kesing. Qozonni o'rniga qo'ying, yag'ni qizdiring va go'shtni qizarting. Go'sht qizilganda, unga piyoz qo'shing va yana bir bor qizdiring. Sabzavotlar qizildan keyin, qora zira, sahar va morkov qo'shing. Har xil ingredientlarni aralashtiring va piyoz bilan birga ezish uchun 15-20 daqiqa dam o'tkazing. Nonni yuvib, kesing. Tuzni qo'shing (miqdorini o'zgartirib oling) va qozonni suvga to'ldiring.vSuv yoki qaynatilgan suv qaynamaga tushgandan so'ng, devzirani tashlang va harakatni o'rniga qo'ying (suv devzirani qoplashi kerak). Devzirani qaynamaguncha pishiring. osh tayyor",
                     reply_markup=ReplyKeyboardRemove())



def register_retsept(dp: Dispatcher):
    dp.register_message_handler(
        show_retsept,
        text=["Retsept"]
    ),
    dp.register_message_handler(
        shirinlik,
        text="Shirinliklar"
    ),
    dp.register_message_handler(
        shirinlik_type,
        text=["tort", "pirog"]
    ),
    dp.register_message_handler(
        ovqat,
        text="Issiq ovqatlar"
    )
    dp.register_message_handler(
        ovqat_type,
        text=["osh", "manti"]
    )
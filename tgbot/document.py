from aiogram import types
from aiogram.dispatcher import FSMContext

from tgbot.misc.states import Document


async def start_document(msg: types.Message):
    await msg.answer(f"Document tayyorlash boshladim, ismingizni kiriting")
    await Document.first()

async def get_name(msg: types.Message, state: FSMContext):
    if len(msg.text) <= 2:
        await msg.answer("Ismingiz juda qisqa qayta kiriting")
        return
    for char in msg.text:
        if char.isdigit():
            await msg.answer("Ismingizda raqam bo'lmasligi kerak, qayta kiriting")
            return

    await state.update_data(
        {
            "name": msg.text
        }
    )
    await msg.answer("Familiyangizni kiriting")

    await Document.next()

async def get_surname(msg: types.Message, state: FSMContext):
    if len(msg.text) < 5:
        await msg.answer("Familiyangiz juda qisqa qayta kiriting")
        return
    for char in msg.text:
        if char.isdigit():
            await msg.answer("Familyangizda raqam bo'lmasligi kerak, qayta kiriting")
            return

    await state.update_data(
        {
            "surname": msg.text
        }
    )
    await msg.answer("PNFL ni kiriting")

    await Document.next()

async def get_personal_number(msg: types.Message, state: FSMContext):
    if not msg.text.isdigit():
        await msg.answer("PNFLni raqamda kiriting")
        return
    if len(msg.text) < 16:
        await msg.answer("PNFL juda qisqa qayta kiriting")
        return

    data = await state.get_data()
    print("data", data)

    name = data.get("name")
    surname = data.get('surname')
    personal_number = msg.text

    await msg.answer(f"Ismingiz{name}\nFamilyangiz {surname}\nPNFL: {personal_number}")

    await state.finish()





def register_handlers_document(dp):
    dp.register_message_handler(
        start_document,
        commands="document",
        state=None
    ),
    dp.register_message_handler(
        get_name,
        state=Document.name
    )

    dp.register_message_handler(
        get_surname,
        state=Document.surname
    )
    dp.register_message_handler(
        get_personal_number,
        state=Document.personal_number
    )

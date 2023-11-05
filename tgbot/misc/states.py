from aiogram.dispatcher.filters.state import State, StatesGroup
class Document(StatesGroup):
    name = State()
    surname = State()
    personal_number = State()

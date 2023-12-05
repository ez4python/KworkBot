from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    language = State()
    fullname = State()
    phone_number = State()


class TaskState(StatesGroup):
    category = State()
    title = State()
    description = State()
    price = State()

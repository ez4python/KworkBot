from aiogram.fsm.state import StatesGroup, State


class UserState(StatesGroup):
    language = State()
    fullname = State()
    phone_number = State()


class FreelancerState(StatesGroup):
    language = State()
    fullname = State()
    phone_number = State()
    category = State()


class TaskState(StatesGroup):
    category = State()
    title = State()
    description = State()
    price = State()

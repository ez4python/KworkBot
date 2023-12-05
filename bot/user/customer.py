from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from sqlalchemy.dialects.mysql import insert

from bot import data, UserState
from bot.button.inline import categories_inline_btn
from bot.button.reply import phone_number_btn
from bot.state import TaskState
from db.config import session
from db.model import Customer
from dispatcher import dp


@dp.message(lambda msg: msg.text == data['UZB']['customer'])
@dp.message(lambda msg: msg.text == data['ENG']['customer'])
async def customer_handler(msg: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get('lang')
    await state.set_state(UserState.fullname)
    text = data[lang]['fullname']
    await msg.answer(text)


@dp.message(UserState.fullname)
async def fullname_handler(msg: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data['lang']
    state_data.update({"fullname": msg.text})
    state_data.update({"user_id": msg.from_user.id})
    await state.set_data(state_data)
    await state.set_state(UserState.phone_number)
    text = data[lang]['phone_number']
    await msg.answer(text, reply_markup=phone_number_btn(lang))


@dp.message(UserState.phone_number, F.contact)
async def phone_number_handler(msg: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang")
    phone_number = msg.contact.phone_number
    state_data.update({"phone_number": phone_number})
    await state.set_data(state_data)
    await state.set_state(TaskState.category)
    query = insert(Customer).values(**state_data)
    session.execute(query)
    session.commit()
    await msg.answer(data[lang]["specialty_text"], reply_markup=categories_inline_btn())

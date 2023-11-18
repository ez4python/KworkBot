from aiogram import F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from bot import data, UserState
from dispatcher import dp


@dp.message(lambda msg: msg.text == data['UZB']['customer'])
@dp.message(lambda msg: msg.text == data['ENG']['customer'])
async def customer_handler(msg: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get('lang')
    await state.set_state(UserState.fullname)
    state_data.update({"fullname": msg.text})
    await state.set_data(state_data)
    await state.set_state(UserState.phone_number)
    text = data[lang]['phone_number']
    await msg.answer(text)


@dp.message(UserState.phone_number, F.contact)
async def phone_number_handler(msg: Message, state: FSMContext):
    state_data = await state.get_data()
    fullname = state_data.get('fullname')
    phone_number = msg.contact.phone_number
    state_data.update({"phone_number": phone_number})
    await state.set_data(state_data)

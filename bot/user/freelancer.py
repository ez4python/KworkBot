from aiogram import types, F
from aiogram.fsm.context import FSMContext
from sqlalchemy import select
from sqlalchemy.dialects.mysql import insert

from bot import data
from bot.button.inline import categories_inline_btn
from bot.button.reply import phone_number_btn, main_menu
from bot.state import FreelancerState
from db.config import session
from db.model import Freelancer
from dispatcher import dp


@dp.message(lambda msg: msg.text == data['UZB']['freelancer'])
@dp.message(lambda msg: msg.text == data['ENG']['freelancer'])
async def freelancer_handler(msg: types.Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang")
    q = select(Freelancer).where(Freelancer.user_id == msg.from_user.id)
    freelancer = session.execute(q).fetchone()
    if freelancer:
        await msg.answer(text=data[lang]["already_register"])
    else:
        await state.set_state(FreelancerState.fullname)
        await msg.answer(data[lang]["fullname"])


@dp.message(FreelancerState.fullname)
async def fullname_handler(msg: types.Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data['lang']
    state_data.update({"fullname": msg.text})
    state_data.update({"user_id": msg.from_user.id})
    await state.set_data(state_data)
    await state.set_state(FreelancerState.phone_number)
    text = data[lang]['phone_number']
    await msg.answer(text, reply_markup=phone_number_btn(lang))


@dp.message(FreelancerState.phone_number, F.contact)
async def phone_number_handler(msg: types.Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang")
    phone_number = msg.contact.phone_number
    state_data.update({"phone_number": phone_number})
    await state.set_data(state_data)
    await state.set_state(FreelancerState.category)
    await msg.answer(data[lang]["specialty_freelancer_text"], reply_markup=categories_inline_btn())


@dp.callback_query(FreelancerState.category)
async def choose_category_handler(call: types.CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang")
    state_data.update({"category_id": int(call.data)})
    user = {
        "fullname": state_data.get("fullname"),
        "phone_number": state_data.get("phone_number"),
        "lang": state_data.get("lang"),
        "category_id": state_data.get("category_id"),
        "user_id": state_data.get("user_id")
    }
    q = insert(Freelancer).values(**user)
    session.execute(q)
    session.commit()
    await state.set_data(state_data)
    await call.message.delete()
    await call.message.answer("Successful register", reply_markup=main_menu(lang))

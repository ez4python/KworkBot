from aiogram import types
from aiogram.fsm.context import FSMContext
from sqlalchemy import select

from bot import TaskState, data
from bot.button.reply import main_menu
from bot.utils import confirm_task_admin
from db.config import session
from db.model import Task, Customer
from dispatcher import dp


@dp.callback_query(TaskState.category)
async def choose_category_handler(call: types.CallbackQuery, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang")
    state_data.clear()
    state_data.update({"lang": lang, "category_id": int(call.data)})
    await state.set_data(state_data)
    await state.set_state(TaskState.title)
    await call.message.delete()
    await call.message.answer(data[lang]['task_title'])


@dp.message(TaskState.title)
async def title_handler(msg: types.Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang")
    state_data.update({"title": msg.text})
    await state.set_data(state_data)
    await state.set_state(TaskState.description)
    await msg.answer(data[lang]["task_description"])


@dp.message(TaskState.description)
async def description_handler(msg: types.Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data.get("lang")
    state_data.update({"description": msg.text})
    await state.set_data(state_data)
    await state.set_state(TaskState.price)
    await msg.answer(data[lang]["task_price"])


@dp.message(TaskState.price)
async def price_handler(msg: types.Message, state: FSMContext):
    query = select(Customer.id).where(Customer.user_id == msg.from_user.id)
    customer_id = session.execute(query).fetchone()[0]
    state_data = await state.get_data()
    lang = state_data.get("lang")
    state_data.update({"price": msg.text.replace(" ", ''), "customer_id": customer_id})
    del state_data["lang"]

    await state.set_data(state_data)
    await confirm_task_admin(msg.bot, state_data)
    await msg.answer(data[lang]["confirm_task"], reply_markup=main_menu(lang))
    await msg.answer("⏳")

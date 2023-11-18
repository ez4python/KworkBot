from aiogram import F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from bot.button.text import begin_text
from bot.button.reply import language_button, main_menu
from bot.language import data
from bot.state import UserState
from dispatcher import dp


@dp.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    await msg.answer(begin_text, reply_markup=language_button())
    await state.set_state(UserState.language)
    await msg.answer("Tilni tanlang 👇", reply_markup=language_button())


@dp.message(lambda msg: msg.text in ("🇺🇿 UZB", "🇬🇧 ENG"), UserState.language)
async def language_handler(msg: Message, state: FSMContext):
    lang = msg.text.split()[1]
    state_data = await state.get_data()
    state_data.update({"lang": lang})
    await state.set_data(state_data)
    text = data[lang]['welcome']
    await msg.answer(text, reply_markup=main_menu(lang))


@dp.message(lambda msg: msg.text == data['UZB']['language'])
@dp.message(lambda msg: msg.text == data['ENG']['language'])
async def language_handler(msg: Message, state: FSMContext):
    state_data = await state.get_data()
    lang = state_data['lang']
    await state.set_state(UserState.language)
    await msg.answer(data[lang]['choose_lang'], reply_markup=language_button())

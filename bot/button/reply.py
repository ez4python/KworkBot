from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from sqlalchemy import select

from bot.language import data
from db.config import session
from db.model import Category


def language_button():
    uzb_btn = KeyboardButton(text = "🇺🇿 UZB")
    eng_btn = KeyboardButton(text = "🇬🇧 ENG")
    design = [[uzb_btn,eng_btn]]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True , one_time_keyboard=True)


def main_menu(lang):
    text_dict = data[lang]
    btn1 = KeyboardButton(text = text_dict['freelancer'])
    btn2 = KeyboardButton(text = text_dict['customer'])
    btn3 = KeyboardButton(text = text_dict['vacancy'])
    btn4 = KeyboardButton(text = text_dict['language'])
    design = [
        [btn1 , btn2],
        [btn3],
        [btn4]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)


def phone_number_btn(lang):
    btn = KeyboardButton(text =data[lang]['phone_button'], request_contact=True)
    return ReplyKeyboardMarkup(keyboard=[[btn]], resize_keyboard=True, one_time_keyboard=True)




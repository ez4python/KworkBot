from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

from bot.language import data


def language_button():
    uzb_btn = KeyboardButton(text="🇺🇿 UZB")
    eng_btn = KeyboardButton(text="🇬🇧 ENG")
    return ReplyKeyboardMarkup(keyboard=[[uzb_btn, eng_btn]], resize_keyboard=True, one_time_keyboard=True)


def main_menu(lang):
    text_dict = data[lang]
    btn1 = KeyboardButton(text=text_dict["freelancer"])
    btn2 = KeyboardButton(text=text_dict["customer"])
    btn3 = KeyboardButton(text=text_dict["vacancy"])
    btn4 = KeyboardButton(text=text_dict["language"])
    design = [
        [btn1, btn2],
        [btn3],
        [btn4]
    ]
    return ReplyKeyboardMarkup(keyboard=design, resize_keyboard=True, one_time_keyboard=True)

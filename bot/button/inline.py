from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from sqlalchemy import select

from db.config import session
from db.model import Category


def categories_inline_btn():
    q = select(Category)
    categories: list = session.execute(q).fetchall()
    design = []
    row = []
    for category in categories:
        category = category[0]
        row.append(InlineKeyboardButton(text=category.name, callback_data=str(category.id)))
        if len(row) == 2:
            design.append(row)
            row = []
    if row:
        design.append(row)

    return InlineKeyboardMarkup(inline_keyboard=design)


def confirm_inline_btn(task_id):
    yes = InlineKeyboardButton(text="ACCEPT 🟢", callback_data=f"accept_{task_id}")
    no = InlineKeyboardButton(text="IGNORE 🔴", callback_data=f"ignore_{task_id}")
    return InlineKeyboardMarkup(inline_keyboard=[[yes, no]])

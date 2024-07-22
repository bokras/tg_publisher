from aiogram.types import (
    KeyboardButton,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
import texts

def main_menu():
    k = InlineKeyboardMarkup(
        inline_keyboard=[
            InlineKeyboardButton(te)
        ]
    )
    return k
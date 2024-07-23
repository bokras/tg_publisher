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
            [InlineKeyboardButton(text=texts.start_work_btn, callback_data="start_work")],
            [InlineKeyboardButton(text=texts.parser_accounts_manage_btn, callback_data="manage_accounts")],
            [InlineKeyboardButton(text=texts.parser_channels_manage_btn, callback_data="manage_channels")],
            [InlineKeyboardButton(text=texts.admins_manage_btn, callback_data="manage_admins")],
            [InlineKeyboardButton(text=texts.change_gpt_prompt_btn, callback_data="manage_prompt")],
        ]
    )
    return k
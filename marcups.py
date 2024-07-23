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


def admins_manage(names):
    btns = []
    for i,name in enumerate(names):
        line = [InlineKeyboardButton(text=name, callback_data=f"admin_{i}")]
        btns.append(line)
    back = [InlineKeyboardButton(text=texts.back_btn, callback_data="back")]
    btns.append(back)
    keyboard = InlineKeyboardMarkup(inline_keyboard=btns)
    return keyboard


def admin_edit():
    btns = []
    line = [InlineKeyboardButton(text=texts.remove_admin_btn, callback_data="remove_admin"),
            InlineKeyboardButton(text=texts.cancel_btn, callback_data="cancel")]
    btns.append(line)
    keyboard = InlineKeyboardMarkup(inline_keyboard=btns)
    return keyboard


def accounts_manage(names):
    btns = []
    for i,name in enumerate(names):
        line = [InlineKeyboardButton(text=name, callback_data=f"accounts_{i}")]
        btns.append(line)
    back = [InlineKeyboardButton(text=texts.back_btn, callback_data="back")]
    btns.append(back)
    keyboard = InlineKeyboardMarkup(inline_keyboard=btns)
    return keyboard


def accounts_edit():
    btns = []
    line = [InlineKeyboardButton(text=texts.remove_account_btn, callback_data="remove_account"),
            InlineKeyboardButton(text=texts.cancel_btn, callback_data="cancel")]
    btns.append(line)
    keyboard = InlineKeyboardMarkup(inline_keyboard=btns)
    return keyboard


def channels_manage(names):
    btns = []
    for i,name in enumerate(names):
        line = [InlineKeyboardButton(text=name, callback_data=f"channel_{i}")]
        btns.append(line)
    back = [InlineKeyboardButton(text=texts.back_btn, callback_data="back")]
    btns.append(back)
    keyboard = InlineKeyboardMarkup(inline_keyboard=btns)
    return keyboard


def channel_edit():
    btns = []
    line = [InlineKeyboardButton(text=texts.remove_channel_btn, callback_data="remove_channel"),
            InlineKeyboardButton(text=texts.cancel_btn, callback_data="cancel")]
    btns.append(line)
    keyboard = InlineKeyboardMarkup(inline_keyboard=btns)
    return keyboard
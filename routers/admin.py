from aiogram import F, Router, Bot
from aiogram.fsm.context import FSMContext
from pyrogram import Client
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
import marcups
from base_control import Control
from context import Context
import texts
from brain import Brain

admin_router = Router()
from aiogram.types.callback_query import CallbackQuery

BrainCore = Brain()
BaseController = Control()
_bot = Bot


def set_bot(bot: Bot):
    global _bot
    _bot = bot


@admin_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    id = str(message.from_user.id)
    print(id)
    await state.set_state(Context.start)
    if BaseController.check_admin_exists(id):
        text = texts.welcome_msg
        text = text.format(str(message.from_user.first_name))
        m = marcups.main_menu()
    else:
        text = texts.you_not_admin
        m = None
    await message.answer(text=text, reply_markup=m)


@admin_router.callback_query()
async def button_handler(callback: CallbackQuery, state: FSMContext):

    if BaseController.check_admin_exists(str(callback.from_user.id)):
        command = callback.data
    else:
        command = "error"

    if command == "error":
        await _bot.send_message(chat_id=callback.from_user.id, text=texts.you_not_admin)

from aiogram import  F, Router, Bot
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
group_router = Router()
_bot = None

def set_bot(bot: Bot):
    global _bot
    _bot = bot

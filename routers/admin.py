from aiogram import  F, Router
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from pyrogram import Client
from aiogram.filters import Command, CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from base_control import Control
from context import Context
import texts
from brain import Brain
admin_router = Router()

BrainCore = Brain()
BaseController = Control()


@admin_router.message(CommandStart())
async def command_start(message: Message, state: FSMContext) -> None:
    await
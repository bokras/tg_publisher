import asyncio
from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN
from routers.admin import admin_router
from routers.group import group_router





async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(admin_router)
    dp.include_router(group_router)
    await dp.start_polling(bot)








if __name__ == "__main__":
    asyncio.run(main())
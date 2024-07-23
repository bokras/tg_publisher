import asyncio
from aiogram import Dispatcher,Bot
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from config import TOKEN
import routers.admin
import routers.group





async def main():
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_router(routers.admin.admin_router)
    routers.admin.set_bot(bot)
    dp.include_router(routers.group.group_router)
    routers.group.set_bot(bot)
    await dp.start_polling(bot)








if __name__ == "__main__":
    asyncio.run(main())
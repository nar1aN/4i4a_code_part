import asyncio
from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.handlers import router

#основная часть запуска 
async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(router)
    print("Бот запущен. Напиши /start в Telegram.")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
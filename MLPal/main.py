import asyncio
from aiogram import Bot, Dispatcher

TOKEN = "8715118884:AAHlLD-8v42xFxr4kXgCAOqWJdL4cCBKZEE" 

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
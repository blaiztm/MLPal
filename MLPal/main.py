import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command

TOKEN = "8715118884:AAFKD-Then8321t_DZqiF8JxfsalucGn9Ws" 

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message):
    await message.answer("Hi fellow ML learner, what is your name?")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
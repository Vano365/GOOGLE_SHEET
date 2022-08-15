from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Text
from aiogram.utils.markdown import hbold, hlink
import asyncio
import psycopg2
from datetime import datetime
from config import *

bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
USERS_ID = BOT_USERS

async def task():
  while True:
    try:
        connection = psycopg2.connect(user=USER_DB,
                                    password=PASSWORD_DB,
                                    host=HOST_DB,
                                    port=PORT_DB,
                                    database=NAME_DB)

        cursor = connection.cursor()
        cursor.execute("SELECT * FROM main_orders")
        rows = cursor.fetchall()
        now = datetime.now().date()
        for i in USERS_ID:
            await bot.send_message(i, "Просроченые номера заказов: ")
            for row in rows:
                #print(row)
                date = row[3]
                if date < now:
                   await bot.send_message(i, str(row[1])) 
        await asyncio.sleep(86400)
    except Exception as e:
        print(str(e))
        await asyncio.sleep(100)
        continue

loop = asyncio.get_event_loop()
loop.create_task(task())
dp = Dispatcher(bot, loop=loop)

@dp.message_handler(commands="start")
async def start(message: types.Message):
    await message.answer("Привет")

def main():
    executor.start_polling(dp)

if __name__ == "__main__":
    main()

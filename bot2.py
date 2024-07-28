import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types.web_app_info import WebAppInfo
from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.types.callback_query import CallbackQuery

# Enable logging to avoid missing important messages
logging.basicConfig(level=logging.INFO)

# Bot object
bot = Bot(token="1834794957:AAF1Ab14a4KjIuJ8netTx9tT8rq-8r3pQAU")
# Dispatcher
dp = Dispatcher()

# Handler for the /start command
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(
                    text='Know more',
                    web_app=WebAppInfo(url='https://559f-213-109-66-248.ngrok-free.app')
                )],
        ]
    )
    await message.answer("Welcome to BITMAIN Shop 🚀\ntap the button below to check out the latest products!", reply_markup=keyboard)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

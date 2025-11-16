import aiogram
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


token="8431434594:AAGy0YyxqZnDBmX2D7xd-kmQchgT-9qZHaQ"
bot = Bot(token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start (message: types.Message):
    await message.answer (
        "Привет! Здесь ты можешь получить информацию обо мне пиши <b>ПРИСЫЛАЙ</b> или <b>НАРАБОТКИ</b> и ты получишь все что тебе нужно :)",
                          parse_mode="html"
    )


@dp.message(lambda m: m.text and m.text.lower() == 'присылай')
async def send_profile(message: types.Message):

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton (text="Открыть мой профиль Сетка", url="https://setka.ru/users/0199d972-d890-7720-a396-bf14142e96ef?view_from_feed=true&comment=true&utm_source=seo")],
                [InlineKeyboardButton (text="Открыть мой профиль Telegram", url="https://t.me/Tolantel")],
                [InlineKeyboardButton (text="Открыть мой профиль HH.ru", url="https://hh.ru/applicant/resumes?hhtmFrom=main&hhtmFromLabel=header")]
            ]
        )
        await message.answer("Выбери нужный профиль для изучения:", reply_markup=keyboard)

@dp.message(lambda m: m.text and m.text.lower() == 'наработки')
async def send_developments(message: types.Message):
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton (text="Мои наработки", url="https://github.com/FearawaitsTM")]
        ]
    )

    await message.answer("Мои наработки:", reply_markup=keyboard)

@dp.message()
async def bad_answer(message: types.Message):
    await message.answer(
        "Вы прислали не верные команды/n"
        "Вернитесь обратно с помощью кнопки '/start' и просмотрите команды заново",
    )

async def main():
    await dp.start_polling(bot)

asyncio.run(main())

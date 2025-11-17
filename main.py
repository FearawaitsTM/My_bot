import aiogram
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

bot = Bot("8431434594:AAGy0YyxqZnDBmX2D7xd-kmQchgT-9qZHaQ")
dp = Dispatcher()

def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Профиль', callback_data='profile'),
                InlineKeyboardButton (text='Наработки', callback_data='developments')
            ],
            [
                InlineKeyboardButton(text='Информация', callback_data='info'),
                InlineKeyboardButton(text="Моя карточка",web_app=WebAppInfo(url="https://setka.ru/"))
            ]
        ]
    )

def back_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton (text='⬅ Назад', callback_data='back')]
        ]
    )

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет! Здесь ты можешь получить информацию обо мне 🙂",
        reply_markup = main_menu()
    )


@dp.callback_query(lambda c: c.data and c.data.lower() == 'profile')
async def send_profile(callback: types.CallbackQuery):

        menu = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton (text="Сетка", url="https://setka.ru/users/0199d972-d890-7720-a396-bf14142e96ef?view_from_feed=true&comment=true&utm_source=seo"),
                    InlineKeyboardButton (text="Telegram", url="https://t.me/Tolantel")
                ],
                [
                    InlineKeyboardButton (text="HH.ru", url="https://hh.ru/applicant/resumes?hhtmFrom=main&hhtmFromLabel=header"),
                    InlineKeyboardButton(text="⬅ Назад", callback_data="back")
                ]
            ]
        )
        await callback.message.edit_text("Выбери нужный профиль:", reply_markup=menu)
        await callback.answer()

@dp.callback_query(lambda c: c.data and c.data.lower() == 'developments')
async def send_developments(callback: types.CallbackQuery):
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton (text="GitHub", url="https://github.com/FearawaitsTM")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back")]
        ]
    )

    await callback.message.edit_text("Мои наработки:", reply_markup = menu)
    await callback.answer()

@dp.callback_query(lambda c: c.data and c.data.lower() == 'bad')
async def bad_answer(message: types.Message):
    await message.answer(
        "Вы прислали не верные команды \n"
        "Вернитесь обратно с помощью кнопки '/start' и просмотрите команды заново",
    )

@dp.callback_query(lambda c: c.data == "info")
async def IRL_info(callback: types.CallbackQuery):

    text = (
        "Мне 19 лет\n"
        "Я учусь в университете МГУТУ\n"
        "Имею знания английского уровня B1\n"
        "Знаю языки программирования такие как: <b>Python, C++, HTML, CSS, JavaScript - на базовом уровне</b>\n"
        "Полный мой список языков: <b>TypeScript, Java, Dart, C, Ассемблер, PHP</b>"
    )

    await callback.message.edit_text(
        text,
        reply_markup=back_button(),
        parse_mode="HTML"
    )
    await callback.answer()


@dp.callback_query(lambda c: c.data and c.data.lower() == 'back')
async def go_back(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Привет! Здесь ты можешь получить информацию обо мне 🙂",
        reply_markup=main_menu()
    )
    await callback.answer()

@dp.message()
async def bad(message: types.Message):
    await message.answer("Нажмите кнопку /start. Текст не воспринимаю(")



async def main():
    await dp.start_polling(bot)

asyncio.run(main())

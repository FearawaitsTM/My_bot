import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

bot = Bot(TOKEN)))))
dp = Dispatcher()

OPERATOR_ID = bolshoe piska
active_chats = {}

def main_menu():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Профиль', callback_data='profile'),
                InlineKeyboardButton(text='Наработки', callback_data='developments'),
            ],
            [
                InlineKeyboardButton(text='Информация', callback_data='info'),
                InlineKeyboardButton(text="Моя карточка",web_app=WebAppInfo(url="https://setka.ru/"))
            ],
            [
                InlineKeyboardButton(text="Связаться с оператором", callback_data="operator")
            ]
        ]
    )

def back_button():
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text='⬅ Назад', callback_data='back')]
        ]
    )

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет! Здесь ты можешь получить информацию обо мне 🙂",
                         reply_markup=main_menu())

@dp.callback_query(lambda c: c.data == 'profile')
async def send_profile(callback: types.CallbackQuery):
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Сетка", url="https://setka.ru/users/0199d972-d890-7720-a396-bf14142e96ef"),
                InlineKeyboardButton(text="Telegram", url="https://t.me/Tolantel")
            ],
            [
                InlineKeyboardButton(text="HH.ru",
                                     url="https://hh.ru/applicant/resumes?hhtmFrom=main"),
                InlineKeyboardButton(text="⬅ Назад", callback_data="back")
            ]
        ]
    )
    await callback.message.edit_text("Выбери нужный профиль:", reply_markup=menu)
    await callback.answer()

@dp.callback_query(lambda c: c.data == 'developments')
async def send_developments(callback: types.CallbackQuery):
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="GitHub", url="https://github.com/FearawaitsTM")],
            [InlineKeyboardButton(text="⬅ Назад", callback_data="back")]
        ]
    )
    await callback.message.edit_text("Мои наработки:", reply_markup=menu)
    await callback.answer()

@dp.callback_query(lambda c: c.data == "info")
async def IRL_info(callback: types.CallbackQuery):
    text = (
        "Мне 19 лет\n"
        "Я учусь в университете МГУТУ\n"
        "Английский уровень B1\n"
        "Знаю: Python, C++, HTML, CSS, JavaScript\n"
        "Учусь: TypeScript, Java, Dart, C, Ассемблер, PHP"
    )
    await callback.message.edit_text(text, reply_markup=back_button(), parse_mode="HTML")
    await callback.answer()

@dp.callback_query(lambda c: c.data == 'back')
async def go_back(callback: types.CallbackQuery):
    await callback.message.edit_text("Привет! Здесь ты можешь получить информацию обо мне 🙂",
                                     reply_markup=main_menu())
    await callback.answer()

@dp.callback_query(lambda c: c.data == 'operator')
async def connect_operator(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    active_chats[user_id] = True
    await callback.message.edit_text(
        "Оператор подключён 💬\nПишите свои сообщения.\n\nНажмите «Отключиться» чтобы завершить чат.",
        reply_markup=InlineKeyboardMarkup(
            inline_keyboard=[[InlineKeyboardButton(text="❌ Отключиться",
                                                   callback_data="user_stop_chat")]]
        )
    )
    await bot.send_message(OPERATOR_ID, f"🟢 Новый чат!\nПользователь {user_id} подключился.")
    await callback.answer()

@dp.message(lambda m: m.from_user.id == OPERATOR_ID)
async def operator_message(message: types.Message):
    text = message.text.strip()

    if text.startswith("/stop"):
        try:
            _, user_id = text.split()
            user_id = int(user_id)
            if user_id in active_chats:
                del active_chats[user_id]
                await bot.send_message(user_id, "❌ Оператор завершил чат.")
                await bot.send_message(OPERATOR_ID, f"🔴 Чат с {user_id} завершён.")
            else:
                await message.answer("Пользователь не в чате.")
        except:
            await message.answer("Использование: /stop user_id")
        return

    try:
        uid, msg = text.split(" ", 1)
        uid = int(uid)
        if uid not in active_chats:
            await message.answer("Пользователь не в чате.")
            return
        await bot.send_message(uid, f"<b>Оператор:</b> {msg}", parse_mode="HTML")
    except:
        await message.answer("Формат: user_id сообщение")

@dp.message()
async def user_message(message: types.Message):
    user_id = message.from_user.id
    if user_id == OPERATOR_ID:
        return
    if user_id not in active_chats:
        return
    await bot.send_message(OPERATOR_ID, f"💬 Сообщение от {user_id}:\n{message.text}")

@dp.callback_query(lambda c: c.data == "user_stop_chat")
async def user_disconnect(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    if user_id in active_chats:
        del active_chats[user_id]
        await bot.send_message(OPERATOR_ID, f"🔴 Пользователь {user_id} отключил чат.")
    await callback.message.edit_text("Чат завершён.")
    await callback.answer()

async def main():
    await dp.start_polling(bot)

asyncio.run(main())

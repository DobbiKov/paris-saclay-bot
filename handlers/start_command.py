from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.start_keyboard import start_keyboard

from loader import dp

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message, state: FSMContext):
    await dp.bot.send_message(message.chat.id, "Hello! It's Paris-Saclay bot!", reply_markup=start_keyboard())
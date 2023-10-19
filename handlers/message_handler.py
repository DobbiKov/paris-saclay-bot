from aiogram import types
from aiogram.dispatcher import FSMContext
from modules.schedule import send_today_schedule, send_tomorrow_schedule
from handlers.week_schedule import send_week_schedule
from keyboards.inline.search_choose_category import search_choose_category

from loader import dp

@dp.message_handler(state="*")
async def message_handler(message: types.Message, state: FSMContext):
    if message.text == "⏰ Aujourd'hui":
        await send_today_schedule(message.chat.id, message.from_user.id, dp)
    if message.text == "⏰ Demain":
        await send_tomorrow_schedule(message.chat.id, message.from_user.id, dp)
    if message.text == "📅 Semaine":
        await send_week_schedule(message.chat.id, message.from_user.id, dp)
    # await dp.bot.send_message(message.chat.id, "Please, choose a category that concerns your request:", reply_markup=search_choose_category())
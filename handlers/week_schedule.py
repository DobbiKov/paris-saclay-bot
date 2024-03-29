from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from typing import List
import os

from modules.excel import Excel

from datetime import date, timedelta

from modules.send_day_schedule import send_day_schedule

async def send_week_schedule(chat_id, user_id, _dp):
    today = date.today()
    d0 = date(2024, 1, 8)
    delta = today - d0
    days_between = delta.days + 1

    week = (days_between // 7) + 1  # then we use number of weeks + the day on the next week()
    day = days_between % 7 
    if day > 5:
        week += 1
    for i in range(5):
        local_date = d0 + timedelta(days=days_between - day + i) 
        await send_day_schedule(local_date, i + 1, week, chat_id, user_id, _dp)

@dp.message_handler(commands=['week_schedule'])
async def week_schedule_command(message: types.Message, state: FSMContext):
    # add_announce = AddAnnounce("oneplus 8", "", "1000", "fdsafads", "dsfafasd", "Oneplus бери не хочу")
    # willhaben.add_announce(add_announce)
    await send_week_schedule(message.chat.id, message.from_user.id, dp)

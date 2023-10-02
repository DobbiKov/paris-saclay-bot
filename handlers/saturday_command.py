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

async def send_saturday_schedule(chat_id, _dp):
    today = date(2023, 9, 30)
    d0 = date(2023, 9, 11)
    delta = today - d0
    days_between = delta.days + 1

    week = (days_between // 7) + 1 # then we use number of weeks + the day on the next week()
    day = days_between % 7 
    await send_day_schedule(today, day, week, chat_id, _dp)

async def send_sunday_schedule(chat_id, _dp):
    tomorrow = date(2023, 9, 30) + timedelta(days=1)
    d0 = date(2023, 9, 11)
    delta = tomorrow - d0
    days_between = delta.days + 1

    week = (days_between // 7) + 1 # then we use number of weeks + the day on the next week()
    day = days_between % 7 
    await send_day_schedule(tomorrow, day, week, chat_id, _dp)

@dp.message_handler(commands=['sunday'])
async def sunday_schedule(message: types.Message, state: FSMContext):
    await send_sunday_schedule(message.chat.id, dp)

@dp.message_handler(commands=['saturday'])
async def saturday_command(message: types.Message, state: FSMContext):
    await send_saturday_schedule(message.chat.id, dp)

from datetime import date, timedelta

from modules.send_day_schedule import send_day_schedule

async def send_today_schedule(chat_id, user_id, _dp):
    today = date.today()
    d0 = date(2024, 1, 8)
    delta = today - d0
    days_between = delta.days + 1

    week = (days_between // 7) + 1 # then we use number of weeks + the day on the next week()
    day = days_between % 7 
    await send_day_schedule(today, day, week, chat_id, user_id, _dp)

async def send_tomorrow_schedule(chat_id, user_id, _dp):
    tomorrow = date.today() + timedelta(days=1)
    d0 = date(2024, 1, 8)
    delta = tomorrow - d0
    days_between = delta.days + 1

    week = (days_between // 7) + 1 # then we use number of weeks + the day on the next week()
    day = days_between % 7 
    await send_day_schedule(tomorrow, day, week, chat_id, user_id, _dp)

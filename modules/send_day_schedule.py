from modules.excel import Excel
from loader import database

def get_excel_row_for_week(week):
    return 5 + week
def excel_fields_for_day(day):
    if day > 5:
        return []
    days = [
        ["C", "D", "E", "F"],
        ["G", "H", "I", "J"],
        ["K", "L", "M", "N"],
        ["O", "P", "Q", "R"],
        ["S", "T", "U", "V"],
    ]
    return days[day-1]

def get_day_of_the_week_by_day(day) -> str:
    day_of_the_week = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]
    return day_of_the_week[day-1]

def get_excel_fields_for_day(day, week):
    if day > 5 or day == 0:
        return []
    row_week = get_excel_row_for_week(week)
    days = [
        ["C", "D", "E", "F"],
        ["G", "H", "I", "J"],
        ["K", "L", "M", "N"],
        ["O", "P", "Q", "R"],
        ["S", "T", "U", "V"],
    ]
    for i in range(len(days)):
        for j in range(len(days[i])):
            days[i][j] = days[i][j] + f'{row_week}'
    return days[day-1]

def get_batiment_salle(day):
    if day > 5:
        return []
    days_fields = excel_fields_for_day(day)
    for i in range(len(days_fields)):
        days_fields[i] = days_fields[i] + '5'
    return days_fields

def get_hours(day):
    if day > 5:
        return []
    days_fields = excel_fields_for_day(day)
    for i in range(len(days_fields)):
        days_fields[i] = days_fields[i] + '4'
    return days_fields

async def send_day_schedule(date, day, week, chat_id, user_id, _dp):
    excel = Excel()
    user = database.get_user(user_id)
    formation = user['FORMATION']
    excel.get_file(
        excel.get_formation_file(formation)
    )
    if user == None or len(user) == 0:
        return await _dp.bot.send_message(chat_id, f"Something went wrong, you're not in database! Please, write /start command!") 
    excel.get_sheet(
        excel.get_formation_sheet(formation)
    )

    # ex_week = get_excel_row_for_week(week)
    cours = get_excel_fields_for_day(day, week)
    if len(cours) == 0:
        return await _dp.bot.send_message(chat_id, f"<b>{get_day_of_the_week_by_day(day)} ({date})</b>:\nIl n'y a aucun cours.")
    
    text = f"<b>{get_day_of_the_week_by_day(day)} ({date}) ({formation})</b>:\n" 
    text += "==================\n"
    bat_salles = get_batiment_salle(day)
    hours = get_hours(day)
    for i in range(4):
        cours_text = excel.get_data_by_text(cours[i])
        if cours_text == None:
            continue
        text += excel.get_data_by_text(hours[i]) + "\n"
        text += f"{cours_text} ({excel.get_data_by_text(bat_salles[i])})\n"
        text += "==================\n"
    # await dp.bot.send_message(chat_id, f"Your schedule: days between {days_between}")
    await _dp.bot.send_message(chat_id, text, parse_mode="HTML")
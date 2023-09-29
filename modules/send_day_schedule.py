from modules.excel import Excel

def get_excel_row_for_week(week):
    return 6 + week
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
    day_of_the_week = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi"]
    return day_of_the_week[day-1]

def get_excel_fields_for_day(day, week):
    if day > 5:
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

async def send_day_schedule(date, day, week, chat_id, _dp):
    excel = Excel()
    excel.get_file()
    excel.get_sheet()

    # ex_week = get_excel_row_for_week(week)
    cours = get_excel_fields_for_day(day, week)
    if len(cours) == 0:
        return await _dp.bot.send_message(chat_id, f"<b>{get_day_of_the_week_by_day(day)} ({date})</b>:\nIl n'y a aucun cours.")
    
    text = f"<b>{get_day_of_the_week_by_day(day)} ({date})</b>:\n" 
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
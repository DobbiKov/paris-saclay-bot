from aiogram.types import ReplyKeyboardMarkup

def start_keyboard():
    keyboard = ReplyKeyboardMarkup()
    keyboard.row("⏰ Aujourd'hui", "📅 Semaine")
    return keyboard
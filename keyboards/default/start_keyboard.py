from aiogram.types import ReplyKeyboardMarkup

def start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("⏰ Aujourd'hui", "⏰ Demain")
    keyboard.row("📅 Semaine")
    return keyboard
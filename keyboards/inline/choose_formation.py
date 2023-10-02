# - *- coding: utf- 8 - *-
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def choose_fac_keyboard():
    button1 = InlineKeyboardButton("L1-Maths-Info", callback_data="choose_fac:L1-MI")
    button2 = InlineKeyboardButton("L1-Maths-Physic", callback_data="choose_fac:L1-MP")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(button1)
    keyboard.add(button2)
    
    return keyboard

def choose_formation_mi_keyboard():
    button1 = InlineKeyboardButton("L1-MI1", callback_data="choose_form:L1-MI1")
    button2 = InlineKeyboardButton("L1-MI2", callback_data="choose_form:L1-MI2")
    button3 = InlineKeyboardButton("L1-MI3", callback_data="choose_form:L1-MI3")
    button4 = InlineKeyboardButton("L1-MI4", callback_data="choose_form:L1-MI4")


    button5 = InlineKeyboardButton("LDD1-IM1", callback_data="choose_form:LDD1-IM1")
    button6 = InlineKeyboardButton("LDD1-IM2", callback_data="choose_form:LDD1-IM2")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(button1, button2)
    keyboard.add(button3, button4)
    keyboard.add(button5, button6)
    
    return keyboard

def choose_formation_mp_keyboard():

    button7 = InlineKeyboardButton("L1-MP-A1", callback_data="choose_form:L1-MP-A1")
    button8 = InlineKeyboardButton("L1-MP-A2", callback_data="choose_form:L1-MP-A2")
    button9 = InlineKeyboardButton("L1-MP-A3", callback_data="choose_form:L1-MP-A3")
    button10 = InlineKeyboardButton("L1-MP-B1", callback_data="choose_form:L1-MP-B1")
    button11 = InlineKeyboardButton("L1-MP-B2", callback_data="choose_form:L1-MP-B2")

    button12 = InlineKeyboardButton("LDD1-MPSI-B3", callback_data="choose_form:LDD1-MPSI-B3")
    button13 = InlineKeyboardButton("LDD1-MPSI-B4", callback_data="choose_form:LDD1-MPSI-B4")
    button14 = InlineKeyboardButton("LDD1-MPSI-STAPS-B5", callback_data="choose_form:LDD1-MPSI-STAPS-B5")

    keyboard = InlineKeyboardMarkup()
    keyboard.add(button7, button8, button9, button10, button11)
    keyboard.add(button12, button13, button14)
    
    return keyboard
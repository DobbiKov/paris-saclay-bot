from aiogram import types
from aiogram.dispatcher import FSMContext
from keyboards.default.start_keyboard import start_keyboard
from keyboards.inline.choose_formation import choose_fac_keyboard, choose_formation_mi_keyboard, choose_formation_mp_keyboard

from loader import dp
from modules.database import Database
from loader import database

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message, state: FSMContext):
    user = database.get_user(message.from_user.id)
    if(len(user) == 0):
        database.create_user(message.from_user.id, message.from_user.username or "", "L1-MI3")

    await dp.bot.send_message(message.chat.id, "Salut! C'est un bot de Paris Saclay pour l'emploi du temps!", reply_markup=start_keyboard())
    await dp.bot.send_message(message.chat.id, "Pour utiliser le bot, choisissez votre formation s'il vout plaît:", reply_markup=choose_fac_keyboard())

@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("choose_fac"), state="*")
async def callback_choose_fac_query_handler(call: types.CallbackQuery, state: FSMContext):
    """
    Process a category
    """
    fac = call.data.split(":")[-1]
    if fac == "L1-MI":
        return await dp.bot.send_message(call.message.chat.id, "Bien! Maintenant, choisissez votre group:", reply_markup=choose_formation_mi_keyboard())
    return await dp.bot.send_message(call.message.chat.id, "Bien! Maintenant, choisissez votre group:", reply_markup=choose_formation_mp_keyboard())


@dp.callback_query_handler(lambda callback_query: callback_query.data.startswith("choose_form"), state="*")
async def callback_choose_group_query_handler(call: types.CallbackQuery, state: FSMContext):
    """
    Process a category
    """
    formation = call.data.split(":")[-1]
    
    database.update_user_formation(call.from_user.id, formation)
    await call.message.reply(f"Cool! Vous avez choisi {formation} comme votre group!")
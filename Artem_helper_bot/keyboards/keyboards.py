from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from lexicon.lexicon import LEXICON_RU


#Создаем кнопки клавиатур
button_about_me: InlineKeyboardButton = InlineKeyboardButton(
    text='Обо мне', 
    callback_data='pressed_about_me')
button_services: InlineKeyboardButton = InlineKeyboardButton(
    text='Услуги',
    callback_data='pressed_services')
button_price_list: InlineKeyboardButton = InlineKeyboardButton(
    text='Прайс лист',
    callback_data='pressed_price_list')
button_contact_me: InlineKeyboardButton = InlineKeyboardButton(
    text='Связь со мной',
    url='https://t.me/callmesombure')

back_button: InlineKeyboardButton = InlineKeyboardButton(
    text='Назад',
    callback_data='pressed_back_button')

#Создем клиавиатуры
main_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[button_about_me],
                     [button_services],
                     [button_price_list],
                     [button_contact_me]])
back_button_keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(
    inline_keyboard=[[back_button]])
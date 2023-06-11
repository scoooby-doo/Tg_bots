from aiogram import Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Text, Command
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import main_keyboard, back_button_keyboard


#Инициализируем роутер
router: Router = Router()

#Хэндлер срабатывает на команду /start
@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'],
                         reply_markup=main_keyboard)

#Хэндлер срабатывает на команду /help
@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])

#Хэндлер реагирует на нажатия кнопки 'button_about_me'
@router.callback_query(Text(text='pressed_about_me'))
async def pressed_button_about_me(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['about_me'],
        reply_markup=back_button_keyboard)

#Хэндлер реагирует на нажатия кнопки 'button_services'
@router.callback_query(Text(text='pressed_services'))
async def pressed_button_services(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['services'],
        reply_markup=back_button_keyboard)

#Хэндлер реагирует на нажатия кнопки 'button_price_list'
@router.callback_query(Text(text='pressed_price_list'))
async def pressed_button_price_list(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['price_list'],
        reply_markup=back_button_keyboard)

#Хэндлер реагирует на нажатие кнопки 'back_button'
@router.callback_query(Text(text=['pressed_back_button']))
async def process_back_bn_pressed(callback: CallbackQuery):
    await callback.message.edit_text(text=LEXICON_RU['/start'],
                                     reply_markup=main_keyboard)
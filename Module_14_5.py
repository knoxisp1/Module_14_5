from pkgutil import get_data

from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from crud_functions import *

api = "7993073270:AAFjsMFNPo_sL-4wG7cuM_BCYIrgHJKNS6M"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())
kb_rp = ReplyKeyboardMarkup(resize_keyboard=True)
btn1 = KeyboardButton(text="Регистрация")
kb_rp.add(btn1)


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью',reply_markup=kb_rp)


@dp.message_handler(text="Регистрация")
async def sing_up(message):
    await message.answer("Введите имя пользователя(только латинский алфавит):")
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    user_exists =is_included(message.text)
    if not user_exists:
        await state.update_data(username=str(message.text))
        await message.answer("Введите свой email:")
        await RegistrationState.email.set()
    else:
        await message.answer("Пользователь существует,введите другое имя")


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=str(message.text))
    await message.answer("Введите свой возраст:")
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def set_age(message,state):
    await state.update_data(age=int(message.text))
    data=await state.get_data()
    username=data.get("username")
    email=data.get("email")
    age=data.get("age")
    add_user(username, email, age)
    await message.answer("Регистрация прошла успешно")
    await state.finish()


@dp.message_handler()
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение")


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


api = ""
bot = Bot(token = api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard = True)
button = KeyboardButton(text = 'Рассчитать')
button2 = KeyboardButton(text = 'Информация')
kb.add(button)
kb.add(button2)

InKb = InlineKeyboardMarkup()
Inbutton = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data = 'calories')
Inbutton2 = InlineKeyboardButton(text = 'Формулы рассчета', callback_data = 'formulas')
InKb.add(Inbutton)
InKb.add(Inbutton2)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer("Привет! Я бот помогающий твоему здоровью.", reply_markup = kb)

@dp.message_handler(text = 'Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup = InKb)


@dp.callback_query_handler(text = 'formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6.25 x рост (см) – 5 x возраст (г) + 5) x A)')
    await call.answer()


@dp.callback_query_handler(text = 'calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    if message.text.isdigit():
        await state.update_data(age=(message.text))
        await message.answer('Введите свой рост:')
        await UserState.growth.set()
    else:
        await message.answer('Пожалуйста, введите корректное число.')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    if message.text.isdigit():
        await state.update_data(growth=(message.text))
        await message.answer('Введите свой вес:')
        await UserState.weight.set()
    else:
        await message.answer('Пожалуйста, введите корректное число.')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    if message.text.isdigit():
        await state.update_data(weight=(message.text))
        data = await state.get_data()
        result = round(10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5 * 1.9)
        await message.answer(f'Ваша норма калорий {result}')
        await state.finish()
    else:
        await message.answer('Пожалуйста, введите корректное число.')

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start чтобы начать общение')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
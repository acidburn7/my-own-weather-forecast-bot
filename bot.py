from aiogram import Bot, Dispatcher, types, executor
import os
from dotenv import load_dotenv

from Weather import Weather

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
OPENWEATHER_KEY = os.getenv('OPENWEATHER_KEY')

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


async def main_menu():
    markup = types.reply_keyboard.ReplyKeyboardMarkup(row_width=2)
    btn1 = types.KeyboardButton('Погода в моем городе')
    btn2 = types.KeyboardButton('Погода в другом городе')
    btn3 = types.KeyboardButton('История')
    btn4 = types.KeyboardButton('Установить свой город')
    markup.add(btn1, btn2, btn3, btn4)
    return markup

@dp.message_handler(commands=['start'])
async def start_message(message):
    markup = await main_menu()
    
    text = f'Привет {message.from_user.first_name}, я бот, который расскажет тебе о погоде на сегодня'
    await message.answer(text, reply_markup=markup)

@dp.message_handler(regexp='Погода в моем городе')
async def get_user_city(message):
    markup = types.reply_keyboard.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Меню')
    # markup.add(btn1)
    # text = f'Я пока так не умею'

    weather = Weather(OPENWEATHER_KEY, 'Дмитров')
    weather_answer = weather.get_weather()
    
    await message.answer(weather_answer, reply_markup=markup)

@dp.message_handler(regexp='Погода в другом городе')
async def get_another_user_city(message):
    markup = types.reply_keyboard.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Меню')
    markup.add(btn1)
    text = f'Я пока так не умею'
    await message.answer(text, reply_markup=markup)

@dp.message_handler(regexp='История')
async def get_history(message):
    markup = types.reply_keyboard.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Меню')
    markup.add(btn1)
    text = f'Я пока так не умею'
    await message.answer(text, reply_markup=markup)

@dp.message_handler(regexp='Установить свой город')
async def set_own_town(message):
    markup = types.reply_keyboard.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton('Меню')
    markup.add(btn1)
    text = f'Я пока так не умею'
    await message.answer(text, reply_markup=markup)

# @dp.message_handler(regexp='Меню')
# async def 

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
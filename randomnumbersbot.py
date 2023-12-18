import telebot
import logging
import random
from telebot import types

# Настройка логгирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Инициализация бота
TOKEN = '6553010317:AAFDz5vAFTcB2KHr_ERID4mrwsD_-GX-3I0'  # Твой токен
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть! В этом боте ты можешь сгенерировать случайное число! Напиши команду /help чтобы узнать команды :)')

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '1. /random30 - Рандом от 1 до 30.\n2. /random50 - Рандом от 1 до 50.\n3. /random100 - Рандом от 1 до 100.\n4. /random500 - Рандом от 1 до 500.\n5. /random1000 - Рандом число от 1 до 1000.\n6. /random - Случайное сгенерированое число.')

# Обработчик команды /random
@bot.message_handler(commands=['random30'])
def random_number(message):
    random_num = random.randint(1, 30)  # Генерируем случайное число от 1 до 30
    bot.send_message(message.chat.id, f'Вот твое случайное число: {random_num}')

# Обработчик команды /random
@bot.message_handler(commands=['random50'])
def random_number(message):
    random_num = random.randint(1, 50)  # Генерируем случайное число от 1 до 50
    bot.send_message(message.chat.id, f'Вот твое случайное число: {random_num}')

# Обработчик команды /random
@bot.message_handler(commands=['random100'])
def random_number(message):
    random_num = random.randint(1, 100)  # Генерируем случайное число от 1 до 100
    bot.send_message(message.chat.id, f'Вот твое случайное число: {random_num}')

# Обработчик команды /random
@bot.message_handler(commands=['random500'])
def random_number(message):
    random_num = random.randint(1, 500)  # Генерируем случайное число от 1 до 500
    bot.send_message(message.chat.id, f'Вот твое случайное число: {random_num}')

# Обработчик команды /random
@bot.message_handler(commands=['random1000'])
def random_number(message):
    random_num = random.randint(1, 1000)  # Генерируем случайное число от 1 до 1000
    bot.send_message(message.chat.id, f'Вот твое случайное число: {random_num}')

# Обработчик команды /random
@bot.message_handler(commands=['random'])
def random_number(message):
    random_num = random.randint(1, 99999999999999999999999999999999999999)  # Генерируем случайное число
    bot.send_message(message.chat.id, f'Вот твое случайное число: {random_num}')

# Запуск бота
bot.polling()


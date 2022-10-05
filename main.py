import telebot
import random
import time
from telebot import types
zz = 0, 1, 2, 3, 4
b = 'Жми на кнопки чудила)'
f = open('facts.txt', 'r', encoding='ANSI')
facts = f.read().split('\n')
f.close()
f = open('joke.txt', 'r', encoding='UTF-8')
joke = f.read().split('*****')
f.close()
f = open('films.txt', 'r', encoding='UTF-8')
films = f.read().split('\n')


TOKEN = "5467507762:AAELfQLpnrfCKBWVl3GiZr2D8aodlwxaSNg"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Факт")
    item2 = types.KeyboardButton("Шутка")
    item3 = types.KeyboardButton("Фильм")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, 'Нажми: \nФакт для получения интересного факта\nШутка - для анекдота)\nИли выбери кино в формате название и год выхода', reply_markup=markup)


@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip() == 'Факт':
        answer = random.choice(facts)
    elif message.text.strip() == 'Шутка':
        answer = random.choice(joke)
    elif message.text.strip() == 'Фильм':
        answer = random.choice(films)
    else:
        answer = b
    time.sleep(random.choice(zz))
    bot.send_message(message.chat.id, answer)


try:
    bot.polling(none_stop=True, interval=0)
except Exception:
    pass

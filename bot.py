import random

import telebot
from script import parse_products, generate_links, parse_fb
from database import select_feedbacks
from excel import create_table
import datetime

bot = telebot.TeleBot(token=your token)

@bot.message_handler(commands=['start'])
def greeting(message):
    msg = bot.send_message(message.chat.id,text='Отправьте мне ссылку на категорию!')
    bot.register_next_step_handler(msg,parse)
def parse(message):
    url = message.text
    parse_fb(url=url)
    filename = f'result{random.randint(0,999999)}'
    create_table(filename=filename)

    f = open(filename,"rb")
    bot.send_document(message.chat.id, f)


if "__main__" == __name__:
    bot.polling()

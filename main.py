import requests
import random
from bs4 import BeautifulSoup as b
import telebot

URL = 'https://www.anekdot.ru/last/good/'
API_KEY = '6222025029:AAHj_dN0sJOTKtMv33Z2olrrpsp6G-3zGwo'

def parser(url):
    r = requests.get(url)
    soup = b(r.text, 'html.parser')
    jokes = soup.find_all('div', class_ = 'text')
    return [joke.text for joke in jokes]

jokes_list = parser(URL)
random.shuffle(jokes_list)

bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])

def hello(message):
    bot.send_message(message.chat.id, 'Привет! Могу отправить тебе анекдоты')

@bot.message_handler(content_types=['text'])


def jokes(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, jokes_list[0])
        del jokes_list[0]
    else:
        bot.send_message(message.chat.id, 'Я вас не понял, пожалуйста введите любую цифру')



bot.polling()

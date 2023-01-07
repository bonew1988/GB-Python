import os
import requests
import telebot

os.system('clear')

TOKEN = '5846844230:AAEvAYzZR1ms5RWuIF7Dxs7K7PP3nEcmpYw'
bot = telebot.TeleBot(TOKEN)

def request_valute(data):
    printed_message = []
    if data == 1:
        req_data = 'USD'
    elif data == 2:
        req_data = 'EUR'
    elif data == 3:
        req_data = 'GBP'
    elif data == 4:
        req_data = 'BYN'
    res = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    printed_message.append((res['Valute'][req_data]['Name'], res['Valute'][req_data]['Value']))
    return printed_message

@bot.message_handler(commands=['menu'])
def start_message(message):
    bot.send_message(message.chat.id, 'Выберите валюту:\n'+
    '-----------------------------------------\n'+
    '1 - Доллар США\n'+
    '2 - Евро\n'+
    '3 - Фунт стерлингов Соединенного королевства\n'+
    '4 - Белорусский рубль\n'+
    '-----------------------------------------')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == '1' or message.text == '2' or message.text == '3' or message.text == '4':
        bot.send_message(message.chat.id, f'{request_valute(int(message.text))}')
    else:
        bot.send_message(message.chat.id, 'Некорректный ввод')

bot.infinity_polling()
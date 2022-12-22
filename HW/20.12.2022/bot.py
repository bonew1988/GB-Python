# import os
# os.system('clear')

import telebot
bot = telebot.TeleBot("5846844230:AAEvAYzZR1ms5RWuIF7Dxs7K7PP3nEcmpYw")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    lst = [i for i in message.text.split() if 'абв' not in i]
    bot.reply_to(message, ' '.join(lst))

bot.infinity_polling()

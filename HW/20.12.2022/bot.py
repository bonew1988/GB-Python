# import os
# import telebot
# import game

# bot = telebot.TeleBot("5846844230:AAEvAYzZR1ms5RWuIF7Dxs7K7PP3nEcmpYw")

# @bot.message_handler(commands=['start', 'help'])
# def send_welcome(message):
# 	bot.reply_to(message, "Howdy, how are you doing?")

# bot.infinity_polling()

import telebot
import game

bot = telebot.TeleBot("5846844230:AAEvAYzZR1ms5RWuIF7Dxs7K7PP3nEcmpYw")

@bot.message_handler(content_types=['text', 'document', 'audio'])

def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")
    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")








bot.polling(none_stop=True, interval=0)
import telebot
import os

token = os.environ.get('TELEGRAM_TOKEN', '')
states = {}

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_cmd(message):
    bot.send_message(message.chat.id, 'Hello!')


bot.polling()

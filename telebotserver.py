import telebot
import time
import requests
import configparser
import logging.config

config = configparser.SafeConfigParser()
config.read('server.conf')
token = config.get('server','token')

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['help'])
def send_help(message):
    logger.debug(message.chat.id)
    text = ('帮助\n')
    bot.send_message(message.chat.id,text)
    
@bot.message_handler()
def echo(message):
    bot.reply_to(message, message.text)
    
if __name__ == '__main__':
    logger.debug('telebot start...')
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            time.sleep(15)

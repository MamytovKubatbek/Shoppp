from django.core.management.base import BaseCommand
import telebot
TOKEN = '5753864361:AAEerBmg_H0BOJb4G1bOTGIooqL3L0_FHuE'
bot = telebot.TeleBot(TOKEN)




@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message.chat.id, 'Привет!')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)


class Command(BaseCommand):
    help = 'Телеграм-бот'

    def handle(self, *args, **options):
        bot = telebot.TeleBot(token=TOKEN)
        bot.get_updates(timeout=15)
        bot.polling()

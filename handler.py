import telebot

bot = telebot.TeleBot("314688077:AAE9ko_pksYCe0IoI1P15X71NTUxFJKi_vQ");
@bot.message_handler(commands = ['start'])
def send_welcome(message):
	bot.reply_to(message, "Куриленко лох")
	
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)
	
bot.polling()
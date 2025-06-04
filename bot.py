import telebot

TOKEN = "7719653484:AAE1bm7UOml43wb9EdlLVdErFus2TM2Jmfo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou seu bot hospedado na Render!")

bot.polling()

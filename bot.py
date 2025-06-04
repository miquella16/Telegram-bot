import telebot

TOKEN = "7719653484:AAE1bm7UOml43wb9EdlLVdErFus2TM2Jmfo"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou seu bot que vai comer você!")

bot.polling()

@bot.message_handler(commands=['oi'])
def diga_oi(mensagem):
    bot.send_message(mensagem.chat.id, "Olá! Como posso ajudar?")

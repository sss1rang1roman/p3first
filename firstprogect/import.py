import telebot

API_TOKEN = '8436897050:AAFZwr9CEZRlAarFIMR0A2Bwix16GIjnJlc'

bot = telebot.TeleBot(API_TOKEN)



@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['info'])
def send_welcome(message):
   
    text = """\
Hi i like to tell about weather, ohh yeasss\
"""
    
    try:
     
        with open('img/2 test lol.webp', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption=text)

    except FileNotFoundError:
 
        bot.reply_to(message, text + "\n\n(Фотография не найдена)")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, message.text)


bot.infinity_polling()
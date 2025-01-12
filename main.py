import telebot
import os
import random 

# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7457293771:AAHZjYKL0bB5UeGltCQ3rGgipm-FwMHK3lk")
    
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")
    
@bot.message_handler(commands=['hello'])
def send_hello(message):
    bot.reply_to(message, "Привет! Как дела?")
    
@bot.message_handler(commands=['bye'])
def send_bye(message):
    bot.reply_to(message, "Пока! Удачи!")

@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Здесь вы можете увидеть сколько разлогаются некоторые виды мусора.Команды: food waste,paper,textile products,glass.")

@bot.message_handler(commands=['food waste'])
def send_food(message):
    bot.reply_to(message, "От одной недели до нескольких лет")

@bot.message_handler(commands=['paper'])
def send_paper(message):
    bot.reply_to(message, "От двух недель до шести месяцев")

@bot.message_handler(commands=['textile products'])
def send_textile(message):
    bot.reply_to(message, "От одного месяца до двухсот лет")

@bot.message_handler(commands=['glass'])
def send_glass(message):
    bot.reply_to(message, "разлогается в течении нескольких тысяч лет")

@bot.message_handler(commands=['rules'])
def send_mem(message):
    rules = os.listdir('rules')
    img_name = random.choice(rules)
    with open(f'rules/{img_name}', 'rb') as f:   
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['mem'])
def send_mem(message):
    images = os.listdir('images')
    img_name = random.choice(images)
    with open(f'images/{img_name}', 'rb') as f:   
        bot.send_photo(message.chat.id, f)

@bot.message_handler(commands=['animals'])
def send_animals(message):
    animals = os.listdir('animals')
    img_name = random.choice(animals)
    with open(f'animals/{img_name}', 'rb') as f:   
        bot.send_photo(message.chat.id, f)
    
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()

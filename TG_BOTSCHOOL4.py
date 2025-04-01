import telebot
from telebot import types

bot = telebot.TeleBot('7849120078:AAEHYzZSQKHpNd4UltD9hW0ydw-zqFxbcVc') 


@bot.message_handler(commands = ['start'])
def start_message(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

    item1 = types.KeyboardButton("О боте")
    item2 = types.KeyboardButton("Credit")
    item3 = types.KeyboardButton("Сохранить")
    item4 = types.KeyboardButton("Загрузка")

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Привет, {0.first_name}. Это тест бота, а точнее заготовка для дальнейшего использования. С помощью кнопок Вы сможете узнать больше '.format(message.from_user), reply_markup = markup)
    
@bot.message_handler(func=lambda message: message.text == "О боте")
def abtBot(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        bot.send_message(message.chat.id, 'Этот бот является моим школьным проектом. Его основная функция это, конечно же, выполнение роли показа проекта и возможностей. Главное что он умеет это загрузка и сохранение Ваших файлов. Полный код на Github см. Credit ', reply_markup= markup)
@bot.message_handler(func=lambda message: message.text == "Credit")
def abtBot(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        bot.send_message(message.chat.id, 'Г', reply_markup= markup)

bot.infinity_polling()
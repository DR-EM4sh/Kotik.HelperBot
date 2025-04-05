import telebot
from telebot import types
import time
bot = telebot.TeleBot('7849120078:AAEHYzZSQKHpNd4UltD9hW0ydw-zqFxbcVc') 
bot.set_webhook()

@bot.message_handler(commands = ['start'])
def start_message(message): 
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

    item1 = types.KeyboardButton("О боте")
    item2 = types.KeyboardButton("Credits")
    item3 = types.KeyboardButton("Функции")
    item4 = types.KeyboardButton("Загрузка")

    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id, 'Привет, *{0.username}*. Я - бот для помощи в администрации каналов. Можете использовать кнопки.'.format(message.from_user), reply_markup = markup, parse_mode= 'Markdown')
    
@bot.message_handler(func=lambda message: message.text == "О боте")
def abtBot(message):
        bot.send_message(message.chat.id, 'Этот бот является моим школьным проектом и помощником для администрации каналов. Полный код на Github см. Credits ')

@bot.message_handler(func=lambda message: message.text == "Гладить")
def abtBot(message):
        name = message.from_user.username
        bot.send_message(message.chat.id, f'*{name}* погладил(-а) кота',parse_mode= 'Markdown')

@bot.message_handler(func=lambda message: message.text == "Credits")
def abtBot(message):
        bot.send_message(message.chat.id, '[Код для бота](https://github.com/DR-EM4sh/Kotik.HelperBot)',parse_mode ='Markdown')

@bot.message_handler(func=lambda message: message.text == "Функции")
def abtBot(message):
        bot.send_message(message.chat.id, '*Кик* - как понятно, кикнуть бунтовщика. \n*Мут/Инмут* - заставит замолчать неугомонных спамеров (или наоборот). \nИ самое главное - *Гладить*',parse_mode= 'Markdown')

@bot.message_handler(func=lambda message: message.text == "Загрузка")
def abtBot(message):
        bot.send_message(message.chat.id, '*Когда-нибудь* (а может и никогда)',parse_mode ='Markdown')

@bot.message_handler(content_types=["new_chat_members"])
def new_member(message):
    name = message.new_chat_members[0].username
    if name == "Kotik.Helper":
        bot.send_message(message.chat.id, "Привет, теперь я буду здесь :3 ")  
    else:
         bot.send_message(message.chat.id, f"Приветик, *{name}*! Добро пожаловать :3",parse_mode= 'Markdown')

@bot.message_handler(func=lambda message: message.text == "Кик")
def kick_ppl(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        user_id1 = message.from_user.id
        user_status1 = bot.get_chat_member(chat_id, user_id1).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно кикнуть админа.")
        elif user_status1 != 'administrator' or user_status != 'creator':
             bot.reply_to(f"*{message.from_user.username}*, вы не админ.", parse_mode = 'Markdown')
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"*{message.reply_to_message.from_user.username}* был кикнут.", parse_mode = 'Markdown')
    else:
        bot.reply_to(message, "Используйте команду в ответ на чье-то сообщение")

@bot.message_handler(func=lambda message: message.text == "Мут")
def mute_bunt(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        user_id1 = message.from_user.id
        user_status1 = bot.get_chat_member(chat_id, user_id1).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно замутить админа.")
        elif user_status1 != 'administrator' or user_status1 != 'creator':
             bot.reply_to(f"*{message.from_user.username}*, вы не админ.", parse_mode = 'Markdown')
        else:
            duration = 60
            args = message.text.split()[1:]
            if args:
                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Введите время *правильно*.", parse_mode = 'Markdown')
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть *положительным числом*.", parse_mode = 'Markdown')
                    return
                if duration > 1440:
                    bot.reply_to(message, "Нельзя больше дня")
                    return
            bot.restrict_chat_member(chat_id, user_id, until_date=time.time()+duration*60)
            bot.reply_to(message, f"*{message.reply_to_message.from_user.username}* замучен на *{duration}* минут.",parse_mode = 'Markdown')
    else:
        bot.reply_to(message, "Используйте команду в ответ на чье-то сообщение")
@bot.message_handler(func=lambda message: message.text == "Инмут")
def unmute_bunt(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_id1 = message.from_user.id
        user_status1 = bot.get_chat_member(chat_id, user_id1).status
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"*{message.reply_to_message.from_user.username}* размучен.",parse_mode = 'Markdown')
    elif user_status1 != 'administrator' or user_status1 != 'creator':
         bot.reply_to(f"*{message.from_user.username}*, вы не админ.", parse_mode = 'Markdown')
    else:
        bot.reply_to(message, "Используйте команду на сообщение того, кого хотите размутить")

bot.infinity_polling()

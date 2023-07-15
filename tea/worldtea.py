import telebot
from telebot import types
from datatea import *

bot = telebot.TeleBot(token)

def send_photo(message):
    photo = open(f'C:/Users/user752/OneDrive/Desktop/pyBots/tea/tea/{message.text}/1.jpg', 'rb')
    bot.send_photo(message.chat.id, photo)
     

def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Наши цены")
    button3 = types.KeyboardButton("Купить чай")
    markup.row(button1, button3)
    bot.send_message(message.chat.id, hello_message_rus, reply_markup=markup)



def button_tea_about_desc(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ar: types.KeyboardButton = []
    back = types.KeyboardButton("Назад")
    for i in dictObject.values():
        ar.append(types.KeyboardButton(i.name))
    markup.row(ar[0],ar[1],ar[2])
    markup.row(ar[3],ar[4],ar[5])
    markup.row(ar[6],ar[7],ar[8])
    markup.row(ar[9],ar[10])
    
    markup.add(back)
    bot.send_message(message.chat.id, "Выберите чай", reply_markup=markup)


def button_tea_about_price(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ar: types.KeyboardButton = []
    back = types.KeyboardButton("Назад")
    for i in dictObject.values():
        ar.append(types.KeyboardButton(i.name))
    markup.row(ar[0],ar[1],ar[2])
    markup.row(ar[3],ar[4],ar[5])
    markup.row(ar[6],ar[7],ar[8])
    markup.row(ar[9],ar[10])
    
    markup.add(back)
    bot.send_message(message.chat.id, "Выберите чай", reply_markup=markup)


#goto menu

def back_to_menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("Наши цены")
    button3 = types.KeyboardButton("Купить чай")
    markup.row(button1, button3)
    bot.send_message(message.chat.id, "Возвращаем в меню", reply_markup=markup)


def contacts(message):
    bot.send_message(message.chat.id, 'Писать сюда: @prostoalt')


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    button_message(message)
    



def price_about_tea(message):
    bot.send_message(message.chat.id, f'{dictObject[message.text].get()}')
    send_photo(message)

@bot.message_handler(content_types='text')
def say(message):
    if message.text == "Назад":
        back_to_menu(message)
    if message.text == "Купить чай":
        contacts(message)
    if message.text == 'Наши цены':
        button_tea_about_price(message)
    if message.text in names_of_tea_desc:
        price_about_tea(message)
    if message.text == "Фото":
        send_photo(message)
bot.infinity_polling()
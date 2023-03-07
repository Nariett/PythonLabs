import telebot
import random
from telebot import types
import time
admin_id = '******************'

bot = telebot.TeleBot('************************************')
web = "https://azs.belorusneft.by/sitebeloil/ru/center/azs/center/fuelandService/price/"


def price():#функия для обновления информации о топливе
    from bs4 import BeautifulSoup
    import requests
    requests = requests.get(web)
    html = BeautifulSoup(requests.text,"html.parser")
    fuel = html.find("div", class_="b-left__informer")
    test =fuel.find_all('td')
    price = []
    for el in test:
        price.append(el.get_text())
    return price

def select(index,price):
    file = open('C:\\Users\\Sasha\\Desktop\\FuelPrice.txt','r')
    list = []
    for x in file.readlines():
        list.append(x.replace('\n',''))
    if (float(price) <  float(list[index])):###новая цена и старая
        return 1
    elif (float(price) == float(list[index])):
        return 2
    else:
        return 3

def addFile(price):
    f = open('C:\\Users\\Sasha\\Desktop\\FuelPrice.txts','w')
    for index in price:
        f.writelines(str(index)+'\n') 


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("АИ-92")
    btn2 = types.KeyboardButton("АИ-95")
    btn3 = types.KeyboardButton("АИ-98")
    btn4 = types.KeyboardButton("ДТ")
    btn5 = types.KeyboardButton("ДТ-32°")
    btn6 = types.KeyboardButton("ДТ ECO")
    markup.add(btn1, btn2,btn3,btn4,btn5,btn6)
    bot.send_message(message.chat.id, text="Выберите желаемый тип топлива",reply_markup=markup)   
@bot.message_handler(commands=["help"])
def help(m, res=False):
    bot.send_message(m.chat.id, 'Вы запутались? Бот может помочь вам с просмотром цен на топливо на заправке БЕЛОРУСНЕФТЬ')
@bot.message_handler(content_types=["text"])
def text(message):
    if(message.text == "АИ-92"):
        info(int(1),str(message.chat.id))
    elif(message.text == "АИ-95"):
        info(int(2),str(message.chat.id))
    elif(message.text == "АИ-98"):
        info(int(3),str(message.chat.id))
    elif(message.text == "ДТ"):
        info(int(4),str(message.chat.id))
    elif(message.text == "ДТ-32°"):
        info(int(5),str(message.chat.id))
    elif(message.text == "ДТ ECO"):
        info(int(6),str(message.chat.id))
def info(index,user):
    bot.send_message(user, text="Цена: "+ price()[index])
bot.polling(none_stop=True, interval=0)
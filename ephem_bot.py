"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from datetime import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn', 
        'password': 'python'
    }
}


def greet_user(bot, update):
    text = 'Зачем меня призвали?'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print("Сейчас подумаю и отвечу...")
    update.message.reply_text(user_text)

def constellation_check(bot, update):
    planet = update.message.text.split()[1].capitalize()
    constellations = {"Mercury": ephem.constellation(ephem.Mercury(datetime.now())), 
                      "Venus": ephem.constellation(ephem.Venus(datetime.now())), 
                      "Earth": ephem.constellation(ephem.Earth(datetime.now())), 
                      "Mars": ephem.constellation(ephem.Mars(datetime.now())), 
                      "Jupiter": ephem.constellation(ephem.Jupiter(datetime.now())), 
                      "Saturn": ephem.constellation(ephem.Saturn(datetime.now())), 
                      "Uranus": ephem.constellation(ephem.Uranus(datetime.now())), 
                      "Neptune": ephem.constellation(ephem.Neptune(datetime.now())), }
    text_for_user = constellations.get(planet)
    print(text_for_user)
    update.message.reply_text(text_for_user)
 

def main():
    mybot = Updater("1024352282:AAEcDQlc1GxaeO-GMnnJ0BrsynZMuCShuMY", request_kwargs=PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    dp.add_handler(CommandHandler("planet", constellation_check))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()

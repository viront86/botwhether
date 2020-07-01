# Подключаем модуль случайных чисел 
import random

from pyowm import OWM
owm = OWM('8f34384a241507c3923818d782e01af5')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Kazan, RU')
w = observation.weather
b = w.temperature('celsius')['temp']

# Подключаем модуль для Телеграма

import telebot

# Указываем токен

bot = telebot.TeleBot('1346032549:AAGTflQ7YHtcxllSvc7mjXFuEbFwXYoBfR4')

 
# Импортируем типы из модуля, чтобы создавать кнопки

from telebot import types

 
first = w
 
# Метод, который получает сообщения и обрабатывает их

@bot.message_handler(content_types=['text'])

def get_text_messages(message):

    # Если написали «Привет»

    if message.text == "Привет":

        # Пишем приветствие

        bot.send_message(message.from_user.id, "Привет, сейчас я расскажу тебе идти на обед или нет.")

        # Готовим кнопки

        keyboard = types.InlineKeyboardMarkup()

        

        key_pogoda = types.InlineKeyboardButton(text='Погода', callback_data='pogoda')

        # И добавляем кнопку на экран

        keyboard.add(key_pogoda)

        

        
        # Показываем все кнопки сразу и пишем сообщение о выборе

        bot.send_message(message.from_user.id, text='Нажми на кнопку что бы узнать результат', reply_markup=keyboard)

    elif message.text == "/help":

        bot.send_message(message.from_user.id, "Напиши Привет")

    else:

        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

 
# Обработчик нажатий на кнопки

@bot.callback_query_handler(func=lambda call: True)

def callback_worker(call):

    

    if call.data == "pogoda": 

        
        
        # Отправляем текст в Телеграм

    
        bot.send_message(call.message.chat.id, "Возле нашей любимой Рябины  " +str(b)+ " градусов" )

    if b<15:
        bot.send_message(call.message.chat.id, "Ну это просто П*здец как холодно, это что лето?" )
    elif b>15 and b<23:
        bot.send_message(call.message.chat.id, "Ой хорошо, можно и в столовку пойти" )
    elif b>23:
        bot.send_message(call.message.chat.id, "ЖАРА!!!" )
         
        

 
# Запускаем постоянный опрос бота в Телеграме

bot.polling(none_stop=True, interval=0)






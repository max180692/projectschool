import telebot
from telebot import types
import settings
from generateprimer import GeneratePrimer

API_KEY = settings.API_TOKEN
bot = telebot.TeleBot(API_KEY)

registers_users = {}


#сделать счет правильных ответов

#

#функция создания кнопок по выбору примеров
def button_enter_numbers():
    keyboard = types.ReplyKeyboardMarkup(row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in settings.tuple_buttons])
    #button_clear = types.KeyboardButton("Удалить очки")
    #button_get_count = types.KeyboardButton("Показать очки")
    #keyboard.add(button_get_count)
    #keyboard.add(button_clear)
    return keyboard
#функция создания кнопок выбора варианта ответа
def button_numbers(variants_answers):
    keyboard = types.ReplyKeyboardMarkup(row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in variants_answers])
    button = types.KeyboardButton("Назад")
    keyboard.add(button)
    return keyboard

#функция по выбору действия + или -
def button_action():
    keyboard = types.ReplyKeyboardMarkup(row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in settings.tuple_action])
    button = types.KeyboardButton("В начало")
    #button_clear = types.KeyboardButton("Удалить очки")
    #button_get_count = types.KeyboardButton("Показать очки")
    #keyboard.add(button_get_count)
    #keyboard.add(button_clear)
    keyboard.add(button)
    return keyboard


def close_button_action():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Назад')
    keyboard.add(button)
    return keyboard

def registration():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Начать')
    keyboard.add(button)
    return keyboard



#нажатие кнопки старт регистрация пользователя в системе для дальнейшей генерации примеров
@bot.message_handler(commands=['start'])
def start(message):
    registers_users[message.from_user.id] = GeneratePrimer()
    print(registers_users)
    bot.send_message(message.chat.id, "Привет этот бот поможет тебе тренировать примеры на сложение и вычитание чисел. \n Выбери примеры ниже  ", reply_markup=button_enter_numbers())

#слушатель сообщений, которые поступают в телеграмм бот
@bot.message_handler(content_types='text')
def answer(message):
    if message.from_user.id not in registers_users:
        bot.send_message(message.chat.id,"Нажми на кнопку \"Начать\"",reply_markup=registration())
    else:
        #какие примеры будут генерироваться
        if message.text in settings.tuple_buttons:
            registers_users[message.from_user.id].set_sostav_chisla(settings.tuple_sostav_chisel[settings.tuple_buttons.index(message.text)])
            bot.send_message(message.chat.id, "Выбери, что ты будешь делать\n если складывать то нажми на \"+\" \n если вычитать то нажми на \"-\"",reply_markup=button_action())

        #какое дейтствие будет выполняться
        if message.text in settings.tuple_action:
            registers_users[message.from_user.id].enter_action(settings.tuple_action[settings.tuple_action.index(message.text)])
            registers_users[message.from_user.id].get_random_index()
            primer = registers_users[message.from_user.id].get_random_primer()
            result = registers_users[message.from_user.id].get_answer()
            bot.send_message(message.chat.id,primer,reply_markup=button_numbers(result['variants_answers']))

        #возврат на выбор действия
        if message.text == 'Назад':
            registers_users[message.from_user.id].clear_count()
            bot.send_message(message.chat.id, "Выбери что ты будешь делать\n если складывать то нажми на \"+\" \n если вычитать то нажми на \"-\"",reply_markup=button_action())
        
        if message.text == 'В начало':
            bot.send_message(message.chat.id, "Выбери примеры ниже",reply_markup=button_enter_numbers())
        
        
        
        #проверка, что в тексте есть только числа 
        if message.text.isdigit() and message.from_user.id in registers_users:
            proverka_otveta = registers_users[message.from_user.id].answers(message.text)
            bot.send_sticker(message.chat.id,proverka_otveta['stiker'])
            bot.send_message(message.chat.id,proverka_otveta['message'])
            #bot.clear_reply_handlers(message)
            primer = registers_users[message.from_user.id].get_random_primer()
            result = registers_users[message.from_user.id].get_answer()
            #print(result.__class__.__name__)
            #print(result)
            if result.__class__.__name__ == 'dict' and primer.__class__.__name__ == 'str':
                bot.send_message(message.chat.id,primer,reply_markup=button_numbers(result['variants_answers']))
            else:
                bot.send_sticker(message.chat.id,primer['stiker'])
                bot.send_message(message.chat.id,primer['message'],reply_markup=close_button_action())
    #            
                
    if message.text == 'Начать':
        registers_users[message.from_user.id] = GeneratePrimer()
        bot.send_message(message.chat.id, "Привет этот бот поможет тебе тренировать примеры на сложение и вычитание чисел. \n Выбери примеры ниже  ", reply_markup=button_enter_numbers())


def main():
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(e)
            bot.polling(none_stop=True, interval=0) 

if __name__ == '__main__':
    main()

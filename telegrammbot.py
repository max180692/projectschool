import telebot
from telebot import types
import settings
from generateprimer import GeneratePrimer

API_KEY = settings.API_TOKEN
bot = telebot.TeleBot(API_KEY)

registers_users = {}

#выбор темы для работы бота
def enter_tema():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in settings.tuple_enter_tema])
    return keyboard

#отображение таблицы умножения для умножения
def enter_numbers_umnojenie_delenie():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in settings.tuple_enter_numbers_umnojenie_delenie])
    button = types.KeyboardButton("В начало")
    keyboard.add(button)
    return keyboard



#функция создания кнопок по выбору примеров
def button_enter_numbers():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in settings.tuple_buttons])
    
    return keyboard
#функция создания кнопок выбора варианта ответа
def button_numbers(variants_answers):
    #"Назад ◀️"
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in variants_answers])
    button = types.KeyboardButton("Назад")
    keyboard.add(button)
    return keyboard



def button_action_umnojenie_delenie():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in settings.tuple_action_umnoj_delenie])
    button = types.KeyboardButton("В начало")
    keyboard.add(button)
    return keyboard

#функция по выбору действия + или -
def button_action_slojenie_vichitanie():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in settings.tuple_action_slojen_vichitan])
    button = types.KeyboardButton("В начало")
    button_random_primer = types.KeyboardButton("Случайные примеры")
    
    keyboard.add(button_random_primer)
    keyboard.add(button)
    return keyboard

#создание случайных примеров на сложение и вычитание
def create_random_primer():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=3)
    keyboard.add(*[types.KeyboardButton(button) for button in settings.tuple_create_random_primer])
    button_back = types.KeyboardButton('Назад')
    keyboard.add(button_back)
    return keyboard

#кнопка возвращения назад
def close_button_action():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton('Назад')
    keyboard.add(button)
    return keyboard

#регистрация в случае сбоя сервера или обновления бота
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
    print(len(registers_users))
    bot.send_message(message.chat.id, "Привет, этот бот поможет тебе тренировать примеры на сложение и вычитание чисел, а так же на умножение и деление. \nВыбери тему ниже  ", reply_markup=enter_tema())

#слушатель сообщений, которые поступают в телеграмм бот
@bot.message_handler(content_types='text')
def answer(message):
    if message.from_user.id not in registers_users:
        bot.send_message(message.chat.id,"Был перезапуск сервера или добавление обновлений бота, поэтому нажми на кнопку начать\"Начать\"",reply_markup=registration())

    else:
        if message.text in settings.tuple_enter_tema:
            if message.text == settings.tuple_enter_tema[0]:
                bot.send_message(message.chat.id, f"Вы выбрали \"{settings.tuple_enter_tema[0]}\" Выбери примеры ниже  ", reply_markup=button_enter_numbers())
            if message.text == settings.tuple_enter_tema[1]:
                bot.send_message(message.chat.id, f"Вы выбрали \"{settings.tuple_enter_tema[1]}\" Выбери таблицу", reply_markup=enter_numbers_umnojenie_delenie())


        #какие примеры будут генерироваться
        if message.text in settings.tuple_buttons:
            registers_users[message.from_user.id].set_sostav_chisla(settings.tuple_sostav_chisel[settings.tuple_buttons.index(message.text)])
            bot.send_message(message.chat.id, "Выбери, что ты будешь делать:\n- если складывать  нажми на \"+\";\n- если вычитать нажми на \"-\";",reply_markup=button_action_slojenie_vichitanie())


        #какое дейтствие будет выполняться
        if message.text in settings.tuple_enter_numbers_umnojenie_delenie:
            registers_users[message.from_user.id].set_sostav_chisla(settings.tuple_numbers_umnojenie_delenie[settings.tuple_enter_numbers_umnojenie_delenie.index(message.text)])
            bot.send_message(message.chat.id, "Выбери, что ты будешь делать:\n- если умножать  нажми на \"\u00D7\";\n- если делить нажми на \"\u00F7\";",reply_markup=button_action_umnojenie_delenie())

        #проверка того, что выбрали + или -
        if message.text in settings.tuple_action_slojen_vichitan:
            registers_users[message.from_user.id].enter_action(settings.tuple_action_slojen_vichitan[settings.tuple_action_slojen_vichitan.index(message.text)])
            registers_users[message.from_user.id].get_random_index()
            primer = registers_users[message.from_user.id].get_random_primer()
            result = registers_users[message.from_user.id].get_answer()
            bot.send_message(message.chat.id,primer,reply_markup=button_numbers(result['variants_answers']))
        #проверка выбора * или /
        if message.text in settings.tuple_action_umnoj_delenie:
            registers_users[message.from_user.id].enter_action(settings.tuple_action_umnoj_delenie[settings.tuple_action_umnoj_delenie.index(message.text)])
            registers_users[message.from_user.id].get_random_index()
            primer = registers_users[message.from_user.id].get_random_primer()
            result = registers_users[message.from_user.id].get_answer()
            bot.send_message(message.chat.id,primer,reply_markup=button_numbers(result['variants_answers']))
        
        if message.text == 'Случайные примеры':
            bot.send_message(message.chat.id,'Выбери сколько примеров хочешь сделать',reply_markup=create_random_primer())

        #создание рандомных примеров
        if message.text in settings.tuple_create_random_primer:
            registers_users[message.from_user.id].create_multiple_primerov(settings.tuple_random_numbers[settings.tuple_create_random_primer.index(message.text)])
            registers_users[message.from_user.id].create_random_multiple_index()
            registers_users[message.from_user.id].create_new_random_primer()
            primer = registers_users[message.from_user.id].get_random_primer()
            result = registers_users[message.from_user.id].get_answer()
            bot.send_message(message.chat.id,primer,reply_markup=button_numbers(result['variants_answers']))

        #возврат на выбор действия
        if message.text == 'Назад':
            registers_users[message.from_user.id].clear_count()
            bot.send_message(message.chat.id, "Выбери тему ниже  ", reply_markup=enter_tema())
        
        if message.text == 'Назад ◀️':
            registers_users[message.from_user.id].clear_count()
            bot.send_message(message.chat.id, "Выбери таблицу", reply_markup=enter_numbers_umnojenie_delenie())
        

        if message.text == 'В начало':
            bot.send_message(message.chat.id, "Выбери примеры ниже",reply_markup=enter_tema())
        
        
        
        #проверка, что в тексте есть только числа 
        if message.text.isdigit() and message.from_user.id in registers_users:
            proverka_otveta = registers_users[message.from_user.id].answers(message.text)
            bot.send_sticker(message.chat.id,proverka_otveta['stiker'])
            bot.send_message(message.chat.id,proverka_otveta['message'])

            primer = registers_users[message.from_user.id].get_random_primer()
            result = registers_users[message.from_user.id].get_answer()
       
            if result.__class__.__name__ == 'dict' and primer.__class__.__name__ == 'str':
                bot.send_message(message.chat.id,primer,reply_markup=button_numbers(result['variants_answers']))
            else:
                bot.send_sticker(message.chat.id,primer['stiker'])
                bot.send_message(message.chat.id,primer['message'],reply_markup=close_button_action())
    #            
    if message.text == 'Начать':
        registers_users[message.from_user.id] = GeneratePrimer()
        print(len(registers_users))
        bot.send_message(message.chat.id, "Привет, этот бот поможет тебе тренировать примеры на сложение и вычитание чисел, а так же на умножение и деление. \nВыбери тему ниже  ", reply_markup=enter_tema())


def main():
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(e)
            bot.polling(none_stop=True, interval=0) 

if __name__ == '__main__':
    main()

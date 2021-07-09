from app import bot, app
from app.models import User, Bundle
from app.helpers import manage_user
from telebot import types
from app import cache as storage
from flask import url_for

@bot.message_handler(commands=['start', 'help'])
@manage_user
def start_command(message):
    bot.send_message(message.chat.id, "Hello, i can help you to learn new vocabulary")

@bot.message_handler(commands=['token'])
@manage_user
def send_token(message):
    bot.send_message(message.chat.id, f"Your token api is: {message.chat.id}")

@bot.message_handler(commands=['create_bundle'])
@manage_user
def create_bundle(message):
    keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    end_btn = types.KeyboardButton(text='Save and exit')
    keyboard.add(end_btn)

    msg = bot.send_message(message.chat.id, "Send me word and translation in format: word - translation\nTo save all words send me '!end'", reply_markup=keyboard)
    words = dict()
    bot.register_next_step_handler(msg, lambda m: set_word(m, words))

def set_word(message, words):
    if message.text == 'Save and exit':
        print(words)
        new_bundle = Bundle(message.chat.id)
        new_bundle.encode_words(words)
        new_bundle.save()
        link = app.config['WEBHOOK'] + url_for('get_bundle', user_id=message.chat.id, bundle_id=new_bundle.id)
        # removes kayboard
        markup = types.ReplyKeyboardRemove(selective=False)
        bot.send_message(message.chat.id, f"Words successfully saved, link: {link}", reply_markup=markup)
        return
    
    input_data = message.text.split('-')
    word = input_data[0].strip()
    translation = input_data[1].strip()
    words[word] = translation

    msg =  bot.send_message(message.chat.id, "Okay, wanna to add one more? Just write it)")
    bot.register_next_step_handler(msg, lambda m: set_word(m, words))

@bot.message_handler(commands=['web'])
@manage_user
def get_web(message):

    bot.send_message(message.chat.id, "The web application of our project")
from app import bot
from app.models import User
from app.helpers import manage_user

@bot.message_handler(commands=['start'])
@manage_user
def start_command(message):
    bot.send_message(message.chat.id, "Hello")

@bot.message_handler(commands=['set'])
@manage_user
def set_bundle(message):
    bot.send_message(message.chat.id, "Not available yet)")
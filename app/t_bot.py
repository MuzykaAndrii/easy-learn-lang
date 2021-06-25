from app import bot
from app.models import User

@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id

    current_user = User.query.filter_by(telegram_id=chat_id).first()

    if current_user:
        bot.send_message(chat_id, "Hello, {} {}".format(message.from_user.first_name, message.from_user.last_name))
    else:
        new_user = User(chat_id)
        new_user.save()
        bot.send_message(chat_id, "Hello, you account successfully registered")
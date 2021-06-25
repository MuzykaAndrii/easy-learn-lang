from flask import Flask, request
import telebot
import config
import os

app = Flask(__name__)

env_config = os.getenv('APP_SETTINGS', config.DevConfig)
app.config.from_object(env_config)

bot = telebot.TeleBot(app.config['TOKEN'], threaded=False)
bot.set_webhook(url=app.config['WEBHOOK'])

@app.route("/", methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200

@bot.message_handler(commands=['lol'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello!")
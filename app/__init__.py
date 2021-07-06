from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
import telebot
import config
import os

#init flask app
app = Flask(__name__)
#init bot
bot = telebot.TeleBot(app.config['TOKEN'])

#gather configs
env_config = os.getenv('APP_SETTINGS', config.DevConfig)
app.config.from_object(env_config)

#cache instance
cache = Cache(app)

#configure db
from config import metadata
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

#config root route to set certain webhook address
@app.route('/' + app.config['TOKEN'], methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@app.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='{}/{}'.format(app.config['WEBHOOK'], app.config['TOKEN']))
    return "!", 200


from app.t_bot import *
from app import web

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

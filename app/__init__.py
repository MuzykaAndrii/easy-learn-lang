from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
import telebot
import config
import os

#init flask app
app = Flask(__name__)
#gather configs
env_config = os.getenv('APP_SETTINGS', config.DevConfig)
app.config.from_object(env_config)

#init bot
bot = telebot.TeleBot(app.config['TOKEN'], threaded=False)
bot.enable_save_next_step_handlers(delay=0)
bot.load_next_step_handlers()

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
    app.run(threaded=False, processes=1)

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_caching import Cache
import telebot
import config
import os

app = Flask(__name__)

#gather configs
env_config = os.getenv('APP_SETTINGS', config.DevConfig)
app.config.from_object(env_config)

#cache instance
cache = Cache(app)

#configure db
from config import metadata
db = SQLAlchemy(app, metadata=metadata)
migrate = Migrate(app, db)

#init bot
bot = telebot.TeleBot(app.config['TOKEN'], threaded=False)
#bot.set_webhook(url=app.config['WEBHOOK'])

#config root route to set certain webhook address
@app.route("/", methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "ok", 200

from app import web
from app.t_bot import *

from flask import Flask
import config
import os

app = Flask(__name__)

env_config = os.getenv('APP_SETTINGS', config.DevConfig)
app.config.from_object(env_config)

@app.route('/')
def index():
    return 'hello world'
import os

class Config:
    token = os.getenv('BOT_TOKEN')

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False

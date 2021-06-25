import os

class Config:
    TOKEN = os.getenv('BOT_TOKEN')
    WEBHOOK = os.getenv('WEBHOOK', 'https://c7864313cf3e.ngrok.io')

class DevConfig(Config):
    DEBUG = True

class ProdConfig(Config):
    DEBUG = False

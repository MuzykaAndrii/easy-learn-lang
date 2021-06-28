import os
#define basic directory to locate sqlite3 batabase file
basedir = os.path.abspath(os.path.dirname(__file__))

from sqlalchemy import MetaData
convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(constraint_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}
metadata = MetaData(naming_convention=convention)

class Config:
    TOKEN = os.getenv('BOT_TOKEN')
    WEBHOOK = os.getenv('WEBHOOK', 'https://c7864313cf3e.ngrok.io')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevConfig(Config):
    DEBUG = True
    SECRET_KEY = 'SuperSecretString'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'sqlite:///' + os.path.join(basedir, 'app.db'))
    CACHE_TYPE = 'filesystem'
    CACHE_DIR = 'cache/'

class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', '')
    SECRET_KEY = os.getenv('SECRET_KEY', 'uyzdkgruyvgkxudyrgvkydgkruyfgkdzyrgkfygvkdrygvk')
    CACHE_TYPE = 'SimpleCache'

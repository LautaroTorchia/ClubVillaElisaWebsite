import os
basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://relderf:asd1@localhost:5432/grupo12"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    BD_SERVER = "localhost"
    DB_DATABASE = "grupo12"
    DB_USER = ""
    DB_PASSWORD = ""
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{BD_SERVER}:5432/{DB_DATABASE}"

class TestingConfig(Config):
    TESTING = True

def get_config():
    return {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    }
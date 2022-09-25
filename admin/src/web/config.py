import os
from os import environ as env
basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import load_dotenv
load_dotenv()

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://localhost:5432/grupo12"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class ProductionConfig(Config):
    DEBUG = False
    DB_USER = env.get("DB_USER")
    DB_PASSWORD = env.get("DB_PASSWORD")
    DB_HOST = env.get("DB_HOST")
    DB_NAME = env.get("DB_NAME")
    DB_PORT = env.get("DB_PORT")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    DB_USER = env.get("DB_USER", "postgres")
    DB_PASSWORD = env.get("DB_PASSWORD", "postgres")
    DB_HOST = env.get("DB_HOST", "localhost")
    DB_NAME =  env.get("DB_NAME", "grupo12")
    DB_PORT = env.get("DB_PORT", "5432")
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"


class TestingConfig(Config):
    TESTING = True

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}

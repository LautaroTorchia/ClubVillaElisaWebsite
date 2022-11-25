import os
from os import environ as env
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

from dotenv import load_dotenv

load_dotenv()


class Config(object):
    # flask session
    SESSION_TYPE = "filesystem"
    # locale
    BABEL_DEFAULT_LOCALE = "es"
    WTF_I18N_ENABLED = False
    DEBUG = False
    TESTING = False
    # wtforms csrf and secret key
    CSRF_ENABLED = True
    SECRET_KEY = "EE7B8DA8E71E36A651E765B88F2A6"
    # db
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://localhost:5432/grupo12"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # flask jwt extended
    JWT_SECRET_KEY = "secret_key"
    JWT_TOKEN_LOCATION = ["cookies"]
    JWT_ACCESS_CSRF_HEADER_NAME = "X-Xsrf-Token"
    JWT_REFRESH_CSRF_HEADER_NAME = "X-Xsrf-Token"
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)


class ProductionConfig(Config):
    DEBUG = False
    # db
    DB_USER = env.get("DB_USER")
    DB_PASSWORD = env.get("DB_PASS")
    DB_HOST = env.get("DB_HOST")
    DB_NAME = env.get("DB_NAME")
    DB_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class DevelopmentConfig(Config):
    ENV = "development"
    DEVELOPMENT = True
    DEBUG = True
    # db
    DB_USER = env.get("DB_USER")
    DB_PASSWORD = env.get("DB_PASSWORD")
    DB_HOST = env.get("DB_HOST")
    DB_NAME = env.get("DB_NAME")
    DB_PORT = 5432
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    )


class TestingConfig(Config):
    TESTING = True


def get_config():
    """Returns:
    dict: System configuration as a dictionary
    """
    return {
        "development": DevelopmentConfig,
        "testing": TestingConfig,
        "production": ProductionConfig,
    }

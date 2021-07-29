import os

ROOT_DIR = os.path.abspath(os.path.abspath(os.path.dirname(__file__)))


class Config:
    DEBUG = False


class DevConfig(Config):
    DEBUG = True
    SERVER_NAME = 'localhost:8080'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(ROOT_DIR, '../app.sqlite')


class TestingConfig(Config):
    DEBUG = True
    TESTING = True


config_by_name = dict(
    dev=DevConfig,
    testing=TestingConfig
)

import os


class Config:
    debug = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mitchel@localhost/users'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:mitchel@localhost/users'
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig
}
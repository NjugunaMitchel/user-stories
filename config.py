import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2345@localhost/users'
    SECRET_KEY = 'e00060cf5211571fa30d8af1c0edcb0734bea0ad'

class prodConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True


config_options = {
    'development':DevConfig,
    'production':prodConfig
}
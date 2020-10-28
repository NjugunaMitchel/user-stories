import os


class Config:
    debug = True
    SECRET_KEY = 'e00060cf5211571fa30d8af1c0edcb0734bea0ad'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2345@localhost/users'


class prodConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': prodConfig
}
import os


class Config:
    debug = True
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:2345@localhost/users'


class prodConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': prodConfig
}
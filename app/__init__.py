from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config_options


# from config import Config
app = Flask(__name__)

db = SQLAlchemy()


login_manager = LoginManager()
bootstrap = Bootstrap(app)
mail = Mail(app)
login_manager.login_view = 'auth.login'
login_manager.session_protection = 'strong'


def create_app(config_name):
    db.init_app(app)

    app.config.from_object(config_options[config_name])

    bootstrap.init_app(app)

    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint 
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint)

    login_manager.init_app(app)

    return app

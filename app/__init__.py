from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_loader,Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_simplemde import SimpleMDE

login_manager = LoginManager()
login_manager.session_protection = 'srong'
login_manager.login_view = 'auth.login'

db = SQLAlchemy()
bootstrap = Bootstrap()
simplemde = SimpleMDE()

def create_app(config_name):
    app = Flask(__name__)

    # configurations
    app.config.from_object(config_loader[config_name])
    app.config.from_object(Config)

    # INITIALIZING FLASK EXTENSIONS
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    simplemde.init_app(app)

    # REGISTERING BLUEPRINTS
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/accounts')

    return app

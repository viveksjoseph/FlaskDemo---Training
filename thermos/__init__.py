import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

from .config import config_by_name

# Configure SQL Alchemy
db = SQLAlchemy()

#Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"  # redirect to login page if no login detected

#Enable debug toolbar
toolbar = DebugToolbarExtension()

#For displaying timestamps
moment = Moment()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config_by_name[config_name])
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)
    toolbar.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    from .bookmarks import bookmarks as bookmark_blueprint
    app.register_blueprint(bookmark_blueprint, url_prefix='/bookmarks')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
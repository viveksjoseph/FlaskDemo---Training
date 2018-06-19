import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_moment import Moment
from flask_debugtoolbar import DebugToolbarExtension

#path to current python file
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

#Configure database
app.config['SECRET_KEY'] = b'oy\xe6W\xe1\xddJ\xaa\x1f-$\xb6\xe0\x95d\xf3^\xc1\x10<]\xf4U\xf2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['DEBUG'] = True
db = SQLAlchemy(app)

#Configure authentication
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "login"  # redirect to login page if no login detected
login_manager.init_app(app)

#Enable debug toolbar
toolbar = DebugToolbarExtension(app)

#For displaying timestamps
moment = Moment(app)

import thermos.models
import thermos.views
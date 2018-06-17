import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#path to current python file
basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = b'oy\xe6W\xe1\xddJ\xaa\x1f-$\xb6\xe0\x95d\xf3^\xc1\x10<]\xf4U\xf2'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'thermos.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import thermos.models
import thermos.views

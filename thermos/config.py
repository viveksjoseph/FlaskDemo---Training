import os

#path to current python file
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = b'oy\xe6W\xe1\xddJ\xaa\x1f-$\xb6\xe0\x95d\xf3^\xc1\x10<]\xf4U\xf2'
    DEBUG = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-test.db')
    WTF_CSRF_ENABLED = False

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'thermos.db')

config_by_name = dict(
    dev = DevelopmentConfig,
    test = TestingConfig,
    prod = ProductionConfig
)
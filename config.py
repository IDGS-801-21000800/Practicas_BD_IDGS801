import os
from sqlalchemy import create_engine
import urllib

class Config(object):
    SECRET_KEY = "clave_nueva"
    SESSION_COOKIE_SECURE=False

class DevelopmentConfig(Config):
    DEBUG=True
    SQLALCHEMY_DATABASE_URI="mysql+pymysql://Dario:Dario12:v@127.0.0.1/prueba_flask"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

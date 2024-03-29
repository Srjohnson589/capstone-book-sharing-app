import os

class Config():
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    FLASK_APP = os.environ.get('FLASK_APP')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    KEY = os.environ.get('KEY')
    YOUR_CLIENT_ID = os.environ.get('YOUR_CLIENT_ID')
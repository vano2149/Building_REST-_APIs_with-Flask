"""
__init__.py file!
"""
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATEBASE_URI = os.environ.get("BD_URI") or "sqlite://add12.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    #  MAIL_USE_TSL = True
    MAIL_USERNAME = os.environ.get("EMAIL_ADMIN")
    MAIL_PASSWORD = os.environ.get("EMAIL_ADMIN_PASSWORD")

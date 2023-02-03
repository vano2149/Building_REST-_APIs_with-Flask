from flask import Flask, request
from app.configs import Configs
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail

app = Flask(__name__)

app.configs.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category = "info"
mail = Mail(app)


# Здесь пропишим наш babel

from app.models.post import Post
from app.models.user import User
from app.routes.general import *
from app.routes.general import *
from app.errors.hendlers import *

# API
from app.api import *
"""
user.py file!
"""
from app import db, login_manager, app
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from itsdangerous import TimedSerializer

class User(UserMixin, db.Model):

    __tablename__ = "users"

    id = db.Column(db.Iteger, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(120), unique=True, nullable=False)
    password_hash= db.Column(db.String(256), nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default="default.png")
    join_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())

    posts = db.relationship('Post', beckref="author", lazy=True)

    @staticmethod
    def verify_reset_token(token):
        ser = TimedSerializer(app.config["SECRET_KEY"])
        try:
            user_id = ser.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        check_password_hash(self.password_hash, password)
    
    def __repr__(self):
        return f"User('{self.username}', {self.email}, '{self.image_file}')"


@login_manager.user_loader
def load_user(_id:int):
    return User.query.get(int(_id))

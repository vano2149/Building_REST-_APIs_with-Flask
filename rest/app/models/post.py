"""
post.py file!
"""

from app import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = "posts"
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Iteger, db.ForeignKey('users.id'), nullable=False)

    def __repr__(self):
        return f"Post ('{self.title}', '{self.date_posted}')"

posts = [
    {
        'author' : 'Evgeny Vlasov',
        'title' : 'Blog Post #1',
        'content' : 'First post content',
        'date_posted' : 'April 17, 2021',
    }, 
    {
        'author' : 'Alice Yandex',
        'title' : 'Blog Post #2',
        'content' : 'Second post content',
        'date_posted' : 'April 18, 2021',
    }, 
    {
        'author' : 'Oleg Tinkoff',
        'title' : 'Blog Post #3',
        'content' : 'Third post content',
        'date_posted' : 'April 19, 2021',
    }
]
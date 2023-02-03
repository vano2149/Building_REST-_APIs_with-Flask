"""
Запуск нашего api!
manage.py file!
"""
from app import app, db, mail
from app.models.user import User
from app.madels.post import Post

@app.shell_context_processor
def make_shell_context():
    return {
        "app": app,
        "db": db,
        "User": User,
        "Post": Post,
        "mail": mail,
    }

if __name__ == "__main__":
    app.run()


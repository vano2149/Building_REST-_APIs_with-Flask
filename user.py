"""
user.py file!
"""

class User:
    """
    Класс пользователя.
    attrs:
        * id - пользователя.
        * login - логин пользователя.
        * password - ЧИСТЫЙ ПАРОЛЬ пользователя. (так ни кто не делает но мы сделаем!!!!)
    """
    def __init__(self, _id:int, login:str, password:str):
        self.id = _id
        self.login = login
        self.password = password

    def __str__(self):
        return f"User str<id: {self.id}, login:{self.login}>"
    
    def __repr__(self):
        return f"User Repr<{self.id}>, login: {self.login}"


"""
auth_conf.py file!
"""
from user import User
from werkzeug.security import hmac, safe_join

# Наша бд

users=[
    User(1, "Alex", "abcdefg"),
    User(2, "Bob", "qwerty123"),
]
#Возвращаем все логины
user_logins = {u.login: u for u in users}
# Возвращаем id
user_ids = {u.id : u for u in users}
# 2 метода для бд (в виде списка)
# Возвращает все логины.
#+ По login пытаемся найти пользователя в бд
#+ Если такой имеется  - то сравниваем его пароль и пароль в бд.
#+ В случае если все OK - возврашаем данного пользователя.
def authenticated(user_login:str, user_password:str):
    """
    user_login - это данныеб с которыми пользователь к нам пришел (его логин)
    user_password - это пароль с которым к нам пришел пользователь.
    """
    # находим пользователя по login
    user = user_logins.get(user_login, None)
    # Проверим, что пользователь не None и что его пароль совпадает с паролем в бд
    if user and user.password == user_password:
        return user

#Функция которая будет отдавать пользователя по id
def identity(payload:dict):
    _id = payload["identity"]
    return user_ids.get(_id, None)

# coment!
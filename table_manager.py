"""
table_manager.py file!
"""

import sqlite3

# Подключение к субд (реальное)
conn = sqlite3.connect("data.db")
# Интерфейс бд
cursor = conn.cursor()

# Первая команда - создать какую-нибуть таблицу
create_query = 'CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, login TEXT, password TEXT)'

# Выполнить данный запрос
cursor.execute(create_query)

# Cохранить изменения
conn.commit()

# Вторая команда - добавим пользователя
user = ("Alex", "qwerty123456")
insert_query = 'INSERT INTO user VALUES(NUUL, ?, ?)' # ? -placeholder для далнейших
# параметровб передаваемых на этапе выполнения запроса.
# теперь выполним запрос и передадим параметры.

for i in range(1, 1000):
    cursor.execute(insert_query, user)
    # сохраним изменения
conn.commit()

# Третья команда - проверимб что в бд что-то появилось
select_query = "SELECT * FROM users"
for row in cursor.execute(select_query):
    print(row)
# Отключиться от бд
cursor = conn.cursor()

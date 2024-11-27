# view_messages.py

'''
Задание:
Выберите все сообщения всех пользователей, возрастом старше 18 лет. 
'''

'''
Таблица Users содержит сведения о пользователях:
Поле id - первичный ключ таблицы;
Поле nickname - имя пользователя;
Поле dob - дата рождения пользователя;
Поле gender - пол пользователя;
Поле region - местоположение пользователя.

Таблица Post хранит сведения о сообщениях пользователей:
Поле id - первичный ключ таблицы;
Поле title - заголовок сообщения;
Поле description - содержимое поста;
Поле user_id - автор поста.
'''

# Собственные модули
from database import fetch_data


select_query = """
SELECT 
    users.nickname AS Никнейм,
    users.dob AS ДатаРождения,
    posts.title AS ЗаголовокСообщения,
    posts.description AS ОписаниеСообщения
FROM users
JOIN posts ON users.id = posts.user_id
WHERE 
    DATE('now', '-18 years') > users.dob
    AND users.dob IS NOT NULL;
"""


def run_view_messages(connection):
    results = fetch_data(connection, select_query)
    if results:
        for row in results:
            print(row)
    else:
        print("No data")
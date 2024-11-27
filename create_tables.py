# create_tables.py

'''
Задание: создайте таблицы posts, comments, likes. Примечание: все поля
таблицы отделяются запятыми. Внешние ключи перечисляются без запятых.
'''

'''
Таблица Regions содержит сведения о странах. Название страны считается уникальным. Таблица состоит из одного поля namereg.

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

Таблица Comments содержит комментарии к сообщениям:
Поле id - первичный ключ таблицы;
Поле description - содержимое комментария;
Поле post_id - сообщение, к которому пишется комментарий;
Поле user_id - автор комментария.

Таблица Likes позволяет учитывать «лайки» к комментариям и постам от разных пользователей:
Поле id - первичный ключ таблицы;
Поле user_id - пользователь;
Поле post_id - сообщение;
Поле comment_id - комментарий.
'''

# Собственные модули
from database import execute_query

# Таблица regions
reg_table = """
CREATE TABLE IF NOT EXISTS regions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    namereg TEXT UNIQUE NOT NULL
);
"""

# Таблица users
users_table = """
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nickname TEXT NOT NULL,
    dob DATE,
    gender TEXT,
    region_id TEXT,
    FOREIGN KEY (region_id) REFERENCES regions (id)
);
"""

# Таблица posts
posts_table = """
CREATE TABLE IF NOT EXISTS posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    description TEXT,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# Таблица comments
comments_table = """
CREATE TABLE IF NOT EXISTS comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL,
    post_id INTEGER NOT NULL,
    user_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES posts (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

# Таблица likes
likes_table = """
CREATE TABLE IF NOT EXISTS likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER,
    comment_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (post_id) REFERENCES posts (id),
    FOREIGN KEY (comment_id) REFERENCES comments (id)
);
"""


def run_create_tables(connection):
    execute_query(connection, reg_table)
    execute_query(connection, users_table)
    execute_query(connection, posts_table)
    execute_query(connection, comments_table)
    execute_query(connection, likes_table)


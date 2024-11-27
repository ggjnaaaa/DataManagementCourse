# fill_tables.py

'''
Задание: Создайте запросы на заполнение таблиц posts, comments, likes и выполните их. 
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
ins_reg = """
INSERT INTO regions (namereg)
VALUES
    ('Россия'),
    ('USA'),
    ('Белоруссия'),
    ('England');
"""

# Таблица users
ins_users = """
INSERT INTO users (nickname, dob, gender, region_id)
VALUES
    ('Колян', '2000-12-25', 'male', 1),
    ('Leila', '1998-11-01', 'female', 4),
    ('Миша', '2006-11-26', 'male', 3),
    ('Паша', '2006-11-30', 'male', 2),
    ('Elizabeth', '2005-01-21', 'female', 2);
"""

# Таблица posts
ins_posts = """
INSERT INTO posts (title, description, user_id)
VALUES
    ('Приветствие', 'Привет всем, это мой первый пост!', 1),
    ('Обновление', 'Сегодня я обновил свой профиль.', 2),
    ('Мем', 'Котики-инопланетяне зип-зип.', 3),
    ('Обновление', 'Сегодня я обновил свой аватар.', 4),
    ('Идея', 'У меня есть идея для нового проекта.', 5);
"""

# Таблица comments
ins_comments = """
INSERT INTO comments (description, post_id, user_id)
VALUES
    ('Отличная идея!', 3, 2),
    ('Привет! Рад тебя видеть.', 1, 3),
    ('Круто, что обновил профиль!', 2, 1);
"""

# Таблица likes
ins_likes = """
INSERT INTO likes (user_id, post_id, comment_id)
VALUES
    (2, 1, NULL),  -- Лайк поста
    (3, 2, NULL),  -- Лайк поста
    (1, NULL, 1),  -- Лайк комментария
    (2, NULL, 2),  -- Лайк комментария
    (3, NULL, 3);  -- Лайк комментария
"""


def run_fill_tables(connection):
    execute_query(connection, ins_reg)
    execute_query(connection, ins_users)
    execute_query(connection, ins_posts)
    execute_query(connection, ins_comments)
    execute_query(connection, ins_likes)
# main.py


# Собственные модули
from create_tables import run_create_tables
from fill_tables import run_fill_tables
from view_messages import run_view_messages
from database import (
    create_connection,
    get_default_db_path
)

def main(db_path=None):
    if not db_path:
        db_path = get_default_db_path()  # Получение дефолтного пути к бд (директория data в коне проекта, файл default_created_db.sqlite)

    connection = create_connection(db_path)

    # ЛР1 создание таблиц
    # run_create_tables(connection=connection)
    
    # ЛР2 запись в таблицы
    # run_fill_tables(connection=connection)

    # ЛР3 просмотр сообщений
    run_view_messages(connection=connection)


if __name__ == "__main__":
    main()
# database.py

# Стандартные модули Python
import os
import sqlite3
from sqlite3 import Error as e

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except e:
        print(f"The error '{e}' occurred")

    if connection is None:
        print("Failed to create a database connection")
        return
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except e as ex:
        print(f"Error: {ex}\nQuery: {query}")


def get_default_db_path():
    """Создаёт путь к файлу базы данных по умолчанию."""
    base_dir = os.getcwd()  # Текущая рабочая директория
    data_dir = os.path.join(base_dir, "data")  # Поддиректория для базы данных
    os.makedirs(data_dir, exist_ok=True)  # Создаём папку data, если её нет
    return os.path.join(data_dir, "default_created_db.sqlite")
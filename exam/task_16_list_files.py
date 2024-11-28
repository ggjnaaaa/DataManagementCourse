"""
Задача 16
Выведите список файлов в указанной директории. 
Путь к каталогу укажите с клавиатуры.
"""

import os


def list_files_in_directory(directory):
    try:
        return os.listdir(directory)
    except FileNotFoundError:
        return "Директория не найдена!"
    except PermissionError:
        return "Нет доступа к указанной директории!"


def main():
    directory = input("Введите путь к директории: ")
    result = list_files_in_directory(directory)
    if isinstance(result, list):
        print("Файлы в директории:")
        for file in result:
            print(file)
    else:
        print(result)


if __name__ == "__main__":
    main()
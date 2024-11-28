"""
Задача 12
Напишите программу, которая принимает имя файла и выводит его расширение. 
Если расширение у файла определить невозможно, выбросите исключение.
"""

def get_file_extension(filename):
    if "." in filename:
        return filename.split(".")[-1]
    else:
        raise ValueError("Указанный файл не имеет расширения")


def main():
    filename = input("Введите имя файла: ")
    try:
        extension = get_file_extension(filename)
        print("Расширение файла:", extension)
    except ValueError as e:
        print("Ошибка:", e)


if __name__ == "__main__":
    main()
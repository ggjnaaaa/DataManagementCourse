"""
Задача 10
Вы принимаете от пользователя последовательность чисел (вводите с клавиатуры), 
разделённых запятой. Составьте список и кортеж с этими числами.
"""

def parse_numbers(input_string):
    return [int(num.strip()) for num in input_string.split(",")], tuple(int(num.strip()) for num in input_string.split(","))


def main():
    user_input = input("Введите числа, разделённые запятой: ")
    numbers_list, numbers_tuple = parse_numbers(user_input)
    print("Список:", numbers_list)
    print("Кортеж:", numbers_tuple)


if __name__ == "__main__":
    main()
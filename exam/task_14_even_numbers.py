"""
Задача 14
Напишите программу, которая выводит чётные числа из заданного списка и останавливается, если встречает число 237.

list = [326, 46, 447, 18, 909, 434, 236, 375, 822, 666, 597, 978, 328, 615, 953,
345, 399, 162, 758, 219, 918, 237, 413, 566, 826, 248, 866, 951, 626, 949, 687, 217]
"""

def print_even_numbers_until_237(numbers):
    for num in numbers:
        if num == 237:
            print("Остановились на числе:", num)
            break
        if num % 2 == 0:
            print(num)


def print_even_numbers_until_237_recursive(numbers):
    if not numbers:  # Базовый случай: список пустой
        return
    current = numbers[0]  # Берём первый элемент
    if current == 237:  # Условие остановки
        print("Остановились на числе:", current)
        return
    if current % 2 == 0:  # Если число чётное, выводим его
        print(current)
        
    print_even_numbers_until_237_recursive(numbers[1:])


def main():
    numbers = [
        326, 46, 447, 18, 909, 434, 236, 375, 822, 666, 597, 978, 328, 615, 953,
        345, 399, 162, 758, 219, 918, 237, 413, 566, 826, 248, 866, 951, 626, 949, 687, 217
    ]
    print_even_numbers_until_237(numbers)


if __name__ == "__main__":
    main()
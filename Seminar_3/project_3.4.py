# Задание 4.
# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        return None

# Запрос чисел у пользователя
num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вызов функции и вывод результата
result = divide_numbers(num1, num2)
if result is not None:
    print("Результат деления:", result)

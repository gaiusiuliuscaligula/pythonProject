def sum_recursive(a, b):
    # Базовый случай: если одно из чисел равно 0, возвращаем другое число
    if a == 0:
        return b
    if b == 0:
        return a

    # Рекурсивный случай: суммируем числа с уменьшенными на 1 значениями
    return sum_recursive(a - 1, b + 1)


# Пример использования
a = 2
b = 2
result = sum_recursive(a, b)
print(result)  # Выводит: 4

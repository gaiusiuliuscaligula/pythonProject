def my_func(a, b, c):
    # Находим максимальное значение среди трех аргументов
    max_value = max(a, b, c)

    # Вычисляем сумму двух наибольших аргументов
    sum_of_max = a + b + c - max_value

    return sum_of_max


# Вызов функции с передачей трех позиционных аргументов
result = my_func(1, 3, 2)
print(result)  # Выводит: 5

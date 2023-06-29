def power_recursive(a, b):
    # Базовый случай: если степень равна 0, возвращаем 1
    if b == 0:
        return 1
    # Рекурсивный случай: возвращаем произведение числа A на его степень B-1
    return a * power_recursive(a, b-1)

# Пример использования
A = 3
B = 5
result = power_recursive(A, B)
print(result)  # Выводит: 243

A = 2
B = 3
result = power_recursive(A, B)
print(result)  # Выводит: 8

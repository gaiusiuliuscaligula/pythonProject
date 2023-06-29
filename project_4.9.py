def fact(n):
    factorial = 1
    for num in range(1, n+1):
        factorial *= num
        yield factorial

# Пример использования
n = 5
for el in fact(n):
    print(el)

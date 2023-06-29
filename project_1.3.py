# Получаем число от пользователя
n = int(input("Введите число n: "))

# Вычисляем nn и nnn
nn = int(str(n) + str(n))
nnn = int(str(n) + str(n) + str(n))

# Суммируем числа
sum_numbers = n + nn + nnn

# Выводим результат
print("n + nn + nnn =", sum_numbers)

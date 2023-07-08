# Задание 10.
# Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена
# составить не менее b километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3. Результат: 1-й день: 2 2-й день: 2,2
# 3-й день: 2,42 4-й день: 2,66 5-й день: 2,93 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.

# Получаем значения a и b от пользователя
a = float(input("Введите результат спортсмена в первый день (в километрах): "))
b = float(input("Введите желаемый общий результат спортсмена (в километрах): "))

# Инициализируем переменные
day = 1
total_distance = a

# Проверяем достижение общего результата b
while total_distance < b:
    # Увеличиваем результат на 10% относительно предыдущего дня
    a *= 1.1
    # Увеличиваем общий результат
    total_distance += a
    # Увеличиваем счетчик дня
    day += 1

# Выводим результат
print("На", day, "-й день спортсмен достиг результата — не менее", b, "километров.")
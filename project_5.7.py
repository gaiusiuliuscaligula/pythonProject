# Генерация набора чисел
numbers = [1, 2, 3, 4, 5]

# Запись чисел в файл
with open('numbers1.txt', 'w') as file:
    file.write(' '.join(map(str, numbers)))

# Чтение чисел из файла и вычисление суммы
with open('numbers1.txt', 'r') as file:
    content = file.read()
    numbers = list(map(int, content.split()))

sum_numbers = sum(numbers)

# Вывод результата на экран
print("Сумма чисел:", sum_numbers)

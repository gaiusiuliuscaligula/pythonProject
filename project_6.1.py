# Ввод данных с клавиатуры
a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разность прогрессии: "))
n = int(input("Введите количество элементов прогрессии: "))

# Создание пустого массива для хранения элементов прогрессии
progression = []

# Вычисление и добавление элементов в массив
for i in range(n):
    element = a1 + i * d
    progression.append(element)

# Вывод массива
print(progression)

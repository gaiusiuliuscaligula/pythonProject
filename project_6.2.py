# Исходный массив (список)
array = [10, 25, 15, 30, 20, 5]

# Заданный диапазон значений
min_value = 10
max_value = 20

# Список для хранения индексов
indices = []

# Поиск индексов элементов, принадлежащих заданному диапазону
for index, value in enumerate(array):
    if min_value <= value <= max_value:
        indices.append(index)

# Вывод найденных индексов
print(indices)

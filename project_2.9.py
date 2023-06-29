# Ввод элементов списка
elements = input("Введите элементы списка, разделенные пробелами: ").split()

# Преобразование элементов списка к нужному типу данных (если требуется)
elements = [int(element) for element in elements]

# Обмен значений соседних элементов
for i in range(0, len(elements) - 1, 2):
    elements[i], elements[i + 1] = elements[i + 1], elements[i]

# Вывод обновленного списка
print("Обновленный список:")
print(elements)

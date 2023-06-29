def get_greater_elements(lst):
    result = [lst[i] for i in range(1, len(lst)) if lst[i] > lst[i-1]]
    return result

# Пример исходного списка
numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

# Получение элементов, значения которых больше предыдущего элемента
greater_elements = get_greater_elements(numbers)

# Вывод результата
print(greater_elements)

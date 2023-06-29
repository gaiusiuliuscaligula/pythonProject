def max_berries(filename):
    # Чтение данных из входного файла
    with open(filename, 'r') as file:
        N = int(file.readline().strip())
        berries = list(map(int, file.readline().split()))

    # Создание списка для хранения сумм ягод
    total_berries = []

    # Расчет суммы ягод для каждого куста
    for i in range(N):
        left_neighbor = berries[(i-1) % N]
        right_neighbor = berries[(i+1) % N]
        total_berries.append(berries[i] + left_neighbor + right_neighbor)

    # Нахождение максимальной суммы ягод
    max_berries = max(total_berries)

    # Вывод результата
    print("Максимальное количество собранных ягод за один заход: ", max_berries)


# Пример использования
filename = "input.txt"
max_berries(filename)

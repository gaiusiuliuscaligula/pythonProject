# Задание 2.
# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних.
# Всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью,
# поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система
# автоматического сбора черники. Эта система состоит из
# управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.

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

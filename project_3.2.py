# Ввод данных
N = int(input("Введите количество элементов в массиве: "))
A = list(map(int, input("Введите элементы массива, разделенные пробелами: ").split()))
X = int(input("Введите число X: "))

# Инициализация переменных
closest = A[0]
min_diff = abs(X - A[0])

# Поиск ближайшего элемента
for num in A:
    diff = abs(X - num)
    if diff < min_diff:
        min_diff = diff
        closest = num

# Вывод результата
print("Самый близкий элемент к числу X:", closest)

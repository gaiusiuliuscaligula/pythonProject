# Задание 1.
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N –
# количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
# Последняя строка содержит число X Пример:
# 5 1 2 3 4 5 3 -> 1

# Ввод данных
N = int(input("Введите количество элементов в массиве: "))
A = list(map(int, input("Введите элементы массива, разделенные пробелами: ").split()))
X = int(input("Введите число X: "))

# Подсчет количества вхождений числа X в массив A
count = A.count(X)

# Вывод результата
print("Число X встречается", count, "раз(а) в массиве A.")

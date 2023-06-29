def find_common_elements(n, m):
    set1 = set()
    set2 = set()

    # Ввод элементов первого множества
    print("Введите элементы первого множества:")
    for i in range(n):
        num = int(input())
        set1.add(num)

    # Ввод элементов второго множества
    print("Введите элементы второго множества:")
    for i in range(m):
        num = int(input())
        set2.add(num)

    # Находим пересечение множеств
    common_elements = set1.intersection(set2)

    # Выводим результаты
    sorted_elements = sorted(common_elements)
    print("Числа, встречающиеся в обоих наборах без повторений в порядке возрастания:")
    for num in sorted_elements:
        print(num)


# Получаем ввод от пользователя
n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

# Вызываем функцию для поиска общих элементов
find_common_elements(n, m)

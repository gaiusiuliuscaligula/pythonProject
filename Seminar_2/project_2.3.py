# Задание 3.
# Требуется вывести все целые степени двойки (т.е. числа вида 2k),
# не превосходящие числа N.

N = int(input("Введите число N: "))

power = 0
result = 1

while result <= N:
    print(result)
    power += 1
    result = 2 ** power

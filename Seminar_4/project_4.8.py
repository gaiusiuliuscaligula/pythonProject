# Задание 8.
# Реализовать два небольших скрипта: а) итератор, генерирующий целые числа,
# начиная с указанного, б) итератор, повторяющий элементы некоторого списка,
# определенного заранее. Подсказка: использовать функцию count() и cycle()
# модуля itertools. Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении
# числа 10 завершаем цикл. Во втором также необходимо предусмотреть условие,
# при котором повторение элементов списка будет прекращено.

# A)
from itertools import count

def integer_iterator(start, stop):
    for num in count(start):
        if num > stop:
            break
        yield num

# Пример использования
for num in integer_iterator(3, 10):
    print(num)

# B)
from itertools import cycle

def list_iterator(data, stop_condition):
    count = 0
    for item in cycle(data):
        if stop_condition(item):
            break
        yield item
        count += 1

# Пример использования
my_list = [1, 2, 3]
stop_condition = lambda x: x == 2  # Пример условия завершения (при достижении числа 2)
for item in list_iterator(my_list, stop_condition):
    print(item)

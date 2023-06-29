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

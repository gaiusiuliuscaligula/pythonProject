from functools import reduce

numbers = [x for x in range(100, 1001) if x % 2 == 0]
result = reduce(lambda a, b: a * b, numbers)
print(result)
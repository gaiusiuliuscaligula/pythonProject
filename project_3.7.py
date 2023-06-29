def my_func(x, y):
    result = 1
    for _ in range(abs(y)):
        result *= x
    if y < 0:
        result = 1 / result
    return result

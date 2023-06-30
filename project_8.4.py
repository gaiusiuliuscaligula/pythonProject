class NonNumericError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Ошибка: Введено некорректное значение '{self.value}'. Введите число."


# Создаем список для хранения чисел
number_list = []

# Запрашиваем данные у пользователя
while True:
    value = input("Введите число (или 'stop' для завершения): ")

    if value == "stop":
        break

    try:
        number = float(value)

        if not isinstance(number, int) and not isinstance(number, float):
            raise NonNumericError(value)

        number_list.append(number)

    except NonNumericError as error:
        print(error)

# Выводим сформированный список на экран
print("Список чисел:", number_list)

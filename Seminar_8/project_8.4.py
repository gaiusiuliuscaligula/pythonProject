# Задание 4.
# Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
# пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
# При этом скрипт завершается, сформированный список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить
# только числа и строки. При вводе пользователем очередного элемента
# необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить пользователю
# ввести текст (не число) и отобразить соответствующее сообщение.
# При этом работа скрипта не должна завершаться.

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

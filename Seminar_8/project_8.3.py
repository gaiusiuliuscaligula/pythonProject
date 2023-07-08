# Задание 3.
# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно
# обработать эту ситуацию и не завершиться с ошибкой.

class DivisionByZeroError(Exception):
    def __init__(self, message="Деление на ноль недопустимо"):
        self.message = message
        super().__init__(self.message)


# Пример использования класса-исключения
try:
    dividend = int(input("Введите делимое: "))
    divisor = int(input("Введите делитель: "))

    if divisor == 0:
        raise DivisionByZeroError()

    result = dividend / divisor
    print("Результат деления:", result)

except ValueError:
    print("Ошибка: Введите целое число")

except DivisionByZeroError as error:
    print("Ошибка:", error)

except Exception as error:
    print("Произошла ошибка:", error)

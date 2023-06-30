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

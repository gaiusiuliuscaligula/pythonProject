# Задание 2.
# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    def __init__(self, date_string):
        self.date_string = date_string

    @classmethod
    def extract_date(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        return day, month, year

    @staticmethod
    def validate_date(day, month, year):
        if 1 <= day <= 31 and 1 <= month <= 12 and year >= 0:
            return True
        return False

    def process_date(self):
        day, month, year = self.extract_date(self.date_string)
        if self.validate_date(day, month, year):
            return f"Дата: {day:02d}.{month:02d}.{year}"
        else:
            return "Некорректная дата"


# Пример использования класса
date_string = "25-06-2023"
date = Date(date_string)
result = date.process_date()
print(result)

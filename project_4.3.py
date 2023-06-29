import sys

def calculate_salary(hours_worked, hourly_rate, bonus):
    salary = (hours_worked * hourly_rate) + bonus
    return salary

# Проверка наличия необходимого количества аргументов
if len(sys.argv) != 4:
    print("Неверное количество аргументов.")
    print("Пример использования: python script.py <выработка в часах> <ставка в час> <премия>")
    sys.exit(1)

# Чтение аргументов командной строки
try:
    hours_worked = float(sys.argv[1])
    hourly_rate = float(sys.argv[2])
    bonus = float(sys.argv[3])
except ValueError:
    print("Неверный формат аргументов.")
    print("Все аргументы должны быть числами.")
    sys.exit(1)

# Расчет заработной платы сотрудника
salary = calculate_salary(hours_worked, hourly_rate, bonus)

# Вывод результата
print("Заработная плата сотрудника: ", salary)

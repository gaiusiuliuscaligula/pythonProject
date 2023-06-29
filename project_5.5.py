filename = "salaries.txt"

# Чтение файла
with open(filename, "r") as file:
    lines = file.readlines()

# Список для хранения фамилий сотрудников с окладом менее 20 тыс.
less_than_20k = []

# Сумма окладов для расчета среднего дохода
total_salary = 0

# Подсчет фамилий и суммирование окладов
for line in lines:
    line = line.strip()  # Удаление символа перевода строки
    parts = line.split()  # Разделение строки на фамилию и оклад
    if len(parts) == 2:
        surname = parts[0]
        salary = float(parts[1])
        total_salary += salary  # Суммирование окладов
        if salary < 20000:  # Проверка оклада
            less_than_20k.append(surname)  # Добавление фамилии в список

# Вывод фамилий сотрудников с окладом менее 20 тыс.
print("Сотрудники с окладом менее 20 тыс.:")
for surname in less_than_20k:
    print(surname)

# Расчет и вывод средней величины дохода
average_salary = total_salary / len(lines)
print("Средний доход сотрудников:", average_salary)

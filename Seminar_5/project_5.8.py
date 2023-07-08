# Задание 8.
# Необходимо создать (не программно) текстовый файл, где каждая строка описывает
# учебный предмет и наличие лекционных, практических и лабораторных
# занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран. Примеры строк файла: Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб) Физкультура: — 30(пр) — Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

import re

# Открываем файл на чтение
with open('lessons.txt', 'r', encoding="utf-8") as file:
    content = file.readlines()

# Создаем словарь для хранения данных
lessons_dict = {}

# Обрабатываем каждую строку файла
for line in content:
    # Используем регулярное выражение для извлечения числовых значений
    matches = re.findall(r'\d+', line)
    numbers = [int(match) for match in matches]

    # Извлекаем название предмета из строки
    subject = line.split(':')[0].strip()

    # Вычисляем общее количество занятий
    total_lessons = sum(numbers)

    # Добавляем предмет и общее количество занятий в словарь
    lessons_dict[subject] = total_lessons

# Выводим словарь на экран
print(lessons_dict)
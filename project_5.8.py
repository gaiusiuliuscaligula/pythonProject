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

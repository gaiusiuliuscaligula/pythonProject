# Задание 6.
# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1 Two — 2 Three — 3 Four — 4 Необходимо написать программу,
# открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

# Открываем файл на чтение
with open('numbers.txt', 'r') as file:
    lines = file.readlines()  # Считываем строки из файла

rus_numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

# Заменяем английские числительные на русские
for i in range(len(lines)):
    for eng, rus in rus_numbers.items():
        if eng in lines[i]:
            lines[i] = lines[i].replace(eng, rus)

# Записываем новый блок строк в файл
with open('numbers_rus.txt', 'w') as file:
    file.writelines(lines)

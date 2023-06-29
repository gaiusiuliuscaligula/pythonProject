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

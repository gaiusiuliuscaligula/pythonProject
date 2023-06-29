filename = "example.txt"

# Чтение файла
with open(filename, "r") as file:
    lines = file.readlines()

# Подсчет количества строк
num_lines = len(lines)

# Подсчет количества слов в каждой строке
word_counts = []
for line in lines:
    words = line.split()
    word_count = len(words)
    word_counts.append(word_count)

# Вывод результатов
print("Количество строк в файле:", num_lines)
print("Количество слов в каждой строке:")
for i, count in enumerate(word_counts, start=1):
    print("Строка", i, ":", count)
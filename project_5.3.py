# Открытие файла для записи
filename = "data.txt"
with open(filename, "w") as file:
    # Цикл для ввода данных пользователем
    while True:
        # Ввод данных
        line = input("Введите данные (или оставьте пустую строку для окончания ввода): ")

        # Проверка на пустую строку
        if line == "":
            break

        # Запись данных в файл
        file.write(line + "\n")

print("Данные записаны в файл", filename)

# Открытие файла
with open('california_housing_train.csv', 'r') as file:
    lines = file.readlines()

# Первая строка содержит заголовки столбцов
headers = [header.strip('"') for header in lines[0].strip().split(',')]

# Поиск индекса столбца 'population'
population_index = headers.index('population')

# Инициализация переменных
total_cost = 0
count = 0

# Чтение данных из файла
for line in lines[1:]:
    data = line.strip().split(',')
    population = float(data[population_index])
    if population >= 0 and population <= 500:
        median_house_value = float(data[-1].strip('"'))
        total_cost += median_house_value
        count += 1

# Вычисление средней стоимости дома
average_cost = total_cost / count

# Вывод результата
print("Средняя стоимость дома с количеством людей от 0 до 500:", average_cost)

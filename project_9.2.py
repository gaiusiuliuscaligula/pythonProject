# Открытие файла
with open('california_housing_train.csv', 'r') as file:
    lines = file.readlines()

# Первая строка содержит заголовки столбцов
headers = [header.strip('"') for header in lines[0].strip().split(',')]

# Поиск индексов столбцов 'population' и 'households'
population_index = headers.index('population')
households_index = headers.index('households')

# Инициализация переменных
min_population = float('inf')
max_households = 0

# Чтение данных из файла
for line in lines[1:]:
    data = line.strip().split(',')
    population = float(data[population_index])
    households = float(data[households_index])

    if population < min_population:
        min_population = population
        max_households = households
    elif population == min_population:
        max_households = max(max_households, households)

# Вывод результата
print("Максимальное количество households в зоне с минимальным значением population:", max_households)

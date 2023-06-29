# Решение через список (list):
month = int(input("Введите номер месяца (от 1 до 12): "))

seasons = ['зима', 'весна', 'лето', 'осень']

if month in [1, 2, 12]:
    season = seasons[0]  # зима
elif month in [3, 4, 5]:
    season = seasons[1]  # весна
elif month in [6, 7, 8]:
    season = seasons[2]  # лето
elif month in [9, 10, 11]:
    season = seasons[3]  # осень
else:
    print("Ошибка: введен некорректный номер месяца.")
    exit()

print(f"Месяц номер {month} относится к времени года: {season}.")

# Решение через словарь (dict):
month = int(input("Введите номер месяца (от 1 до 12): "))

seasons = {
    (1, 2, 12): 'зима',
    (3, 4, 5): 'весна',
    (6, 7, 8): 'лето',
    (9, 10, 11): 'осень'
}

for key in seasons:
    if month in key:
        season = seasons[key]
        break
else:
    print("Ошибка: введен некорректный номер месяца.")
    exit()

print(f"Месяц номер {month} относится к времени года: {season}.")

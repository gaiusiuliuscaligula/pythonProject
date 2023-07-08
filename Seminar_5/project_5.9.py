# Задание 9.
# Создать (не программно) текстовый файл, в котором каждая строка должна
# содержать данные о фирме: название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000. Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями,
# а также словарь со средней прибылью. Если фирма получила убытки,
# также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}]. Итоговый список сохранить в виде json-объекта в
# соответствующий файл. Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
# Подсказка: использовать менеджеры контекста.

import json

result = []
total_profit = 0
num_profitable_companies = 0

with open("companies.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split()
        name = data[0]
        revenue = int(data[2])
        expenses = int(data[3])
        profit = revenue - expenses

        if profit >= 0:
            num_profitable_companies += 1
            total_profit += profit

        result.append({name: profit})

average_profit = total_profit / num_profitable_companies if num_profitable_companies > 0 else 0
result.append({"average_profit": average_profit})

with open("result.json", "w", encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False)

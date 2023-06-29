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

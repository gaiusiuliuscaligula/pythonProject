products = []
analytics = {}

while True:
    name = input("Введите название товара: ")
    price = float(input("Введите цену товара: "))
    quantity = int(input("Введите количество товара: "))
    unit = input("Введите единицу измерения товара: ")

    product = {
        "название": name,
        "цена": price,
        "количество": quantity,
        "ед": unit
    }

    products.append((len(products) + 1, product))

    for key, value in product.items():
        if key in analytics:
            analytics[key].append(value)
        else:
            analytics[key] = [value]

    choice = input("Хотите добавить еще товар? (да/нет): ")
    if choice.lower() != "да":
        break

print("Структура товаров:")
print(products)

print("Аналитика о товарах:")
print(analytics)

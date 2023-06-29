ratings = [7, 5, 3, 3, 2]

while True:
    new_rating = int(input("Введите новый элемент рейтинга (натуральное число): "))
    ratings.append(new_rating)
    ratings.sort(reverse=True)
    print("Новый рейтинг:", ratings)

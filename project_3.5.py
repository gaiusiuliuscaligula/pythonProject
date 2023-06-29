def print_user_data(name, surname, birth_year, city, email, phone):
    user_data = f"Имя: {name}, Фамилия: {surname}, Год рождения: {birth_year}, Город: {city}, Email: {email}, Телефон: {phone}"
    print(user_data)

# Вызов функции с передачей именованных аргументов
print_user_data(name="Иван", surname="Иванов", birth_year=1990, city="Москва", email="ivan@example.com", phone="123456789")

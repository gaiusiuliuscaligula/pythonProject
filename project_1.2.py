# Получаем время от пользователя
total_seconds = int(input("Введите время в секундах: "))

# Вычисляем часы, минуты и секунды
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

# Выводим время в формате чч:мм:сс
time_format = "{:d}:{:d}:{:d}".format(hours, minutes, seconds)
print("Время в формате ч:м:с -", time_format)

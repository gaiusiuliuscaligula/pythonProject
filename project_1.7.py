# Получаем номер билета от пользователя
ticket_number = input("Введите номер билета: ")

# Проверяем, является ли билет счастливым
# Разделяем номер на отдельные цифры
digit1 = int(ticket_number[0])
digit2 = int(ticket_number[1])
digit3 = int(ticket_number[2])
digit4 = int(ticket_number[3])
digit5 = int(ticket_number[4])
digit6 = int(ticket_number[5])

# Вычисляем сумму первых трех цифр и последних трех цифр
sum_first_three = digit1 + digit2 + digit3
sum_last_three = digit4 + digit5 + digit6

# Проверяем, является ли билет счастливым
if sum_first_three == sum_last_three:
    print("yes")
else:
    print("no")

# Получаем количество сделанных журавликов
s = int(input("Введите общее количество журавликов (S): "))

# Вычисляем количество журавликов для каждого ребенка
# Петя и Сережа сделали одинаковое количество журавликов
# Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе

petya_sereja = s // 4  # Журавлики, сделанные Петей и Сережей (одинаковое количество)
katya = petya_sereja * 2  # Журавлики, сделанные Катей

# Выводим результат
print("Петя:", petya_sereja)
print("Катя:", katya)
print("Сережа:", petya_sereja)

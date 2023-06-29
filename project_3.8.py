def calculate_sum():
    total_sum = 0
    while True:
        numbers = input("Введите числа, разделенные пробелом (для завершения введите специальный символ): ")
        numbers_list = numbers.split()
        for num in numbers_list:
            if num.isdigit():
                total_sum += int(num)
            else:
                return total_sum
        print("Текущая сумма:", total_sum)

    return total_sum

final_sum = calculate_sum()
print("Итоговая сумма:", final_sum)

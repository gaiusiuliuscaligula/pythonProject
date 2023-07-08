# Задание 6
# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта,
# создав экземпляры класса (комплексные числа) и выполнив
# сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class ComplexNumber:
    def __init__(self, real_part, imaginary_part):
        self.real = real_part
        self.imaginary = imaginary_part

    def __add__(self, other):
        if isinstance(other, ComplexNumber):
            real_sum = self.real + other.real
            imaginary_sum = self.imaginary + other.imaginary
            return ComplexNumber(real_sum, imaginary_sum)
        else:
            raise ValueError("Ошибка: Нельзя сложить комплексное число с другим типом данных.")

    def __mul__(self, other):
        if isinstance(other, ComplexNumber):
            real_product = self.real * other.real - self.imaginary * other.imaginary
            imaginary_product = self.real * other.imaginary + self.imaginary * other.real
            return ComplexNumber(real_product, imaginary_product)
        else:
            raise ValueError("Ошибка: Нельзя умножить комплексное число на другой тип данных.")

    def __str__(self):
        return f"{self.real} + {self.imaginary}i"


# Пример использования класса

# Создаем два комплексных числа
complex1 = ComplexNumber(2, 3)
complex2 = ComplexNumber(4, 5)

# Сложение комплексных чисел
sum_result = complex1 + complex2
print(f"Сумма: {sum_result}")

# Умножение комплексных чисел
product_result = complex1 * complex2
print(f"Произведение: {product_result}")

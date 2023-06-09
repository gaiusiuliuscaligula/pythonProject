# Задание 5.
# Реализовать программу работы с органическими клетками.
# Необходимо создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число).
# В классе должны быть реализованы методы перегрузки арифметических
# операторов: сложение (add()), вычитание (sub()), умножение (mul()),
# деление (truediv()).Данные методы должны применяться только к клеткам
# и выполнять увеличение, уменьшение, умножение и обычное (не целочисленное)
# деление клеток, соответственно. В методе деления должно осуществляться
# округление значения до целого числа. Сложение. Объединение двух клеток.
# При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность
# количества ячеек двух клеток больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется
# как произведение количества ячеек этих двух клеток. Деление.
# Создается общая клетка из двух. Число ячеек общей клетки определяется как
# целочисленное деление количества ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(),
# принимающий экземпляр класса и количество ячеек в ряду.
# Данный метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида \n\n*****...,
# где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний
# ряд записываются все оставшиеся. Например, количество ячеек клетки равняется 12,
# количество ячеек в ряду — 5. Тогда метод make_order() вернет строку: \n\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: \n\n*****.

class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __str__(self):
        return f"Клетка с {self.cells} ячейками"

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        diff = self.cells - other.cells
        if diff > 0:
            return Cell(diff)
        else:
            print("Разность количества ячеек меньше или равна нулю.")

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_per_row):
        rows = self.cells // cells_per_row
        remainder = self.cells % cells_per_row
        result = ""
        for _ in range(rows):
            result += "*" * cells_per_row + "\n"
        result += "*" * remainder
        return result


# Пример использования
cell1 = Cell(12)
cell2 = Cell(7)

print(cell1)
print(cell2)

cell3 = cell1 + cell2
print("Сложение:", cell3)

cell4 = cell1 - cell2
print("Вычитание:", cell4)

cell5 = cell1 * cell2
print("Умножение:", cell5)

cell6 = cell1 / cell2
print("Деление:", cell6)

print("Ячейки по рядам:")
print(cell1.make_order(5))

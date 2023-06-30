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

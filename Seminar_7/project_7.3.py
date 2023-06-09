# Задание 3.
# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса
# (метод init()), который должен принимать данные (список списков)
# для формирования матрицы. Подсказка: матрица — система некоторых
# математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке. Следующий шаг — реализовать
# перегрузку метода str() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода add() для реализации операции сложения
# двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            row_str = " ".join(str(element) for element in row)
            matrix_str += row_str + "\n"
        return matrix_str

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError("Матрицы должны быть одинакового размера для выполнения сложения.")

        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[i])):
                element_sum = self.data[i][j] + other.data[i][j]
                row.append(element_sum)
            result.append(row)

        return Matrix(result)


# Пример использования
matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(matrix1)
print(matrix2)

matrix_sum = matrix1 + matrix2
print(matrix_sum)

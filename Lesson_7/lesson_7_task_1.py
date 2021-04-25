class Matrix:
    def __init__(self, my_matrix):
        self.matrix = my_matrix

    def __str__(self):
        result = ''
        max_num = 2
        for i in self.matrix:
            if max_num < max(i):
                max_num = max(i)
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                result += str(self.matrix[i][j]).rjust(len(str(max_num)) + 2, ' ')
                # ширина столбцов подстраивается под самое длинное число в матрице для более красивого вывода
            result += '\n'
        return result

    def __add__(self, plus_matrix):
        result = []
        if len(self.matrix) == len(plus_matrix.matrix):
            for line_1, line_2 in zip(self.matrix, plus_matrix.matrix):
                if len(line_1) != len(line_2):
                    return 'Матрицы разных размеров!'
                result.append([i + j for i, j in zip(line_1, line_2)])
        else:
            return 'Матрицы разных размеров!'
        result = Matrix(result)
        return result


matrix_1 = Matrix([[828, 16, 4], [51, 4, 985], [5, 630, -95], [7, 8, 85]])
matrix_2 = Matrix([[72, -2, 9], [49, 5, -85], [11, 47, -5], [5, 0, 15]])

print(matrix_1)
print(matrix_2)
print(matrix_1+matrix_2)


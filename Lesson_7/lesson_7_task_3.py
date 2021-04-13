class Cell:
    def __init__(self, num):
        self.num = num

    def make_order(self, num_rows):
        result = '\n'.join(['*' * num_rows for i in range(self.num // num_rows)])
        result += '\n' + '*' * (self.num % num_rows)
        return result

    def __str__(self):
        return str(self.num)

    def __add__(self, other):
        return self.num + other.num

    def __sub__(self, other):
        if self.num - other.num > 0:
            return self.num - other.num
        else:
            return 'В первой клетке не больше ячеек, чем во второй!'

    def __mul__(self, other):
        return self.num * other.num

    def __truediv__(self, other):
        return round(self.num / other.num)


cell_1 = Cell(35)
cell_2 = Cell(20)
print(cell_1)
print(cell_2)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(15))

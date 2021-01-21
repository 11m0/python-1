class Cell:
    def __init__(self, number_of_cells: int):
        self.number = number_of_cells

    def __add__(self, other):
        return self.number + other.number

    def __sub__(self, other):
        return self.number - other.number \
            if self.number > other.number \
            else print('The other cell must be larger than the original!')

    def __mul__(self, other):
        return self.number * other.number

    def __truediv__(self, other):
        return self.number // other.number

    def make_order(self, cells_in_line):
        try:
            return ''.join(['*' if i % cells_in_line != 0 else '*\n' for i in range(1, self.number + 1)]).strip()
        except TypeError:
            pass


c_1 = Cell(4)
c_2 = Cell(3)
print(f'The result of adding two cells is:\n{Cell(c_1 + c_2).make_order(5)}')
print(f'The result of subtracting two cells is:\n{Cell(c_1 - c_2).make_order(5)}')
print(f'The result of multiplying two cells is:\n{Cell(c_1 * c_2).make_order(5)}')
print(f'The result of division two cells is:\n{Cell(c_1 / c_2).make_order(5)}')

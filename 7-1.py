class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __add__(self, other):
        self.new_matrix = []
        for i in range(0, len(self.matrix)):
            self.new_matrix.append([m + n for m, n in zip(self.matrix[i], other.matrix[i])])
        return self.new_matrix

    def __str__(self):
        data_str = ''
        for el in [[str(el) for el in line] for line in self.matrix]:
            data_str += ' '.join(el) + '\n'
        return data_str


m_1 = Matrix([[3, 5, 1],
              [2, 4, 2],
              [1, 3, 0]])
m_2 = Matrix([[1, 1, 1],
              [1, 1, 1],
              [1, 1, 1]])

print(m_1)
print(m_2)
print(Matrix(m_1 + m_2))

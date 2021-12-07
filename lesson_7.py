class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
    # список в списке, itm внутри line
    def __str__(self):
        return '\n'.join('\t'.join(f"{itm}" for itm in line) for line in self.matrix)

    def __add__(self, other):
        sum = [int(self.list[line][itm] + int(other.list[line][int])) for itm in range(len(self.matrix[line]))]
        return Matrix(sum)


matrix_1 = Matrix([[1, 2], [3, 4], [5, 5]])
matrix_2 = Matrix([[1, 2], [3, 4], [5, 5]])
matrix_sum = matrix_1 + matrix_2
print(matrix_1)
print(matrix_2)
print(matrix_sum)


from abc import ABC, abstractmethod

class Clothes(ABC):
    sum = 0
    def __init__(self, parameter):
        self.parameter = parameter

    @property
    @abstractmethod
    def tissue(self):
        pass
    def __add__(self, other):
        Clothes.sum += self.tissue + other.tissue
        return Coat(0)
    def __str__(self):
        result = Clothes.sum
        Clothes.sum = 0
        return f"{result}"

class Coat(Clothes):
    @property
    def tissue(self):
        return round(self.parameter/6.5 + 0.5)
class Suit(Clothes):
    @property
    def tissue(self):
        return round(2*self.parameter + 0.3)



coat = Coat(10)
suit = Suit(12)
print(coat + suit)


class Cell:

    def __init__(self, meshes):
        self.meshes = meshes

    def make_order(self, rows):
        return '\n'.join(['@'*rows for _ in range(self.meshes//rows)]) + '\n' + '@'*(self.meshes%rows)

    def __add__(self, other):
        print(f"Sum is:")
        return Cell(self.meshes + other.meshes)

    def __sub__(self, other):
        print(f"Truediv is:")
        if self.meshes - other.meshes > 0:
            return Cell(self.meshes - other.meshes)
        else:
            print(f"Not possible")

    def __mul__(self, other):
        print(f"Multiply is:")
        return Cell(self.meshes*other.meshes)

    def __floordiv__(self, other):
        print(f"Multiply is:")
        return Cell(self.meshes/other.meshes)


cell_1 = Cell(10)
cell_2 = Cell(20)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1*cell_2)
print(cell_1//cell_2)
print(cell_2.make_order(2))



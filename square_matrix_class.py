class SquareMatrix:
    def __init__(self, matrix):
        if type(matrix) != list:
            raise TypeError("matrix should be list of lists")
        for line in matrix:
            if type(line) != list:
                raise TypeError("matrix should be list of lists")
            if len(matrix) != len(line):
                raise TypeError("matrix should be square")
            for element in line:
                if type(element) != float and type(element) != int:
                    raise TypeError("Elements of matrix should be integer or float")
                else:
                    self.matrix = matrix
                    self.determinant = SquareMatrix.matrix_determinant(self)
                    
                    
    def _get_smaller_matrix(matrix, row_number):
        new_matrix = []
        for line_number in range(1, len(matrix)):
            new_line = []
            for element_number in range(len(matrix[line_number])):
                if element_number != row_number:
                    new_line.append(matrix[line_number][element_number])
            new_matrix.append(new_line)
        return new_matrix
    
    
    def matrix_determinant(self):
        if len(self.matrix) == 1:
            return self.matrix[0][0]
        elif len(self.matrix) == 2:
            return self.matrix[0][0] * self.matrix[1][1] - self.matrix[0][1] * self.matrix[1][0]
        else:
            det_value = 0
            for i in range(len(self.matrix[0])):
                if i%2 == 0:
                    det_value += self.matrix[0][i] * matrix_determinant(_get_smaller_matrix(self.matrix, i))
                else: 
                    det_value -= self.matrix[0][i] * matrix_determinant(_get_smaller_matrix(self.matrix, i))
            return det_value
        
    
    def __len__(self):
        return len(self.matrix)
        
        
    def __add__(self, another):
        if len(self) != len(another):
            raise ValueError("The matrixes should have the same dimensions")
        else:
            new_matrix = []
            for line_index in range(len(self)):
                new_line = []
                for item_index in range(len(self)):
                    new_line.append(self.matrix[line_index][item_index] + another.matrix[line_index][item_index])
                new_matrix.append(new_line)                
            return SquareMatrix(new_matrix)
    
    
    def __sub__(self, another):
        if len(self) != len(another):
            raise ValueError("The matrixes should have the same dimensions")
        else:
            new_matrix = []
            for line_index in range(len(self)):
                new_line = []
                for item_index in range(len(self)):
                    new_line.append(self.matrix[line_index][item_index] - another.matrix[line_index][item_index])
                new_matrix.append(new_line)                
            return SquareMatrix(new_matrix)
        
    
    def __eq__(self, another):
        if len(self) != len(another):
            return False
        else:
            for line_index in range(len(self)):
                for item_index in range(len(self)):
                    if self.matrix[line_index][item_index] != another.matrix[line_index][item_index]:
                        return False
            return True
    
    
    def __mul__(self, another):
        if type(another) == int or type(another) == float:
            new_matrix = []
            for line_index in range(len(self)):
                new_line = []
                for item_index in range(len(self)):
                    new_line.append(another * self.matrix[line_index][item_index])
                new_matrix.append(new_line)
            return SquareMatrix(new_matrix)
        else:
            raise ValueError("XXX")
            
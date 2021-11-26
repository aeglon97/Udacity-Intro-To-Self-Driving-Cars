import math
from math import sqrt
import numbers

def zeroes(height, width):
        """
        Creates a matrix of zeroes.
        """
        g = [[0.0 for _ in range(width)] for __ in range(height)]
        return Matrix(g)

def identity(n):
        """
        Creates a n x n identity matrix.
        """
        I = zeroes(n, n)
        for i in range(n):
            I.g[i][i] = 1.0
        return I
    
def dot_product(vector_one, vector_two):
    if len(vector_one) != len(vector_two):
        raise(ValueError, "Vectors must be the same length.")

    sum_vectors = 0
    for i in range(len(vector_one)):
        sum_vectors += vector_one[i] * vector_two[i]
        
    return sum_vectors

class Matrix(object):
    def __init__(self, grid):
        self.g = grid
        self.h = len(grid)
        self.w = len(grid[0])

    #-----Primary matrix math methods-----#
    def determinant(self):
        """
        Calculates the determinant of a 1x1 or 2x2 matrix.
        Determinant: The product of all a[i][j] where i = j MINUS the product of
                     all a[i][j] where j = width - (i-1).
                        for a in matrix A containing i rows and j columns.
                            
        --> 2x2 Product of the major diagonals (top-left to bottom-right) 
                MINUS the product of the backward diagonals (top-right to bottom-left).
                
        --> 3x3 and larger: see Rule of Sarrus.
        
        """
        
        if not self.is_square():
            raise(ValueError, "Cannot calculate determinant of non-square matrix.")
            
        if not self.g:
            raise(ValueError, "Cannot find the determinant of an empty matrix.")
            
        if (self.h == 1 and self.w == 1):
            return (self.g[0][0])
        
        elif (self.h == 2 and self.w == 2):
            return (self.g[0][0] * self.g[1][1] - self.g[0][1] * self.g[1][0])
        
        else:
            raise(NotImplementedError, "Calculating determinant not implemented for matrices larger than 2x2.") 

    def trace(self):
        """
        Calculates the trace of a matrix (sum of diagonal entries).
        Trace: The sum of all a[i][j] where i = j, for element a in matrix A containing i rows and j columns.
        --> The sum of the major diagonal values (top-left to bottom-right).
        """
        
        if not self.is_square():
            raise(ValueError, "Cannot calculate the trace of a non-square matrix.")

        trace = 0
        for n in range(self.h):
            trace += self.g[n][n]
            
        return trace
                      
    def inverse(self):
        """
        Calculates the inverse of a 1x1 or 2x2 Matrix.
        --> If the inverse of scalar x is 1/x, then the inverse of matrix A is A^-1.
        --> Similarly, if x * (1/x) = 1, then A * A^-1 = I.
        
        1x1 matrix -- Formal mathematical definition: A^-1 = [[1/a]] for a in matrix A.
        2x2 matrix -- Formal mathematical definition: A^-1 = (1/detA) * [(traceA * I_2) - A]
             
        """
        if not self.is_square():
            raise(ValueError, "Non-square Matrix does not have an inverse.")
            
        if self.h > 2 or self.w > 2:
            raise(NotImplementedError, "Inversion not implemented for matrices larger than 2x2.")

        if self.h == 1 and self.w == 1:
            return Matrix([[1/self.g[0][0]]])
        
        elif self.h == 2 and self.w == 2:
            factor = 1 / self.determinant()

            trace_times_I2 = self.trace() * identity(2)
            trace_times_I2_minus_A = trace_times_I2 - self
            
            inverse = factor * trace_times_I2_minus_A
            
            return inverse
 
        
    def T(self):
        """
        Returns a transposed copy of this Matrix.
        Formal mathematical definition: [A^T]_i,j = A_j,i
        --> Each element in matrix A at index [i,j] will be at index [j,i] in the 
        transposed matrix.
        """      
        transpose = []
        
        for i_col in range(self.w):
            transposed_row = []
            for i_row in range(self.h):
                transposed_row.append(self.g[i_row][i_col])
                
            transpose.append(transposed_row)
        
        return Matrix(transpose)
        

    def is_square(self):
        return self.h == self.w
    
    #-----OPERATOR OVERLOADING-----#
    def __getitem__(self,idx):
        """
        Defines the behavior of using square brackets [] on instances
        of this class.

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > my_matrix[0]
          [1, 2]

        > my_matrix[0][0]
          1
        """
        
        return self.g[idx]

    def __repr__(self):
        """
        Defines the behavior of calling print on an instance of this class.
        """
        s = ""
        for i_row in self.g:
            s += " ".join(["{} ".format(x) for x in i_row])
            s += "\n"
        return s

    def __add__(self,other):
        """
        Defines the behavior of the + operator
        """
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be added if the dimensions are the same") 
        
        matrix_sum = []
        
        for i_row in range(self.h):
            row_result = []
            for i_col in range(other.w):
                row_result.append(self.g[i_row][i_col] + other.g[i_row][i_col])
 
            matrix_sum.append(row_result)
                
        return Matrix(matrix_sum)

    def __neg__(self):
        """
        Defines the behavior of - operator (NOT subtraction)

        Example:

        > my_matrix = Matrix([ [1, 2], [3, 4] ])
        > negative  = -my_matrix
        > print(negative)
          -1.0  -2.0
          -3.0  -4.0
        """
        neg_matrix = []
        for i_row in range(self.h):
            row_result = []
            for i_col in range(self.w):
                row_result.append(self.g[i_row][i_col] * (-1))
                
            neg_matrix.append(row_result)
            
        return Matrix(neg_matrix)
                
    def __sub__(self, other):
        """
        Defines the behavior of - operator (as subtraction)
        """
        
        if self.h != other.h or self.w != other.w:
            raise(ValueError, "Matrices can only be subtracted if the dimensions are the same") 
            
        matrix_difference = []
        
        for i_row in range(self.h):
            row_result = []
            for i_col in range(other.w):
                row_result.append(self.g[i_row][i_col] - other.g[i_row][i_col])
                
            matrix_difference.append(row_result)
        
        return Matrix(matrix_difference)
    
    def __mul__(self, other):
        """
        Defines the behavior of * operator (matrix multiplication)
        
        matrixA * matrixB = dot product of every column (matrixB) per row in matrixA
        
        --> if matrixA = j * k and matrixB = k * l, then the product matrix will be size j * l.
        """
        
        # If self or other is a Number, a mismatched type error will return after this if statement
        # which will force the matrix to use its __rmul__ logic
        if self.w != other.h:
            raise(ValueError, "The number of columns of Matrix A must equal the number of rows in Matrix B")

        matrix_product = []

        for i_row in range(self.h):
            row_result = []
            for i_col in range(other.w):
                col_vals = [row[i_col] for row in other.g]
                row_result.append(dot_product(self.g[i_row], col_vals))
            matrix_product.append(row_result)

        return Matrix(matrix_product)

    #Scalar multiplication
    def __rmul__(self, other):
        """
        Called when the thing on the left of the * is a scalar value.
        Example:

        > identity = Matrix([ [1,0], [0,1] ])
        > doubled  = 2 * identity
        > print(doubled)
          2.0  0.0
          0.0  2.0
          
        Note: if __mul__ fails, then __rmul__ is automatically invoked next.
        """
        if isinstance(other, numbers.Number):
            scalar_matrix = []
            
            for i_row in range(self.h):
                row = []
                for i_col in range(self.w):
                    row.append(self.g[i_row][i_col] * other)
                scalar_matrix.append(row)
                    
        return Matrix(scalar_matrix)
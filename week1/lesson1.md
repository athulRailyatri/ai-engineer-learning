# Lesson 1 - Matrix Multiplication in Python

## Problem
We need to implement a `Matrix` class in Python that can multiply two matrices using the `*` operator.

Given two matrices:
- Matrix 1: [[1, 2], [3, 4]]
- Matrix 2: [[5, 6], [7, 8]]

The multiplication should be implemented such that:
```python
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])
result = matrix1 * matrix2
```
will produce:
```
[19, 22]
[43, 50]
```

## Solution Code
```python
class Matrix:
    def __init__(self, data):
        self.list = data

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise ValueError("Can only multiply with another Matrix instance")

        if len(self.list[0]) != len(other.list):
            raise ValueError("Incompatible matrices for multiplication")

        result = []
        for i in range(len(self.list)):
            row = []
            for j in range(len(other.list[0])):
                sum_product = 0
                for k in range(len(other.list)):
                    sum_product += self.list[i][k] * other.list[k][j]
                row.append(sum_product)
            result.append(row)
        return result

if __name__ == "__main__":
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])

    result = matrix1 * matrix2
    print("Result of multiplication:")
    for row in result:
        print(row)
```

## Key Points
1. Matrix multiplication requires that the **number of columns in the first matrix equals the number of rows in the second matrix**.
2. We use the `__mul__` magic method to allow the `*` operator for matrix multiplication.
3. The implementation uses three nested loops:
   - Outer loop for each row in the first matrix.
   - Middle loop for each column in the second matrix.
   - Inner loop for summing the products of corresponding elements.

## Example Output
```
Result of multiplication:
[19, 22]
[43, 50]
```

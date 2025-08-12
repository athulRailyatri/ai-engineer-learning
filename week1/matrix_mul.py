
class Matrix:

    list=[]

    def __init__(self,data):
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
    # Example usage
    matrix1 = Matrix([[1, 2], [3, 4]])
    matrix2 = Matrix([[5, 6], [7, 8]])
    
    result = matrix1 * matrix2
    print("Result of multiplication:")
    for row in result:
        print(row)

        
        
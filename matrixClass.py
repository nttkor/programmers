class SimpleMatrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if data else 0

    def __add__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("행렬 크기가 일치하지 않습니다.")
        result = [
            [self.data[i][j] + other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return SimpleMatrix(result)

    def __sub__(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("행렬 크기가 일치하지 않습니다.")
        result = [
            [self.data[i][j] - other.data[i][j] for j in range(self.cols)]
            for i in range(self.rows)
        ]
        return SimpleMatrix(result)

    def __mul__(self, other):
        if self.cols != other.rows:
            raise ValueError("행렬 곱 조건 불만족")
        result = [
            [
                sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                for j in range(other.cols)
            ]
            for i in range(self.rows)
        ]
        return SimpleMatrix(result)

    def transpose(self):
        transposed = [
            [self.data[j][i] for j in range(self.rows)]
            for i in range(self.cols)
        ]
        return SimpleMatrix(transposed)

    def __repr__(self):
        return '\n'.join(['\t'.join(map(str, row)) for row in self.data])

# 사용 예시
arr1 = SimpleMatrix([[1, 2], [3, 4]])
arr2 = SimpleMatrix([[5, 6], [7, 8]])

print("arr1 + arr2")
print(arr1 + arr2,'\n')

print("\narr1 * arr2")
print(arr1 * arr2,'\n')

print("\narr1 transpose")
print(arr1.transpose(),'\n')

arr3 = SimpleMatrix([[1, 4], [3, 2], [4, 1]])
arr4 = SimpleMatrix([[3, 3], [3, 3]])
print(arr3 * arr4,'\n')

arr3 = SimpleMatrix([[2, 3, 2], [4, 2, 4], [3, 1, 4]])
arr4 = SimpleMatrix([[5, 4, 3], [2, 4, 1], [3, 1, 1]])
print(arr3 * arr4)

# transpose is when row of a matrices are set as columns of the matrix
# conditions - rowLen = colLen
# diagonal remains the same

def transposeMatrix(matrix: list[list[int]]):
    n = len(matrix)
    m = len(matrix[0])
    
    print(f"n: {n}, m: {m}")
    temp = [[-1 for _ in range(n)] for _ in range(m)]
    print(temp)
    for i in range(n):
        for j in range(m):
            print(f"j: {j}, i: {i}")
            temp[j][i] = matrix[i][j]
    
    print(temp)

matrix = [[1,2,3],[4,5,6]]
transposeMatrix(matrix=matrix)

n = 2
m=3

tmp = [[-1 for _ in range(n)] for _ in range(m)]
print(tmp)
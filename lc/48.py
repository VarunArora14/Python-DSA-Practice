from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        i = 0
        mid = n // 2
        while i < mid:
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
            i += 1

        print(matrix)
        # transpose via the diagonal
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


s = Solution()

matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
s.rotate(matrix=matrix)
print(matrix)

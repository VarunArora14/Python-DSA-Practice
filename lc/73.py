from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = [False for _ in range(len(matrix))]
        cols = [False for _ in range(len(matrix[0]))]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    rows[i] = True
                    cols[j] = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i] or cols[j]:
                    matrix[i][j] = 0

        # print(matrix)


sol = Solution()
matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
sol.setZeroes(matrix=matrix)

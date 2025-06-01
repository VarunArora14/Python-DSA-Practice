from typing import List


class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        ans_rows = m - k + 1
        ans_cols = n - k + 1
        ans = [[0 for _ in range(ans_cols)] for _ in range(ans_rows)]

        for r_start in range(ans_rows):
            for c_start in range(ans_cols):
                submatrix_elements = []
                for i in range(r_start, r_start + k):
                    for j in range(c_start, c_start + k):
                        submatrix_elements.append(grid[i][j])

                distinct_elements = sorted(list(set(submatrix_elements)))

                if len(distinct_elements) < 2:
                    ans[r_start][c_start] = 0
                else:
                    min_diff = float("inf")
                    for l_idx in range(len(distinct_elements) - 1):
                        diff = distinct_elements[l_idx + 1] - distinct_elements[l_idx]
                        min_diff = min(min_diff, diff)
                    ans[r_start][c_start] = min_diff

        return ans


grid = [[1, 8], [3, -2]]
k = 2
grid = [[3, -1]]
k = 1
sol = Solution()
print(sol.minAbsoluteDifference(grid, k))

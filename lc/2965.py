from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        st = set()
        n_square = n * n
        net_sum = int((n_square * (n_square + 1)) / 2)
        missing_val, repeated_val = -1, -1
        for i in range(n):
            for j in range(n):
                if grid[i][j] in st:
                    repeated_val = grid[i][j]
                else:
                    st.add(grid[i][j])
                    net_sum -= grid[i][j]

        missing_val = net_sum
        return [repeated_val, missing_val]


s = Solution()
grid = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
print(s.findMissingAndRepeatedValues(grid))
"""
We know len of grid is n and so elements inside will have values [1,2...n^2], so we can traverse this array and find the repeating element by checking
if any element occurs again. For the missing one, we know by formula that sum of x numbers from 1 to x is (x*(x+1))/2 and so we keep deducting
the elements of array if non-repeating.


"""

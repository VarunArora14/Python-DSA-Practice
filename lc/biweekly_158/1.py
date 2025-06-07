from collections import defaultdict
from typing import List


class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:
        xmaxy = defaultdict(int)

        for xi, yi in zip(x, y):
            xmaxy[xi] = max(xmaxy[xi], yi)

        if len(xmaxy) < 3:
            return -1

        top_y_values = sorted(xmaxy.values(), reverse=True)

        return sum(top_y_values[:3])


sol = Solution()
x = [1, 2, 1, 3, 2]
y = [5, 3, 4, 6, 2]

x = [1, 2, 1, 2]
y = [4, 5, 6, 7]
print(sol.maxSumDistinctTriplet(x, y))

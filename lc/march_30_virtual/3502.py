from typing import List


class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        stack = []
        res = []
        for c in cost:
            if len(stack) == 0:
                stack.append(c)
            elif stack[-1] > c:
                stack.append(c)

            res.append(stack[-1])

        return res


s = Solution()
cost = [5, 3, 4, 1, 3, 2]
cost = [1, 2, 4, 6, 7]
print(s.minCosts(cost=cost))

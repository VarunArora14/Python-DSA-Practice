from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0 for _ in range(2 * n)]

        for i in range(n):
            res[i] = res[n + i] = nums[i]

        return res


sol = Solution()
print(sol.getConcatenation([1, 2, 1]))

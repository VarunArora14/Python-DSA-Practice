from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        s = set()
        for num in nums:
            if num not in s:
                s.add(num)

        res = []
        for i in range(1, n + 1):
            if i not in s:
                res.append(i)

        return res


sol = Solution()
nums = [4, 3, 2, 7, 8, 2, 3, 1]
print(sol.findDisappearedNumbers(nums))

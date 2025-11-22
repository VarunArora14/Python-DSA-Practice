from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        for i in range(n):
            ctr = 0
            for j in range(n):
                if j != i:
                    if nums[i] > nums[j]:
                        ctr += 1
            res.append(ctr)

        return res


sol = Solution()
nums = [8, 1, 2, 2, 3]
print(sol.smallerNumbersThanCurrent(nums))

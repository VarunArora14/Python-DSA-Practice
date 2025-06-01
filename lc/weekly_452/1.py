from typing import List


class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        total = 1
        for num in nums:
            total *= num

        if total != target * target:
            return False

        n = len(nums)
        total_masks = 1 << n

        for mask in range(1, total_masks - 1):
            p = 1
            for i in range(n):
                if mask & (1 << i):
                    p *= nums[i]
                    if p > target:
                        break
            if p == target:
                return True

        return False


sol = Solution()
nums = [3, 1, 6, 8, 4]
# nums = [2, 5, 3, 7]
print(sol.checkEqualPartitions(nums, 24))

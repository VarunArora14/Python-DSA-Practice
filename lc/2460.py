from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            if nums[i] == nums[i + 1]:
                nums[i] = nums[i] * 2
                nums[i + 1] = 0
        idx = 0
        non_zero_idx = 0
        while idx < n:
            if nums[idx] != 0:
                nums[non_zero_idx] = nums[idx]
                non_zero_idx += 1
            idx += 1

        for i in range(non_zero_idx, n):
            nums[i] = 0  # set remaining nums to 0

        return nums


nums = [0, 1]
s = Solution()
print(s.applyOperations(nums))
""""
perform n-1 operations where we check nums[i] == nums[i+1], multiply nums[i]*2 and set nums[i+1] as 0, otherwise ignore and move to next element
"""

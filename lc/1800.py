from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        sum = nums[0]
        max_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                sum += nums[i]
                max_sum = max(sum, max_sum)
            else:
                sum = nums[i]  # start this new value

        return max_sum


nums = [3, 6, 10, 1, 8, 9, 9, 8, 9]
s = Solution()
print(s.maxAscendingSum(nums=nums))

"""
Here we have to find sum of ascending consecutive numbers in an array to maximize this sum and then return this sum as the answer
"""

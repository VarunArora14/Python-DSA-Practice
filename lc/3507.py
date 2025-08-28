from typing import List


class Solution:
    def check_non_decreasing(self, nums):
        n = len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return False

        return True

    def minimumPairRemoval(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        ops = 0
        while not self.check_non_decreasing(nums):
            min_pair_sum = float("inf")
            min_pair_start_idx = -1
            print(nums)
            # find the min pair
            for i in range(len(nums) - 1):
                curr_sum = nums[i] + nums[i + 1]
                if min_pair_sum > curr_sum:
                    min_pair_sum = curr_sum
                    min_pair_start_idx = i

            nums = nums[:min_pair_start_idx] + [min_pair_sum] + nums[min_pair_start_idx + 2 :]
            ops += 1

        return ops


nums = [5, 2, 3, 1]
s = Solution()
print(s.minimumPairRemoval(nums))

"""
We numbers in any order, if non-decreasing then remove the minimum pair and then check again
We create helper method which checks whether the array is non-decreasing

Then we check the array and if we find it not following non-decreasing then find the smallest pair and change it to it's sum and have the array modified
"""

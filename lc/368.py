from typing import List

# find subsets first of len 2 and more


class Solution:
    def __init__(self):
        self.max_value = 0
        self.max_arr = []

    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if len(nums) < 2:
            return nums

        nums.sort()
        dp = [(1, [nums[i]]) for i in range(len(nums))]

        print(dp)
        for i in range(len(nums)):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0:
                    if dp[j][0] + 1 > dp[i][0]:
                        # dp[i][0] = 1 + dp[j][0]
                        # dp[i][1] = dp[j][1][:] + [nums[i]]  # copy the array + the current elemen
                        dp[i] = (1 + dp[j][0], dp[j][1][:] + [nums[i]])

        max_arr = []
        for ele, arr in dp:
            if len(arr) > len(max_arr):
                max_arr = arr

        return max_arr


nums = [1, 2, 4, 8]
s = Solution()
print(s.largestDivisibleSubset(nums))

"""
We sort the main array and then for each element, we have dp[i] where i is the sorted element index and dp[i] contains the number of elements including nums[i] which
are multiple of nums[i].
We also need to maintain the subset which have this value as we have to return the array and NOT the count
"""

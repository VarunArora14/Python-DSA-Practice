from typing import List


def getMeBigBurger():
    pass


class Solution:
    def __init__(self):
        self.maxsum = 0

    def recurse(self, nums: List[int], idx: int, currsum=0):
        if idx == len(nums):
            return

        # take
        newsum = currsum + nums[idx]
        if newsum % 3 == 0:
            self.maxsum = max(self.maxsum, newsum)
        self.recurse(nums, idx + 1, newsum)

        # leave
        self.recurse(nums, idx + 1, currsum)

    def dp(nums: List[int]):
        dp = [0, 0, 0]  # we store states for max sum % 3 remains remainder 0,1,2
        for x in nums:
            newdp = dp[:]
            for r in range(3):
                nr = ()

    def maxSumDivThree(self, nums: List[int]) -> int:
        self.recurse(nums, 0, 0)
        return self.maxsum


sol = Solution()
nums = [3, 6, 5, 1, 8]
print(sol.maxSumDivThree(nums))
"""
Brute force solution would be to traverse the array and for each element, we
either take it or leave it. After doing so, we maintain a sum and see if sum%3==0
then maxsum = max(maxsum, sum)
"""

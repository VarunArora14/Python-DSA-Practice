from math import e
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        # base case
        if 0 not in nums:
            return len(nums) - 1

        prefs = [0 for _ in range(len(nums) + 1)]
        for i, num in enumerate(nums):
            prefs[i + 1] = prefs[i] + num

        one_count = 0  # if true it meas curr subarray has a 0 i it
        prev_zero = -1
        maxval = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                if prev_zero == -1:
                    maxval = max(maxval, prefs[i + 1])
                else:
                    print("i at maxval", i)
                    print(prefs[i], prefs[prev_zero + 1], prev_zero)
                    maxval = max(maxval, prefs[i + 1] - prefs[prev_zero + 1])  # diff
            else:
                if one_count == 0:
                    one_count += 1
                    continue
                else:
                    prev_zero = i

        return maxval


sol = Solution()
nums = [1, 1, 0, 1]
nums = [0, 1, 1, 1, 0, 1, 1, 0, 1]
print(sol.longestSubarray(nums))

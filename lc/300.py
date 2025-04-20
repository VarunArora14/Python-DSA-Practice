from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis_lengths = [1 for _ in range(len(nums) + 1)]
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    lis_lengths[i] = max(
                        lis_lengths[i], 1 + lis_lengths[j]
                    )  # on finding a smaller number before nums[i], we maximise the LIS till there to later use as solution of subproblem nums[i]

        print(lis_lengths)
        return max(lis_lengths)


s = Solution()
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(s.lengthOfLIS(nums))
"""
For finding the longest increasing subsequence till nums[i], we need to compute the LIS from [0..i-1]
"""

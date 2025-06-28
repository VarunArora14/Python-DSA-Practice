from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        nums = [(nums[i], i) for i in range(len(nums))]
        nums.sort(key=lambda x: (-x[0], x[1]))

        nums = nums[:k]
        nums.sort(key=lambda x: x[1])
        nums = [x[0] for x in nums]
        return nums


sol = Solution()
nums = [-1, -2, 3, 4]
k = 3
print(sol.maxSubsequence(nums, k))

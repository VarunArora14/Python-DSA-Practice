from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ctr = 0
        idx = 0
        while idx < len(nums):
            curr = 0
            if nums[idx] == 0:
                idx += 1
            else:
                while idx < len(nums) and nums[idx] == 1:
                    curr += 1
                    idx += 1
            max_ctr = max(max_ctr, curr)

        print(max_ctr)
        return max_ctr


sol = Solution()
nums = [1, 1, 0, 1, 1, 1]
sol.findMaxConsecutiveOnes(nums)

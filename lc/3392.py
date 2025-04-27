from typing import List


class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        counter = 0

        for i in range(n - 2):
            print(i, i + 1, i + 2)
            if nums[i + 1] == 2 * (nums[i] + nums[i + 2]):
                counter += 1

        return counter


sol = Solution()
nums = [1, 2, 1, 4, 1]
print(sol.countSubarrays(nums))

from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_ones, count_twos, count_zeros = 0, 0, 0

        for num in nums:
            if num == 0:
                count_zeros += 1
            elif num == 1:
                count_ones += 1
            elif num == 2:
                count_twos += 1

        nums[:count_zeros] = [0] * count_zeros
        nums[count_zeros : count_zeros + count_ones] = [1] * count_ones
        nums[count_zeros + count_ones :] = [2] * count_twos

        print(nums)


sol = Solution()
nums = [2, 0, 2, 1, 1, 0]
sol.sortColors(nums)

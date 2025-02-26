from typing import List


class Solution:
    def maxAbsoluteSumBrute(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_arr = [0 for _ in range(n + 1)]
        max_sum = 0
        for i in range(1, n + 1):
            prefix_arr[i] = nums[i - 1] + prefix_arr[i - 1]

        print(prefix_arr)

        for i in range(n + 1):
            for j in range(i + 1, n + 1):
                max_sum = max(max_sum, abs(prefix_arr[j] - prefix_arr[i]))

        return max_sum

    def maxAbsoluteSum(self, nums: List[int]) -> int:
        """
        Find the max sum of subarray separately of largest positive and negative sums separately and then return their max
        as the value (absolute value)
        """
        n = len(nums)
        max_sum = 0
        curr_pos_sum, curr_neg_sum = 0, 0
        for i in range(n):
            curr_pos_sum += nums[i]
            if curr_pos_sum < 0:
                curr_pos_sum = 0

            max_sum = max(max_sum, curr_pos_sum)

        for i in range(n):
            curr_neg_sum += nums[i]
            if curr_neg_sum > 0:
                curr_neg_sum = 0

            max_sum = max(max_sum, -curr_neg_sum)

        return max_sum


s = Solution()
nums = [2, -5, 1, -4, 3, -2]
print(s.maxAbsoluteSum(nums))

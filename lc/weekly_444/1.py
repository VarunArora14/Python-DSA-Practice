from typing import List


class Solution:
    def check_nondecreasing(self, arr):
        return all(arr[i] >= arr[i - 1] for i in range(1, len(arr)))

    def minimumPairRemoval(self, nums: List[int]) -> int:
        ops = 0

        while not self.check_nondecreasing(nums):
            min_sum = float("inf")
            min_idx = -1

            for i in range(len(nums) - 1):
                sum_val = nums[i] + nums[i + 1]
                if sum_val < min_sum:
                    min_sum = sum_val
                    min_idx = i
            # Replace the pair with their sum
            combined = nums[min_idx] + nums[min_idx + 1]
            nums = nums[:min_idx] + [combined] + nums[min_idx + 2 :]
            ops += 1

        return ops


s = Solution()
print(s.minimumPairRemoval([8]))

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        step_counter = 0
        for i in range(n):
            # print("nums", nums)
            if nums[i] == 1:
                continue
            elif nums[i] == 0:
                if i + 2 < n:
                    nums[i] = 0 if nums[i] == 1 else 1
                    nums[i + 1] = 0 if nums[i + 1] == 1 else 1
                    nums[i + 2] = 0 if nums[i + 2] == 1 else 1
                    step_counter += 1
                else:
                    print(nums)
                    return -1

        return step_counter


s = Solution()
nums = [0, 1, 1, 1]
print(s.minOperations(nums))

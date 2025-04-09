from typing import List


class Solution:
    def __init__(self):
        self.flag = False

    def backtrack(self, curr_arr: List[int], idx: int, nums: List[int]):
        if sum(curr_arr) == sum(nums) // 2:
            self.flag = True
            return

        for i in range(idx, len(nums)):
            tmp = curr_arr[:]
            tmp.append(nums[i])
            use = self.backtrack(tmp, i + 1, nums)
            tmp.pop()
            skip = self.backtrack(tmp, i + 1, nums)

            if use or skip:
                return

    def canPartition(self, nums: List[int]) -> bool:
        net_sum = sum(nums)
        if net_sum % 2 != 0:
            return False

        self.backtrack([], 0, nums)
        return self.flag


s = Solution()
nums = [1, 2, 3, 5]
print(s.canPartition(nums))


"""
we have list of nums and we find subsets such that total set get's divided, one way is to sort and find the subsets and check if their sum == net_sum/2
"""

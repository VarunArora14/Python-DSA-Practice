from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]

    def twoSumFaster(self, nums: List[int], target: int) -> List[int]:
        # we process the elements such that if we find the target - curr diff in hashmap then return the indexes
        mapper = {}
        n = len(nums)
        for i in range(n):
            diff = target - nums[i]
            if diff in mapper:
                return [mapper[diff], i]
            mapper[nums[i]] = i

        return [-1, -1]


sol = Solution()
# nums = [2, 7, 11, 15]
# target = 9
nums = [3, 2, 4]
target = 6
print(sol.twoSumFaster(nums=nums, target=target))

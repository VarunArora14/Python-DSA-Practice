from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        net_sum = n * (n + 1) // 2
        arr_sum = sum(nums)
        s = set()
        duplicate_value = -1
        for num in nums:
            if num in s:
                duplicate_value = num
                break
            else:
                s.add(num)

        missing_value = net_sum - (arr_sum - duplicate_value)
        return [duplicate_value, missing_value]


sol = Solution()
nums = [1, 2, 2, 4]
print(sol.findErrorNums(nums))

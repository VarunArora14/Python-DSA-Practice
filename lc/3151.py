from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        for i in range(1, n):
            f = nums[i] % 2 == 0
            s = nums[i - 1] % 2 != 0
            if f ^ s == 1:
                # print(i, f, s)
                return False

        return True


nums = [4, 3, 1, 6]
s = Solution()
print(s.isArraySpecial(nums=nums))

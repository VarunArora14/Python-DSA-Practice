from typing import List
import collections


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count, ans, n = collections.Counter(), 0, len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                ans += 8 * count[nums[i] * nums[j]]
                count[nums[i] * nums[j]] += 1
        return ans


s = Solution()
print(s.tupleSameProduct(nums=[2, 3, 4, 6]))

"""
=> find all the pairs of (nums[i],nums[j]) and keep their freq. If they occur again then do 8*counter[multiply_val] and then counter[multiply_val]+=1
=> store this value and return
"""

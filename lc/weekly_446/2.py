import bisect
from typing import List


class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        tail = []

        for num in nums:
            # Use bisect_right to allow duplicates (non-decreasing)
            idx = bisect.bisect_right(tail, num)
            if idx == len(tail):
                tail.append(num)
            else:
                tail[idx] = max(tail[idx], num)
        print(tail)
        return len(tail)


sol = Solution()
nums = [4, 2, 5, 3, 5]
print(sol.maximumPossibleSize(nums))
"""
Need to do in nlogn, we can create new array where we look for pos to add the new element num in nums and if 
"""

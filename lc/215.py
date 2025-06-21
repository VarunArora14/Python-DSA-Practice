import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, num)
            if len(q) > k:
                heapq.heappop(q)  # remove the smallest element

        return heapq.heappop(q)


sol = Solution()
nums = [3, 2, 1, 5, 6, 4]
print(sol.findKthLargest(nums, 3))

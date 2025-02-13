from typing import List
import heapq


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        q = []
        for num in nums:
            heapq.heappush(q, num)

        # base case: can't perform the min operations
        if len(q) < 2:
            return 0

        counter = 0

        while len(q) >= 2:
            counter += 1
            x = heapq.heappop(q)
            if x >= k:
                print(x)
                return counter - 1
            y = heapq.heappop(q)
            val = x * 2 + y
            heapq.heappush(q, val)  # add smaller number left after the operation on both numbers

        return counter


s = Solution()
nums = [999999999, 999999999, 999999999]
k = 1000000000
print(s.minOperations(nums=nums, k=k))

"""
We find the numbers in sorted manner which are smaller than k and then put them in heap - 
if len of heap >=2 then 2 pop and then operation min(x,y)*2 + max(x,y) and if this number is still smaller than k then push in heap

increment the counter for each operation to store the number of times the operation is performed

Even if there is number x which is less than k and number y which is larger than k, we have to perform this operation on nums, so we just check the smallest
number if >=k and if it is bigger then simply return the counter
"""

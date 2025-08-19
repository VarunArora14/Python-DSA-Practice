from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        counter, res = 0, 0

        for num in nums:
            if num == 0:
                counter += 1
            else:
                counter = 0
            res += counter
        return res


sol = Solution()
nums = [0, 0, 0, 2, 0, 0]
print(sol.zeroFilledSubarray(nums))

"""
find the 0's count of subarrays and then apply the formula n*n+1 /2 for them

example - [1,2,0,0,2,0,0,4] then we have [2,2] as 0's count of subarrays so we can do n*n+1 /2 and sum these values as 3 + 3 = 6 as the answer
Since the answer n*n+1 /2 is found by 1+2+...n, we can rather make it easier that if we encounter 0, we start this counting and add counter to res
and if num is not 0 then reset the counter=0 
"""

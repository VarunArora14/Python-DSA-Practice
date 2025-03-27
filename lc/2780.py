from typing import Counter, List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        lcount = 0
        dominant, rcount = max(Counter(nums).items(), key=lambda x: x[1])
        for i, x in enumerate(nums):
            lcount += x == dominant
            rcount -= x == dominant
            if lcount > (i + 1) // 2 and rcount > (len(nums) - (i + 1)) // 2:
                return i
        return -1


s = Solution()

"""
Here we first find the dominant number and it's occurences and then traverse nums for the split condition - The arrays after split must have the same element as the dominant element
- lcount + x==dominant means add 1 to lcount if element is dominant element, and we do same for rcount
- we then check condition whether the left half of array (i+1)//2 and right half (n-i-1)//2 have dominant count more than half of elements, if yes then return the index

We return false as the base case
"""

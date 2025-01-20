from typing import List
import ast

class Solution:
    def lcs_brute(self, nums:List[int]):
        lcs=0
        s=set()
        for num in nums:
            s.add(num) 
        
        for num in nums:
            curr=num
            count=0
            while curr in s:
                curr-=1
                count+=1
            lcs = max(lcs, count)
        return lcs

    def lcs(self, nums:List[int]):
        lcs=0
        s = set(nums)
        
        for num in nums:
            if num-1 in s:
                continue
            length=1
            while num+1 in s:
                num+=1
                length+=1
            lcs = max(lcs, length)
        return lcs

s=Solution()
nums = ast.literal_eval(input()) # parse the string as array
# print(nums)
print(s.lcs(nums=nums))
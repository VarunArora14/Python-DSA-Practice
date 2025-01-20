from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        nums = [i for i in range(1,m+1)]
        res=[]
        print(nums)
        for q in queries:
            # q is element to find and to put at top of the list
            pos=-1
            for i in range(m):
                if nums[i] == q:
                    pos=i
                    break
            for i in range(pos,-1,-1):
                nums[i]=nums[i-1] # go forward till pos position replaced
            nums[0]=q
            print(f"nums at query {q}: {nums}")
            res.append(pos)
        return res

s=Solution()
print(s.processQueries(queries=[4,1,2,2],m=4))
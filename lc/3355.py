from typing import List


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        tmp = [0 for _ in range(len(nums) + 1)]

        # store the start as 1 and end+1 as -1 so we create prefix array from this
        for [left, right] in queries:
            tmp[left] += 1
            tmp[right + 1] -= 1

        curr = 0
        for i in range(len(tmp)):
            curr += tmp[i]
            tmp[i] = curr

        for i in range(len(tmp)):
            if nums[i] > tmp[i]:
                return False

        return True


sol = Solution()
queries = [[1, 3], [0, 2]]
nums = [4, 3, 2, 1]
print(sol.isZeroArray(nums=nums, queries=queries))

"""
Here we have been given queries 1e5 at max and a nums array which is also 1e5 at max, and we have to see whether for each query, if the array can become
all 0's or not. 

For each query [l,r] - 
- we choose subset of elements from nums[l:r] and then reduce their amount by 1. This subset can have 0 elements as well
- we have to make sure that after all queries are applied, the array has all 0 elements

Now, for the array to NOT have all 0's, the number of queries of nums[i] must be smaller than nums[i], which means queries in range [l,r] must
have index i, l<=i<=r less than nums[i].

This means, we should count the number of times for each index, we can perform the operation of reduction of nums[i] by 1. As per the constraints, we
cannot have 2 loops so it's better we find a single traversal way.

The only way is prefix sum method but we need to find way so that we calculate operations of each index correctly - 

assume - queries = [[1,2], [4,6] ]
this means, the deductions on each index can be [0,1,1,0,1,1,1,0]. Now, you can observe the indices 1,2,4,5,6 are with 1's while others are 0

Another example - [ [1,4], [2,5], [3,4], [6,7] ]
pref_sum = [0,1,2,3,3,1,1,1,0] => Index 0 does not have any operation, index 1 has single (1st query), index 2 has 2 operations at max(1st and 2nd query), index 3 and 4
have 3 operations at max (1,2,3 query) and index 5 has 1 query (2nd query) and index 6,7 has 1 deduction at max (last query)

Using this information, we can see that if nums[i] > pref_sum[i] then not possible.

Now, to create this prefix sum, we first sort the queries and then for each query, we have a variable curr which adds +1 for l coming and -1 for r+1 coming
(which means that query cannot be applied after this)


The unique thing is how we handle the queries. We could have traversed each query and then done tmp[i]+=1 for [l,r] of each query but the constraints
don't allow this so we instead store the value at indices tmp[l]+=1 and tmp[r+1]-=1 and then we use a variable curr when does curr+=tmp[i] and then
we store tmp[i] as curr. This stores the prefix sum values in the tmp array then (can create new array otherwise) and this curr makes tmp[i] store the
values as we want -> if multiple queries have this index in [l,r] add +1 to this array. Later we check whether tmp[i]<nums[i] for faslse condition
"""

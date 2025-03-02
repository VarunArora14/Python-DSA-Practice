from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        mapper = dict()

        for id, val in nums1:
            if id not in mapper:
                mapper[id] = 0
            mapper[id] += val

        for id, val in nums2:
            if id not in mapper:
                mapper[id] = 0
            mapper[id] += val

        res = []
        for k, v in mapper.items():
            res.append([k, v])

        return sorted(res, key=lambda x: x[0])


s = Solution()
nums1 = [[2, 4], [3, 6], [5, 5]]
nums2 = [[1, 3], [4, 3]]
print(s.mergeArrays(nums1=nums1, nums2=nums2))

"""
We have array with nums[i] as id -> val mapping and we want their sums to be taken for the same ids and return the id -> val pair as 2d array again sorted in ascending order
of the ids
"""

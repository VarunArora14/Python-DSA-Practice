from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        mapper = {}
        for num in nums:
            if num not in mapper:
                mapper[num] = 0
            mapper[num] += 1

        for k, v in mapper.items():
            if v % 2 != 0:
                return False

        return True


s = Solution()
print(s.divideArray([3, 2, 3, 2, 2, 2]))

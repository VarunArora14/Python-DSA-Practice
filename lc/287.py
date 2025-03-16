from typing import List


class Solution:
    def binary_search(self, nums):
        start, end = 1, len(nums) - 1
        while start < end:
            mid = (start + end) // 2
            less_counter = 0
            for num in nums:
                if num <= mid:
                    less_counter += 1

            if less_counter > mid:
                end = mid  # potential answer
            else:
                start = mid + 1

        return end  # on while condition failure it is same as end

    def findDuplicate(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return nums[0]

        return self.binary_search(nums)


s = Solution()
nums = [3, 3, 3, 3, 3]
print(s.findDuplicate(nums))

"""
We take 1 and largest value of nums and do binary search. For each mid val, if number of elements in nums <=mid == mid then go right else left
"""

from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]

        start, end = 0, len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if mid % 2 == 1:
                mid -= 1
            if mid + 1 < len(nums) and nums[mid] == nums[mid + 1]:
                start = mid + 2
            else:
                end = mid
            if start == end:
                return nums[start]
        return -1


sol = Solution()
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(sol.singleNonDuplicate(nums))

"""
- The number of ele in this array always odd
- It follows pattern of even-odd pairs before the once-occuring element comes and after that it follows odd-even
- if the middle element at even index(1 based count) then it means single element on the right side of array otherwise on the left
- if on left then we make mid = mid-1 and if on right then 
"""

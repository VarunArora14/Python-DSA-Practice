from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        if nums[0] != nums[1]:
            return nums[0]

        if nums[-1] != nums[-2]:
            return nums[-1]

        start, end = 1, len(nums) - 2
        while start <= end:
            mid = (start + end) // 2
            if (nums[mid] != nums[mid - 1]) and (nums[mid] != nums[mid + 1]):
                return nums[mid]
            elif mid % 2 != 0 and nums[mid] == nums[mid - 1]:
                end = mid - 1
            elif mid % 2 == 0 and nums[mid] == nums[mid + 1]:
                start = mid + 1
        return -1


sol = Solution()
nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]
print(sol.singleNonDuplicate(nums))

"""
- The number of ele in this array always odd
- It follows pattern of even-odd pairs before the once-occuring element comes and after that it follows odd-even
- Go to mid position, check if prev or next ele is not same => return ele
    - if idx is odd and next ele is same then it follows odd-even so make end=mid-1
    - otherwise make start = mid+1
"""

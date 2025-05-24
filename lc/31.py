from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        n = len(nums)
        i = 0
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                break
        print(i)  # break when ascending order from end breaks

        # i=0 means the first element so consider i<0 - potential edge failure
        if i < 0:
            nums.sort()
        else:
            tmp = nums[i]
            j = 0
            for j in range(i + 1, n):
                if nums[j] > nums[i] and nums[j] > tmp:
                    tmp = nums[j]

            nums[i], nums[j] = nums[j], nums[i]

        # print(nums)


nums = [1, 2]
sol = Solution()
sol.nextPermutation(nums)

"""
Conditions to check - 
- The array from end must be in descending order and if that breaks, then we consider next permutation of the number because when nums[i]<nums[i+1], only then we can swap it with a bigger number on the right (just bigger than nums[i])
- The right of the array to nums[i] is already sorted technically, so just find the just bigger number, then swap nums[i], nums[just_bigger_idx] and it should work. Also, no duplicates exist in array for additonal complexity
- Edge case: If we cannot find i>0 and i becomes 0, that means array already sorted in descending order. In this case the next permutation will be the array sorted ascending wise
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        ui = 0
        for i in range(len(nums)):
            if nums[i] in s:
                continue
            else:
                nums[ui] = nums[i]
                ui += 1

            s.add(nums[i])
        print("new nums", nums)
        return ui - 1


sol = Solution()
nums = [1, 1, 2]
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(sol.removeDuplicates(nums=nums))

"""
here we need unique value iterator to mark the indexes till which we have saved the unique elements and will need a map to check uniqueness as well
"""

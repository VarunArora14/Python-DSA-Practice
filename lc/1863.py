from typing import List


class Solution:
    def __init__(self):
        self.subsets_arr = []

    def find_subsets(self, curr_arr: list, idx: int, nums):
        self.subsets_arr.append(curr_arr[:])  # pass the copy as append and pop might reflect their changes otherwise

        for i in range(idx, len(nums)):
            curr_arr.append(nums[i])
            self.find_subsets(curr_arr=curr_arr, idx=i + 1, nums=nums)
            curr_arr.pop()

    def calculate_xor(self, arr):
        if arr == []:
            return 0
        if len(arr) == 1:
            return arr[0]

        res = arr[0]
        for num in arr[1:]:
            res = res ^ num

        return res

    def subsetXORSum(self, nums: List[int]) -> int:
        self.find_subsets(curr_arr=[], idx=0, nums=nums)
        print(self.subsets_arr)

        result = 0
        for s in self.subsets_arr:
            result += self.calculate_xor(arr=s)

        return result


s = Solution()
nums = [5, 1, 6]
print(s.subsetXORSum(nums))

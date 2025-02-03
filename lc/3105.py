from typing import List


class Solution:
    def check_strictly_increasing(self, nums: List[int], start: int, end: int):
        if start == end:
            return True

        for i in range(start, end):
            if nums[i] >= nums[i + 1]:
                return False

        # print("returning True", nums[i], nums[i + 1])
        return True

    def check_strictly_decreasing(self, nums: List[int], start: int, end: int):
        print("hey", start, end)
        if start == end:
            return True

        for i in range(end, start, -1):
            print(nums[i], nums[i - 1])
            if nums[i] >= nums[i - 1]:
                return False
        # print(f"returning True, start: {start}, end: {end}, len: {end - start + 1}")
        return True

    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 1
        for i in range(n):
            for j in range(i + 1, n):
                if self.check_strictly_increasing(nums, i, j):
                    max_len = max(max_len, j - i + 1)
                if self.check_strictly_decreasing(nums, i, j):  # reverse order
                    max_len = max(max_len, j - i + 1)

        return max_len


nums = [1, 4, 3, 3, 2]
s = Solution()
print(s.longestMonotonicSubarray(nums=nums))


"""
We have to check whether the array contains any subarray which is stricty increasing or decreasing. Since the array size is very small, we have to just check
all subarrays.
We can do the operation once with array without any change and then array reversed (to find strictly decreasing order)

Easier and faster implementation of sliding windows till increasing - 


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        temp_count = 1
        n = len(nums)
        max_v = 1
        for i in range (1, n):
            if nums[i] > nums[i-1]:
                temp_count += 1
                max_v = max(temp_count, max_v)
            else:
                temp_count = 1
        temp_count = 1
        for i in range (1,n):
            if nums[i] < nums[i-1]:
                temp_count += 1                
                max_v = max(temp_count, max_v)
            else:
                temp_count = 1
        return max_v



"""

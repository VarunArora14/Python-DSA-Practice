from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        for start in range(n):
            i = 0
            is_sorted = True  # flag to set False if not sorted in non-decreasing
            while i < n - 1:  # compares next element as well
                if nums[(start + i) % n] > nums[(start + i + 1) % n]:  # take modulus to manage overflow
                    is_sorted = False
                    break
                i += 1

            if is_sorted:
                return True

        return False


nums = [1, 2, 3]
s = Solution()
print(s.check(nums=nums))

"""
Here we have to find whether the array has been sorted at least once and then rotated. For this, we traverse the array from each position to next n elements (n being length of the array), and check for each number that is arr[i]<=arr[(i+1)%n] then continue otherwise return False.
This approach will take O(n^2) time as we start with each element and we do entire array traversal in worst case for each element.
"""

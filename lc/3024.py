from typing import Counter, List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        s1, s2, s3 = nums[0], nums[1], nums[2]

        if s1 + s2 <= s3 or s2 + s3 <= s1 or s1 + s3 <= s2:
            return "none"

        keys = len(Counter(nums).keys())
        if keys == 1:
            return "equilateral"
        elif keys == 2:
            return "isosceles"
        else:
            return "scalene"

from collections import Counter
from typing import List


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        arr = []

        for i in range(n - k + 1):
            window = nums[i : i + k]
            freq = Counter(window)
            sorted_freq = sorted(
                freq.items(), key=lambda x: (-x[1], -x[0])
            )  # first consider the value/occurences, then number to be larger for sort
            top_x = set(num for num, _ in sorted_freq[:x])  # get only the key names, top x
            x_sum = sum(num for num in window if num in top_x)
            arr.append(x_sum)

        return arr


sol = Solution()
nums, k, x = [1, 1, 2, 2, 3, 4, 2, 3], 6, 2
print(sol.findXSum(nums, k, x))

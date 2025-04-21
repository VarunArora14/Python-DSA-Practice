from typing import List


class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        net_sum = 0
        for d in differences:
            net_sum += d


sol = Solution()
"""
pref_sum[i] = diff[i] - diff[0] => h[i+1] - h[0]
pref_sum[i] = h[i+1] - h[0] => hk - h[0]

now, we want to find the minimum and max value of hk such that it remains in bounds

lower <= hk - h0 <= upper

min value is when hk-h0 = lower or whe pref_sum[i] == lower or closest to lower
max value is hk-h0 = upper where pref_sum[i] == upper or closest to upper (yet smaller)

"""

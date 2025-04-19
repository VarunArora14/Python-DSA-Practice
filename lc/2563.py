import bisect
from typing import List


class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        ans = 0
        for idx, num in enumerate(nums):
            # find smallest indices where lower - nums[i] can be inserted (which are nums[j] values)
            left_bound = bisect.bisect_left(nums, lower - num, lo=idx + 1, hi=len(nums))
            right_bound = bisect.bisect_right(nums, upper - num, lo=idx + 1, hi=len(nums))
            print(right_bound, left_bound)
            ans += right_bound - left_bound

            # since right bound is the next index, it provides total element count, otherwise it could have been end-start+1

        return ans


sol = Solution()
nums = [0, 1, 7, 4, 4, 5]
print(sol.countFairPairs(nums, lower=3, upper=6))
"""
with idx, num in enumerate, we have lo=i+1 set because we are trying to find nums[j] potential values
where num represents nums[i]. If we set lo=0, it violates condition i<j for fair pairs

We do not have lo=0 as it leads to repetitions as well as failure of condition that i<j

So we find nums[j] values upper and lower bound from i+1 to len(nums)

bisect_left find index where lower-nums[i] can be inserted maintaining the sorted order. For us, it gives 
the smallest position where nums[lower_bound] + nums[i] is >=lower
and then we do same for bisect_right where we find index upper_bound upper-nums[i] can be inserted,
since this provides the next index if x already in arr, we know the range is from [lower_bound, upper_bound-1]

bisect_left gives the starting index of the range.
bisect_right gives the ending index exclusive of the range.
"""

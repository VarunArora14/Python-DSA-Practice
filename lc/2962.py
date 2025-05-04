from typing import List


class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        max_ctr = 0
        start = 0
        subs = 0
        for end, num in enumerate(nums):
            if num == max_val:
                max_ctr += 1

            while max_ctr >= k:
                if nums[start] == max_val:
                    max_ctr -= 1
                
                start += 1

            # there are exact start subarrays ending with index end
            subs += start
        return subs


sol = Solution()
nums = [1, 4, 2, 1]
k = 3
print(sol.countSubarrays(nums, k))

"""
The idea behind solving subarrays questions is that you traverse the array with 'end' as the index
and when a certain condition is met, you do the processing and make the window smaller until it is not
met again.

The previous approach where we do operation of subs+=len(nums) - k is wrong as we should look at the
count in left subarray and not right. We are moving 'end' to right which considers the new array and this
approach of considering smaller to larger index makes correct sense as you leave many left subarrays otherwise.

The operation to do when max_val>=k is result+=
"""

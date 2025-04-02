from typing import List


class Solution:
    def maximumTripletValueUnoptimised(self, nums: List[int]) -> int:
        max_val = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    max_val = max(max_val, (nums[i] - nums[j]) * nums[k])

        return max_val

    def maximumTripletValue(self, nums: List[int]) -> int:
        result = 0
        best_diff = (
            0  # Maxmimize this value so (nums[i] - nums[j]) is largest as it before nums[k] to compute the largest val
        )
        max_i = 0  # Keep the largest values of nums[i] as 1 factor for best_diff as this will help us make the best_diff as it requires 2 variables and we rather store this nums[i] in a variable rather than iterating the array again

        for num in nums:
            # Treat current num as nums[k]
            result = max(result, best_diff * num)  # find the amount before changing the best_diff and max_i

            # Treat current num as nums[j] for next iteration to consider newer best_diff if it is bigger
            best_diff = max(best_diff, max_i - num)

            # Treat current num as nums[i] for next iteration
            max_i = max(max_i, num)

        return result


"""
We have to traverse the array such that for 3 indices i,j,k with i<j<k, we find the largest value of (nums[i] - nums[j]) * nums[k]
For this, we need to have 3 loops as we cannot sort this array (ordering of indices matters)
and then store this max value and return back to user if non negative
"""

s = Solution()
nums = [1, 2, 3]
print(s.maximumTripletValue(nums))

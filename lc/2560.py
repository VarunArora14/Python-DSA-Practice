import heapq
from typing import List

from sortedcontainers import SortedList


class Solution:
    def minCapability(self, nums, k):
        # Store the maximum nums value in maxReward.
        min_reward, max_reward = 1, max(nums)
        total_houses = len(nums)

        # Use binary search to find the minimum reward possible.
        while min_reward < max_reward:
            mid_reward = (min_reward + max_reward) // 2
            possible_thefts = 0

            index = 0
            while index < total_houses:
                if nums[index] <= mid_reward:
                    possible_thefts += 1
                    index += 2  # Skip the next house to maintain the non-adjacent condition
                else:
                    index += 1

            if possible_thefts >= k:
                max_reward = mid_reward
            else:
                min_reward = mid_reward + 1

        return min_reward


s = Solution()
nums = [24, 1, 55, 46, 4, 61, 21, 52]
k = 3
print(s.minCapability(nums, k))

"""
Here, the idea was to find k non-adjacent houses. This was the hint to binary search. Since we can have any houses chosen, even in between and not necessarily two houses robbed
have 1 house between them! This is very important hint that it may either be DP or binary search.

The dynamic programming solution involves a state dp[houseIndex][numberOfHousesRobbed]. Since we iterate over n houses and track up to k robbed houses, 
the problem becomes more complex, and solving it with dynamic programming takes O(n⋅k) time.

We use binary search to find a value mid_reward such that this value has at least k houses non adjacent smaller than it and then we keep making mid_reward smaller
if we have found a solution by making max_reward = mid_reward (store the mid_reward as it is one answer to store)

and we keep making the values smaller as we find results storing max_reward = mid_reward to store potential answer.

If smaller than k potential_thefts then we do min_reward = mid_reward+=1 which takes the upper bound now or gets completed as min_reward = max_reward
"""

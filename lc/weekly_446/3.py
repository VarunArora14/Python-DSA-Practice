from typing import List


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        current_mods = [0] * k
        for num in nums:
            mod = num % k
            new_mods = [0] * k
            for x in range(k):
                if current_mods[x]:
                    new_x = (x * mod) % k
                    new_mods[new_x] += current_mods[x]
            new_mods[mod] += 1  # Add the subarray consisting of the current element alone
            for x in range(k):
                result[x] += new_mods[x]
            current_mods = new_mods.copy()  # Update current_mods for the next iteration
        return result


nums = [1, 1, 2, 1, 1]
k = 2
sol = Solution()
print(sol.resultArray(nums=nums, k=k))

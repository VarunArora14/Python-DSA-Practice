from typing import List


class Solution:
    def countInterestingSubarrays(self, nums: List[int], modulo: int, k: int) -> int:
        n = len(nums)
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + (nums[i] % modulo == k)

        print(pref)

        result = 0
        for i in range(1, len(pref)):
            for j in range(i):
                if pref[i] - pref[j] % modulo == k:
                    if i == j and nums[i - 1] % modulo != k:
                        continue
                    print(i, j, pref[i] - pref[j])
                    result += 1

        return result


sol = Solution()
nums = [3, 2, 4]
modulo = 2
k = 1

nums = [3, 1, 9, 6]
modulo = 3
k = 0

print(sol.countInterestingSubarrays(nums=nums, modulo=modulo, k=k))

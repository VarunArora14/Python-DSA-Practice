from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        vis = set()
        n = len(nums)
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                k, l = j + 1, n - 1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        if (nums[i], nums[j], nums[k], nums[l]) not in vis:
                            res.append((nums[i], nums[j], nums[k], nums[l]))
                            vis.add((nums[i], nums[j], nums[k], nums[l]))
                        k += 1
                        l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] > target:
                        l -= 1
                    else:
                        k += 1
        return res


sol = Solution()
nums = [1, 0, -1, 0, -2, 2]
target = 0
print(sol.fourSum(nums, target))

# can add addition check of nums[i] == nums[i+1] for handling duplicates instead of set

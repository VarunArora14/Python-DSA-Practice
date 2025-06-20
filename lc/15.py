from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        unique = set()
        for i in range(len(nums)):
            j, k = i + 1, len(nums) - 1
            while j < k:
                cur_sum = nums[i] + nums[j] + nums[k]
                if cur_sum == 0 and (nums[i], nums[j], nums[k]) not in unique:
                    unique.add((nums[i], nums[j], nums[k]))
                    j += 1
                    k -= 1
                elif cur_sum < 0:
                    j += 1
                else:
                    k -= 1

        res = [u for u in unique]
        return res

    def three_sum_optimized(self, nums: List[int]):
        nums.sort()
        res = []
        for i in range(len(nums) - 2):
            print(i)
            # duplicate handling
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j, k = i + 1, len(nums) - 1

            while j < k:
                target = nums[i] + nums[j] + nums[k]
                if target == 0:
                    res.append((nums[i], nums[j], nums[k]))

                    # duplicate handling after match found
                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1
                elif target < 0:
                    j += 1
                else:
                    k -= 1
        return res


sol = Solution()
res = sol.three_sum_optimized(nums=[-1, 0, 1, 2, -1, 4])
print(res)

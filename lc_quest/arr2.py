from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        mid_pos = n
        print(mid_pos)
        res = []
        for i in range(mid_pos):
            res.append(nums[i])
            res.append(nums[mid_pos + i])
            # print(f"nums[i]: {nums[i]}, nums[mid_pos+i]: {nums[mid_pos + i]}")

        return res


nums = [2, 5, 1, 3, 4, 7]
n = 3
sol = Solution()
print(sol.shuffle(nums, n))

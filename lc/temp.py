from typing import List


class Solution:
    def minimalHeaviestSetA(self, arr: List[int]) -> List[int]:
        arr.sort()
        n = len(arr)
        arr_sum = sum(arr)
        half_sum = arr_sum // 2  # the finding sum must be greater than this value
        # print(half_sum)
        curr_sum = 0
        for i in range(n - 1, -1, -1):
            curr_sum += arr[i]

            if curr_sum > half_sum:
                return arr[i:]

        return []


s = Solution()

print(s.minimalHeaviestSetA([3, 7, 5, 6, 2]))  # [6,7]
print(s.minimalHeaviestSetA([5, 3, 2, 4, 1, 2]))  # [4,5]
print(s.minimalHeaviestSetA([4, 2, 5, 1, 6]))  # [5,6]

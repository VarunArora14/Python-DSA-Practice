from typing import List


class Solution:
    def bs(self, nums: List[int]):
        start, end = min(nums), max(nums)
        end = min(end, len(nums))
        start = min(start, len(nums))
        print(end)
        ans = start
        while start <= end:
            mid = (start + end) // 2
            counter = 0
            for num in nums:
                if num >= mid:
                    counter += 1

            if counter >= mid:
                ans = mid
                # print("counter: ", counter, "mid: ", mid)
                start = mid + 1
            else:
                # choose a smaller mid for H-index
                end = mid - 1

        return ans

    def hIndex(self, citations: List[int]) -> int:
        return self.bs(citations)

from typing import List


class Solution:
    def helper(self, piles, h, banana_speed):
        taken_hours = 0
        for p in piles:
            taken_hours += (p + banana_speed - 1) // banana_speed  # ceil

        if taken_hours > h:
            return False

        return True

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start, end = 1, max(piles)  # define the lower and upper limit

        while start < end:
            banana_speed = (end + start) // 2
            print(banana_speed)
            if self.helper(piles=piles[:], banana_speed=banana_speed, h=h):
                end = banana_speed
            else:
                start = banana_speed + 1  # move right to more speed

        return start


s = Solution()
piles = [312884470]
h = 312884469

print(s.minEatingSpeed(piles, h))

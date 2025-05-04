from collections import Counter
from typing import List


class Solution:
    def __init__(self):
        self.rotations = float("inf")

    def checkValidRotations(self, value, tops, bottoms):
        n = len(tops)
        # if any domino exists such that their side does not contain value, then return False
        for i in range(len(tops)):
            if tops[i] == value or bottoms[i] == value:
                continue
            else:
                return False

        self.rotations = min(n - tops.count(value), n - bottoms.count(value), self.rotations)

        return True

    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        counter = Counter()
        for t in tops:
            counter[t] += 1
        for b in bottoms:
            counter[b] += 1

        half_size = len(tops)
        for k, v in counter.items():
            if v >= half_size:
                self.checkValidRotations(value=k, tops=tops, bottoms=bottoms)

        if self.rotations < 1e5:
            return self.rotations
        return -1


sol = Solution()
tops = [1, 2, 1, 1, 1, 2, 2, 2]
bottoms = [2, 1, 2, 2, 2, 2, 2, 2]
print(sol.minDominoRotations(tops=tops, bottoms=bottoms))

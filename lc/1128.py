from collections import Counter
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counter = Counter()
        for d in dominoes:
            f = min(d)
            s = max(d)

            counter[(f, s)] += 1

        res = 0
        for k, v in counter.items():
            if v >= 2:
                res += int((v * (v - 1)) / 2)

        return res


sol = Solution()
dominoes = [[1, 2], [1, 2], [1, 1], [1, 2], [2, 2]]
print(sol.numEquivDominoPairs(dominoes=dominoes))

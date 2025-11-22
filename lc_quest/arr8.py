from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        target = [0] + target
        for i in range(1, len(target)):
            diff = target[i] - target[i - 1] - 1
            res += diff * ["Push"] + diff * ["Pop"]
            res += ["Push"]  # push new element

        return res


sol = Solution()
target = [1, 3]
n = 4
print(sol.buildArray(target, n))

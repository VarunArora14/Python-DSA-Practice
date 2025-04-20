from collections import Counter
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        res = 0
        for k, v in counter.items():
            group_size = k + 1
            groups_count = (v + group_size - 1) // group_size  # ceil
            print(group_size, groups_count)
            res += groups_count * group_size

        return res


s = Solution()
answers = [1, 1, 2]
print(s.numRabbits(answers))

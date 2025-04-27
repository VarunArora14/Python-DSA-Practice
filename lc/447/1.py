import bisect
from typing import List


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        row_map = {}
        col_map = {}
        for x, y in buildings:
            row_map.setdefault(x, []).append(y)
            col_map.setdefault(y, []).append(x)

        for lst in row_map.values():
            lst.sort()
        for lst in col_map.values():
            lst.sort()

        count = 0
        # check each building all dirs
        for x, y in buildings:
            ys = row_map[x]
            pos_y = bisect.bisect_left(ys, y)
            has_left = pos_y > 0
            has_right = pos_y < len(ys) - 1

            xs = col_map[y]
            pos_x = bisect.bisect_left(xs, x)
            has_above = pos_x > 0
            has_below = pos_x < len(xs) - 1

            if has_left and has_right and has_above and has_below:
                count += 1

        return count


sol = Solution()
n = 3
buildings = [[1, 1], [1, 2], [2, 1], [2, 2]]
print(sol.countCoveredBuildings(n=n, buildings=buildings))

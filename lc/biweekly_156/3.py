from collections import Counter, defaultdict
from functools import lru_cache
from typing import List


class Solution:
    def maxWeight(self, n: int, edges: List[List[int]], k: int, t: int) -> int:
        graph = defaultdict(list)

        for u, v, w in edges:
            graph[u].append((v, w))

        @lru_cache
        def dfs(u, rem_steps):
            if rem_steps == 0:
                return {0}
            sums = set()
            for v, w in graph[u]:
                for sub_sum in dfs(v, rem_steps - 1):
                    total = w + sub_sum
                    if total < t:
                        sums.add(total)
            return sums

        best = -1
        for start in range(n):
            for path_sum in dfs(start, k):
                if path_sum > best:
                    best = path_sum

        return best


sol = Solution()
n = 3
edges = [[0, 1, 1], [1, 2, 2]]
k = 2
t = 4

n = 3
edges = [[0, 1, 2], [0, 2, 3]]
k = 1
t = 3


n = 3
edges = [[0, 1, 6], [1, 2, 8]]
k = 1
t = 6
print(sol.maxWeight(n, edges, k, t))

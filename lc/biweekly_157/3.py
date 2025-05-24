from collections import deque
from typing import List


class Solution:
    def assignEdgeWeights(self, edges: List[List[int]]) -> int:
        mod = int(1e9 + 7)
        n = max(max(u, v) for u, v in edges)
        adj = [[] for _ in range(n + 1)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        depth = [-1] * (n + 1)
        depth[1] = 0
        q = deque([1])  # root
        while q:
            u = q.popleft()
            for w in adj[u]:
                if depth[w] == -1:
                    depth[w] = depth[u] + 1
                    q.append(w)

        # ignore the root, get max depth
        d = max(depth[1:])
        if d == 0:
            return 0

        # half of the 2^d are odd
        return pow(2, d - 1, mod)


sol = Solution()
edges = [[1, 2], [1, 3], [3, 4], [3, 5]]
print(sol.assignEdgeWeights(edges=edges))

from collections import deque
from typing import List


class Solution:
    def __init__(self):
        self.res = []
        self.vis = set()

    def dfs_helper(self, graph: dict, src: int):
        self.res.append(src)
        self.vis.add(src)

        for nbr in graph[src]:
            if nbr not in self.vis:
                self.dfs_helper(graph=graph, src=nbr)

    def dfs(self, graph, src):
        self.res = []  # Reset result list
        self.vis = set()  # Reset visited set
        self.dfs_helper(graph, src)
        return self.res

    def bfs(self, graph: dict, src: int):
        q = deque()
        vis = set()
        bfs_res = []

        q.append(src)
        vis.add(src)

        while len(q):
            tmp = []
            for _ in range(len(q)):
                top = q.popleft()
                bfs_res.append(top)
                for nbr in graph[top]:
                    if nbr not in vis:
                        tmp.append(nbr)
                        vis.add(nbr)
            q = deque(tmp)  # go to next level

        return bfs_res

    def create_graph(self, V: int, adj: List[List[int]]):
        graph = {}
        for i in range(len(adj)):
            for nbr in adj[i]:
                if i not in graph:
                    graph[i] = []
                graph[i].append(nbr)

        return graph


V = 5
adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

sol = Solution()
graph = sol.create_graph(V, adj)
print(sol.dfs(graph=graph, src=0))
print(sol.bfs(graph, 0))

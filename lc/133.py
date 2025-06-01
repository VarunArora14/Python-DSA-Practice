from collections import deque
from typing import List, Optional


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def createGraph(adj: List[List[int]]):
    graph = {}
    for i in range(len(adj)):
        if i + 1 not in graph:
            graph[i + 1] = []

        for val in adj[i]:
            graph[i + 1].append(val)

    print(graph)


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return node

        mapper = {}

        def helper(node):
            if node in mapper:
                return mapper[node]

            mapper[node] = Node(node.val)
            for nbr in node.neighbors:
                mapper[node].neighbors.append(helper(nbr))

            return mapper[node]

        return helper(node)

    def bfs(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return node

        mapper = {}
        mapper[node] = Node(node.val)

        q = deque([])
        q.append(node)

        while len(q):
            curr: Optional[Node] = q.popleft()
            for nbr in curr.neighbors:
                if nbr not in mapper:
                    mapper[nbr] = Node(nbr.val)
                    q.append(nbr)  # found new node, go through its neighbors

                # if nbr exists then simply add their Node() to the array
                mapper[curr].neighbors.append(mapper[nbr])
                # traverse through neighbors of new node and append mapper[nbr] which is the new node

        return mapper[node]


# The important issue might come in tracking the neighbor node as it may come before and we may have to adjust it's neighbours then on iteration
# for this we need to store this nbr

sol = Solution()
adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]

createGraph(adjList)

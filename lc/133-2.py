from collections import deque
from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        mapper = {}
        mapper[node] = Node(node.val)
        q = deque()
        q.append(node)

        while len(q):
            curr: Node = q.popleft()
            for nbr in curr.neighbors:
                if nbr not in mapper:
                    mapper[nbr] = Node(nbr.val)
                    q.append(nbr)
                mapper[curr].neighbors.append(mapper[nbr])

        return mapper[node]


sol = Solution()

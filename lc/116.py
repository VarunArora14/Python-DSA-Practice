from collections import deque
from typing import Optional


class Node:
    def __init__(self, val: int = 0, left: "Node" = None, right: "Node" = None, next: "Node" = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return root

        q = deque()
        q.append(root)
        while len(q):
            tmp = deque()
            for _ in range(len(q)):
                top = q.popleft()
                if top.left:
                    tmp.append(top.left)

                if top.right:
                    tmp.append(top.right)

            print([t.val for t in tmp])
            for i in range(len(tmp) - 1):
                tmp[i].next = tmp[i + 1]

            q = tmp

        return root


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.left = Node(6)
r.right.right = Node(7)

sol = Solution()
sol.connect(r)

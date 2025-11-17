from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res = []

        q = deque([])
        q.append(root)

        while len(q):
            rightval = -1
            q_size = len(q)
            for _ in range(q_size):
                curr: TreeNode = q.popleft()
                rightval = curr.val
                if curr.left:
                    q.append(curr.left)

                if curr.right:
                    q.append(curr.right)
            res.append(rightval)
        return res


sol = Solution()

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(5)
root.right.right = TreeNode(4)

print(sol.rightSideView(root))

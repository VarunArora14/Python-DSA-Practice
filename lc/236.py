# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __str__(self):
        return str(self.val)

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.path1 = []
        self.path2 = []

    def helper(self, root: Optional[TreeNode], node_val: int, path: list[int]):
        if root is None:
            return False

        if root.val == node_val:
            path.append(root)
            return True

        left = self.helper(root.left, node_val, path)
        right = self.helper(root.right, node_val, path)

        if left or right:
            path.append(root)
            return True
        return False

    def lowestCommonAncestor(self, root: "TreeNode", p: "TreeNode", q: "TreeNode") -> "TreeNode":
        self.helper(root=root, node_val=p.val, path=self.path1)
        self.helper(root=root, node_val=q.val, path=self.path2)

        self.path1 = [x for x in self.path1[::-1]]
        self.path2 = [x for x in self.path2[::-1]]

        i = 0

        while i < len(self.path1) and i < len(self.path2):
            if self.path1[i].val == self.path2[i].val:
                i += 1
            else:
                break

        return self.path1[i - 1]


sol = Solution()
root = TreeNode(3)
root.left = TreeNode(5)
root.right = TreeNode(1)
root.left.left = TreeNode(6)
root.left.right = TreeNode(2)
root.right.left = TreeNode(0)
root.right.right = TreeNode(8)
root.left.right.left = TreeNode(7)
root.left.right.right = TreeNode(4)

print(sol.lowestCommonAncestor(root, root.left, root.right))

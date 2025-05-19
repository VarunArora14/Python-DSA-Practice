# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def helper(self, root: TreeNode):
        if root is None:
            return 0

        return max(self.helper(root.left), self.helper(root.right)) + 1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.helper(root)

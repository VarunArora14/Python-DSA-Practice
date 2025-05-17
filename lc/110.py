from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.flag = True

    def helper(self, root: Optional[TreeNode]):
        if root is None:
            return 0

        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1

        if abs(left - right) > 1:
            self.flag = False

        return max(left, right)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.flag


sol = Solution()
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.right = TreeNode(3)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.left.left.right = TreeNode(4)
print(sol.isBalanced(root))

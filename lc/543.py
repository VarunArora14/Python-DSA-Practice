# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.max_dist = 0

    def helper(self, root: Optional[TreeNode]):
        if root is None:
            return 0

        left = self.helper(root.left)
        right = self.helper(root.right)

        self.max_dist = max(self.max_dist, left + right)  # stores the max diameter found yet

        # return the height of subtree for parent calculation of it's subtrees and their diameters7
        # +1 is the edge between the subtree and parent
        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.helper(root)
        return self.max_dist


sol = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

"""
The idea is to go through each of the subtrees and then check of the height in left and right subtrees. It will go to the leaves first
and follow bottom up like approach.

We have the code to find the height of the subtrees and we use this for calculation. For a given node, we see the height of left subtree as result
shared by recursive method +1 for the edge with subtree node and current node.

Then we have a class variable max_dist calculating the diameter as self.max_dist = max(self.max_dist, left + right) that stores the sum of heights 
of left and right subtrees representing paths between them.
"""

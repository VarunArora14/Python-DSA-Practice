from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return root

        curr = root
        while curr:
            if curr.val == val:
                return curr
            elif curr.val > val:
                curr = curr.left
            else:
                curr = curr.right

        return curr


sol = Solution()

"""
In BST, if the value is same as Node => return the node, if smaller then go left, otherwise go right to the tree
"""

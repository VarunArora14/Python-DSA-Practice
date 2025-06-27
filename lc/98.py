# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorder(self, root: Optional[TreeNode], inorder_list: List[int]):
        if root is None:
            return

        # LNR flow

        if root.left:
            self.inorder(root.left, inorder_list)

        inorder_list.append(root.val)

        if root.right:
            self.inorder(root.right, inorder_list)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        inorder_data = []
        self.inorder(root, inorder_data)

        for i in range(len(inorder_data) - 1):
            if inorder_data[i] >= inorder_data[i + 1]:
                return False
        return True


sol = Solution()
"""
For a tree to be BST, for each subtree, the left nodes must be smaller than root and right nodes always bigger than root.
Now, since we have to see recursively for each substree, we can rather think of traversals to see if they can help.

The preorder traversal works in LRN format, which means it goes right before going to node, but since node is smaller than right tree, ordering will be
a problem. For inorder traversal we have LNR - left -> node -> right 

This is good as we can have things in sorted manner with this traversal if the binary tree is BST
"""

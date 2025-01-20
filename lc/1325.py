from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
    
def isLeaf(node:TreeNode):
    if node.left is None and node.right is None:
        return True
    return False

def deleteLeavesWithTarget(root:TreeNode, target:int):
    if root is None:
        return root
    
    root.left = deleteLeavesWithTarget(root.left, target)
    root.right = deleteLeavesWithTarget(root.right, target)
    
    if root.left is None and root.right is None and root.val == target:
        return None

    return root # base case
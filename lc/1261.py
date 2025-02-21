from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:
    def __init__(self, root: Optional[TreeNode]):
        def traverse(root: TreeNode):
            if root is None:
                return
            if root.left:
                root.left.val = 2 * root.val + 1
                self.ele_set.add(root.left.val)
            if root.right:
                root.right.val = 2 * root.val + 2
                self.ele_set.add(root.right.val)

            traverse(root.left)
            traverse(root.right)

        def traverse_optimized(root: TreeNode, root_val: int):
            if root is None:
                return
            if root.left:
                self.ele_set.add(2 * root_val + 1)

            if root.right:
                self.ele_set.add(2 * root_val + 2)

            traverse_optimized(root=root.left, root_val=2 * root_val + 1)
            traverse_optimized(root=root.right, root_val=2 * root_val + 2)

        self.ele_set = set()
        if root is None:
            return

        self.ele_set.add(0)  # root
        # root.val = 0
        # temp = root
        # traverse(root)
        traverse_optimized(root_val=0, root=root)
        print(self.ele_set)

    def find(self, target: int) -> bool:
        return target in self.ele_set


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)

t = TreeNode(-1)
t.left = TreeNode(-1)
t.left.left = TreeNode(-1)
t.left.right = TreeNode(-1)
t.right = TreeNode(-1)

s = FindElements(t)
print(s.find(2))
print(s.find(3))
print(s.find(5))

"""
Here I have a binary tree as input with all nodes as -1 at start and I want to convert it to proper tree where I can check whether a value exists in this tree.
For this, I use set where if root is None then I keep with empty set, otherwise begin the root value as 0 (important to set this for other operations to perform)
Then we prepare the tree by updating the values of the left and right children nodes as well as saving these in a set (to make find() operation O(1) time complexity)

Optimisation to add: Instead of preparing the tree, we can simply pass the parent value to the method as that's the reason we maintained a tree in the first place. This can be useful for cases when we do not want to modify the tree
"""

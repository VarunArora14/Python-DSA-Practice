from collections import deque


class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

    def bft(self, root):
        q = deque()
        q.append(root)
        print(type(q))
        res = []
        while len(q):
            temp = []
            minval = float("-inf")
            for _ in range(len(q)):
                top: TreeNode = q.popleft()
                minval = max(minval, top.val)
                print(top.val, " ")

                if top.left != None:
                    temp.append(top.left)

                if top.right != None:
                    temp.append(top.right)

            # after the for loop
            for t in temp:
                q.append(t)
            res.append(minval)
            print()


root = TreeNode(10)
root.left = TreeNode(3)
root.left.left = TreeNode(1)
root.right = TreeNode(12)
root.right.left = TreeNode(11)
root.right.right = TreeNode(13)
root.bft(root=root)


# Improvise with coleections->deque

class TreeNode:
    def __init__(self, val) -> None:
        self.val = val
        self.left = None
        self.right = None

    def bfs(self, root):
        if root is None:
            return

        q = []
        q.append(root)

        while len(q):
            for _ in q:
                top: TreeNode = q[0]
                print(top.val)
                q = q[1:]

                if top.left is not None:
                    q.append(top.left)
                if top.right is not None:
                    q.append(top.right)
            print()

    def averageSubtree(self, root) -> int:
        count = 0
        arr = []
        self.postOrder(root, 0, arr)
        print(arr)
        return len(arr)

    def postOrder(self, root, count: int, arr: list) -> (int, int):
        if root is None:
            return 0, 0

        lsum, lcount = self.postOrder(root.left, count, arr)
        rsum, rcount = self.postOrder(root.right, count, arr)

        subtreeSum = lsum + rsum
        subtreeNodeCount = lcount + rcount
        count += 1

        if root.val == (subtreeSum + root.val) // (subtreeNodeCount + 1):  # floor
            arr.append(root.val)

        return (subtreeSum + root.val, subtreeNodeCount + 1)


t = TreeNode(4)
t.left = TreeNode(8)
t.right = TreeNode(5)
t.left.right = TreeNode(1)
t.right.right = TreeNode(6)
t.left.left = TreeNode(0)
# t.bfs(t)
t.averageSubtree(t)

# convert bst to greater search tree
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/

class Node:
    def __init__(self, value:int) -> None:
        self.left = None
        self.right = None
        self.val = value

def createTree():
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(1)
    # root.left.right = Node(2) # makes it non-bst
    root.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(8)
    
    return root

def bstToGst(self, root: Node):
    '''
    Approach - 

    Do inorder traversal and store the nodes in an array
    Reverse traverse the array with curr_sum=0 at start and at each node perform - 
        root.val = root.val + curr_sum
        curr_sum = root.val
    By this way, you will change the values of each nodes
    '''

    arr = []
    def inorder(root):
        if root is None:
            return
        
        inorder(root.left)
        arr.append(root.val)
        inorder(root.right)
    
    curr_sum=0
    for i in range(len(arr),-1,-1):
        node = arr[i]
        node.val = node.val + curr_sum
        curr_sum = node.val
    
    return root
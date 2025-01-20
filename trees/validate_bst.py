class Node:
    def __init__(self, value:int) -> None:
        self.left = None
        self.right = None
        self.value = value

def createTree():
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(1)
    # root.left.right = Node(2) # makes it non-bst
    root.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(8)
    
    return root


def isValidBST( root: Node | None) -> bool:
    '''
    here we use the logic that inorder traversal of a BST is in increasing order as we follow LNR pattern
    '''

    def inorder(root, arr):
        if root is None:
            return
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)
    
    arr = []
    inorder(root, arr)

    for i in range(len(arr)-1):
        if arr[i]>=arr[i+1]:
            return False
    
    return True

def isValidBSTRecurse( root: Node | None):
    '''
    this initialises solve() with min_inf and max_inf as limits and then for each node we check if limits are being violated or not
    '''
    def solve(root: Node | None, llimit, rlimit):
        if root is None:
            return True

        if root.value >=rlimit or root.value <=llimit:
            return False
        
        return solve(root.left, llimit, root.value) and solve(root.right, root.value, rlimit)
    
    return solve(root, -float('inf'), float('inf'))
    

r = createTree()
print(isValidBSTRecurse(r))
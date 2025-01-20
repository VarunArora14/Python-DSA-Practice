class Node:
    def __init__(self, value:int) -> None:
        self.left = None
        self.right = None
        self.value = value



def inorderTraversal(root:Node, arr:list[int]):
    '''
    as arrays are immutable, we get the correct order of nodes in form of array
    '''
    if root is None:
        return []
    
    if root.left:
        inorderTraversal(root.left, arr)
    arr.append(root.value)
    if root.right:
        inorderTraversal(root.right, arr)
    
    return arr

def preorderTraversal(root:Node, arr:list[int]):
    if root is None:
        return

    arr.append(root.value)
    print(root.value)
    if root.left:
        preorderTraversal(root.left, arr)
    if root.right:
        preorderTraversal(root.right, arr)
    
    return arr

def postorderTraversal(root:Node,arr:list[int]):
    if root is None:
        return []

    if root.left:
        postorderTraversal(root.left, arr)
    if root.right:
        postorderTraversal(root.right, arr)
    arr.append(root.value)
    
    return arr

def createTree():
    root = Node(4)
    root.left = Node(3)
    root.left.left = Node(1)
    root.right = Node(6)
    root.right.left = Node(5)
    root.right.right = Node(8)
    
    return root


def breadthTraversal(root:Node):
    q = []
    if root is None:
        return []

    res = [[root.value]]
    q.append(root)
    
    while len(q):
        temp = []
        for i in range(len(q)):
            node = q[i]
            
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)        
        q = temp
        vals = [node.value for node in temp]
        print(vals)
        if vals!=[]:
            res.append(vals) 
    
    for i in range(len(res)):
        print(f"level {i}: {res[i]}")
        


root:Node = createTree()    
arr = []
print("preorder: ",preorderTraversal(root, []))
arr = []
print("inorder: ",inorderTraversal(root, []))
arr = []
print("postorder: ",postorderTraversal(root, []))

breadthTraversal(root)
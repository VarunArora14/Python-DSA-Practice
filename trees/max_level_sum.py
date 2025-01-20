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

def max_level_sum(root:Node):
    
    q = []
    q.append(root)
    level=1
    max_sum = root.value
    max_level = level
    while len(q):
        temp = []
        for i in range(len(q)):
            print(i)
            node = q[i]
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)

        # it considers level n+1 with sum 0 which is unnecessary
        if temp == []:
            break
        q = temp
        level+=1
        curr_sum = sum([x.value for x in temp])
        # arr = [x.value for x in temp]
        
        if max_sum < curr_sum:
            max_sum = curr_sum
            max_level = level
    
    print(max_level, max_sum)

root = createTree()
max_level_sum(root)
            

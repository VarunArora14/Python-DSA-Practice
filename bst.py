class Node:
  def __init__(self, value) -> None:
    self.left = None
    self.right = None
    self.value = value


# node with given value has to be inserted in the bst
def insert(root: Node, value: int):
  # base case and leaf node
  if root is None:
    return Node(value)

  if root.value < value:
    root.right = insert(root.right, value)

  elif root.value > value:
    root.left = insert(root.left, value)

  return root  # unchanged root node so that returned node is same as it was with it's child nodes changed


def findSmallestElement(root: Node):
  curr = root
  if curr is None:
    print("empty element")
    return

  while curr.left is not None:
    curr = curr.left

  return curr.value
	
def findSmallestNode(root:Node):
  curr = root
  while(curr.left):
    curr = curr.left
  
  return curr

def findLargestElement(root: Node):
  curr=root
  if curr is None:
    print("empty element")
    return

  while curr.right:
    curr = curr.right

  return curr.value


def delete(root: Node, value: int):
  # 3 cases exist - leaf node, single child node, two child node
  if root is None:
    return None
  
  if value < root.value:
    root.left = delete(root.left, value)

  elif value > root.value:
    root.right = delete(root.right, value)

  # First case: delete the leaf node

    # single child node

    # return the right child to the parent and set node's child as empty
  if root.left is None and root.right is not None:
     return root.right
  # return the left child to the parent and set node's child as empty
  elif root.right is None and root.left is not None:
    return root.left
    
  else:
    # find the smallest node in right subtree, replace it's value with root, delete the node
    smallestNodeInRightSubtree = findSmallestNode(root.right)
    root.value = smallestNodeInRightSubtree.value
    root.right = delete(root.right, smallestNodeInRightSubtree.value) # go to the right subtree and delete the item we found
    
  return root


# return the node which has the same value
def search(root: Node, value: int):
  if root is None or root.value == value:
    return root

  if root.value < value:
    search(root.right, value)

  # check left subtree
  search(root.left, value)

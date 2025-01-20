class Node:
  def __init__(self,val) -> None:
  self.left=None
  self.right=None
  self.val=val
  
  
def inorder(root:Node):
  
  if not root:
  return
  
  inorder(root.left)
  print(root.val)
  inorder(root.right)
  
  
def isMirror(r1:Node, r2:Node):
  
  # base case for null
  if r1 is None and r2 is None:
  return True
  
  # check if subtrees are mirrors as well
  if (r1 is not None) and (r2 is not None):
  if r1.val == r2.val:
    # check if left and right matches, vice versa
    return isMirror(r1.left, r2.right) and isMirror(r1.right, r2.left)
  
  return False
    
def main():
  root = Node(0)
  root.left=Node(1)
  root.right=Node(1)
  root.left.left=Node(3)
  root.left.right=Node(4)
  root.right.left=Node(4)  
  root.right.right=Node(3)
  
  # inorder(root=root)
  
  print(isMirror(root,root))

main()

# conditions for symmetric tree - 
# 1. root's node key must be same
# 2. left subtree of r1 must be same as right subtree r2 at each node level
# 3. right subtree of r1 is same as left subtree of r2 at each node level
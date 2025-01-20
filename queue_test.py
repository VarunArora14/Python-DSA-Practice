from queue import Queue


class Node:
  def __init__(self, val):
    self.left = None
    self.right = None
    self.val = val


def levelOrderTraversal(root: Node):
  q = Queue()

  if not root:
    return []

  res = []

  q.put(root)

  while not q.empty():
    sz: int = q.qsize()
    temp = []
    for _ in range(sz):
      top: Node = q.get()  # removes the top element as well
      temp.append(top.val)

      if top.left:
        q.put(top.left)

      if top.right:
        q.put(top.right)

    res.append(temp)

  # we want first element of each array as the ans

  answer = []

  for arr in res:
    answer.append(arr[0])
  print("ans: ", answer)


def main():
  root = Node(1)
  root.left = Node(2)
  root.right = Node(3)
  root.left.left = Node(4)
  root.left.right = Node(5)
  root.right.left = Node(6)
  root.right.right = Node(7)
  root.left.left.left = Node(8)

  levelOrderTraversal(root=root)


main()

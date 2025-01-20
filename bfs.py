from collections import defaultdict
from queue import Queue


class Graph:
  def __init__(self) -> None:
    self.graph = defaultdict(list) # list is default value and we don't initialise via self.graph={}
    
  def print(self):
    for key in self.graph.keys():
      print(key, ": ", self.graph[key])
    
  def addEdge(self,u,v):
    if u not in self.graph.keys():
      self.graph[u]=[] # initialise key 'u' with empty value
        
    self.graph[u].append(v)

  def bfs(self, root):
    
    q = Queue()
    vis = set() # use array if nums 0 to n-1
    
    q.put(root) # first value to start the bfs
    vis.add(root)
    
    while q.qsize():
      
      for _ in range(q.qsize()):
        front = q.get()
        print(front)
        # q.pop(0) # remove the 0th element
        
        for nbr in self.graph[front]:
          if nbr not in vis:
            q.put(nbr)
            vis.add(nbr)
      print()

g = Graph()
g.addEdge(1,2)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,5)
g.addEdge(2,3)
g.addEdge(3,1)

g.bfs(root=1)
# g.print()

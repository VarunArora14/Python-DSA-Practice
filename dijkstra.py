import heapq

class Solution:
  def __init__(self,vertices) -> None:
    self.vertices=vertices
    self.adj = [[] for _ in range(vertices)] # O(n)
   
  def addEdge(self,u:int,v:int, wt:int):
    self.adj[u].append(v,wt)
    
  def dijkstra(self,start:int):
    q = heapq()
    dist = [float('inf') for _ in range(self.vertices)]
    heapq.heappush(q,(0,start))
    
    while len(q):
      d, u = heapq.heappop(q)
      for nbr, nbr_wt in self.adj[u]:
        if dist[nbr] > dist[u]+d:
          dist[nbr] = dist[u]+d
          heapq.heappush(q,(dist[u]+d,nbr))
  
  #  TODO: WIP

s=Solution(5)
s.printSol()
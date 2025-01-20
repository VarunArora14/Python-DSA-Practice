from queue import SimpleQueue
class Graph:
    def __init__(self, graph:list[list[int]],n:int) -> None:
        self.graph = graph
        self.n=n
        self.q=SimpleQueue()
        self.vis = [[False for _ in range(n)] for _ in range(n)] # n*n array of False
        self.dirs = [(0,1), (1,0), (-1,0), (0,-1)] # directions to traverse
        self.steps=0
    
    # go through all the elements of the island and mark them true storing their indices
    def floodFill(self, i:int, j:int):
        print(i,j)
        # find all the neighbours part of first island and append their indices
        if i<0 or j<0 or i>=self.n or j>=self.n or self.vis[i][j]==True or self.graph[i][j]==0:
            return
    
        self.q.put((i,j))
        print(f"qsize: {self.q.qsize()}")
        self.vis[i][j]=True
        
        # go in all 4 directions
        print("flood?")
        self.floodFill(i+1,j)
        self.floodFill(i-1,j)
        self.floodFill(i,j+1)
        self.floodFill(i,j-1)
        
        
        
    def findSolution(self)->int:
        flag=0
        for i in range(self.n):
            for j in range(self.n):
                if self.graph[i][j] == 1:
                    # do something
                    self.floodFill(i=i,j=j)
                    print("suuu")
                    flag=1
                    break
            if flag==1:
                break
        
        print(self.vis)
        print(self.graph)
        print(self.q.qsize())
        res = self.findShortestDistance()
        return res
    
    def findShortestDistance(self)->int:
        
        # bfs from all graph nodes(exclude the visited, inner nodes are marked as visited)
        while self.q.qsize():
            for _ in range(self.q.qsize()):
                print("heyyy")
                (i,j) = self.q.get() # get and pop the top element
                
                for x,y in self.dirs:
                    newx = i+x
                    newy = j+y
                    
                    # check if new indices valid
                    if newx<0 or newx>=self.n or newy<0 or newy>=self.n or self.vis[newx][newy]==True :
                        continue
                    
                    # found the destination island
                    if self.graph[newx][newy]==1:
                        return self.steps
                    
                    self.q.put((newx, newy))
                    self.vis[newx][newy]=True
                    
            self.steps+=1 # after each iteration of bfs
        
        return self.steps
                
        
    
graph = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
n = len(graph)
g=Graph(graph=graph, n=n)
print(g.findSolution())

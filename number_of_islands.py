from collections import deque

class Solution:
  def numIslands(self, grid:list[list[int]]):
    if not grid:
      return 0
    count=0
    vis=  [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))] # 2d array of 0s of row*col
     
    for i in range(len(grid)):
      for j in range(len(grid[0])):
        if grid[i][j]==1 and vis[i][j]==False:
          count+=1 # found an island
          self.search(i,j,grid, vis)
    return count
          

  def search(self, i,j,grid, vis):
    q = deque()
    q.append((i,j)) # use this to have tuples inside deque
      
    while len(q):
      # print(q.copy())
      row, col = q.popleft()
        
      if row>=0 and row<len(grid) and col>=0 and col<len(grid[0]) and grid[row][col]==1 and vis[row][col]==False:
        # extend is better way of calling append multiple times
        q.extend([(row-1,col), (row,col-1), (row+1,col), (row,col+1)])
        vis[row][col]=True


grid = [[1,0,0,0], 
        [0,0,1,0], 
        [1,1,0,0], 
        [0,1,0,1]]

s = Solution()
res = s.numIslands(grid=grid)
print(res)

# set with tuples in python
# sset = set()
# sset.add((1,2))
# if (1,2) in sset:
#   print("yooooo")
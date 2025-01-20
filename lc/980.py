from typing import List, Set
from ast import literal_eval

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        
        n = len(grid)
        m = len(grid[0])
        
        startx,starty=0,0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    startx=i
                    starty=j
        
        visited_paths = []
        vis = set()
        counter=0 
        vis.add((startx, starty))
        # we want to find unique paths meaning somewhere we better store the paths we have travelled\
            
        def dfs(currx:int, curry:int, vis:Set, grid:List[List[int]]):
            global counter
            dirs = [0,1,0,-1,0]
            if currx<0 or curry<0 or currx>=len(grid) or curry>=len(grid[0]) or (currx,curry) in vis:
                return
            
            if grid[currx][curry]==2:
                counter+=1
                return
            
            vis.add((currx, curry))
            for i in range(len(dirs)):
                vis.add((currx, curry))
                x=dirs[i]
                y=dirs[i+1]
                dfs(currx=currx+x, curry=curry+y, vis=vis, grid=grid)
            
            vis.remove((currx, curry)) # remove for backtracking
            return
        
        dfs(currx=startx, curry=starty, grid=grid, vis=vis)             
        print(counter)
        
s = Solution()
grid = literal_eval(input())
s.uniquePathsIII(grid=grid)
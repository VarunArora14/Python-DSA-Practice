# Given indices (sr,sc) representing the row, col to start floodfill and 2d array where arr[i][j] = 1 means can travel to and 0 means blockage
# Do floodfill to find shortest distance from sr,sc to all other points

def floodfill(row, col, graph, vis,color, initialColor):
    if row>= len(graph) or row<0 or col<0 or col>=len(graph[0]) or vis[row][col] or graph[row][col]!=initialColor:
        return
    
    vis[row][col]=True
    graph[row][col]=color
    
    floodfill(row+1, col, graph, vis,color, initialColor)
    floodfill(row-1, col, graph, vis,color, initialColor)
    floodfill(row, col+1, graph, vis,color, initialColor)
    floodfill(row, col-1, graph, vis,color, initialColor)

def main():
    
    arr = [
        [1,1,1],
        [1,1,0],
        [1,0,1]
    ]
    n=len(arr)
    m = len(arr[0])
    
    vis = [[False for _ in range(m)] for _ in range(n)] # 2d array of n*m
    
    sr,sc=1,1
    color =2
    initialColor = arr[sr][sc]
    floodfill(sr, sc, arr, vis, color, initialColor)
    print(arr)

main()
from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        if n == 1 and m == 1:
            return 0
        rows = [0 for _ in range(n)]
        cols = [0 for _ in range(m)]

        indices = []
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    rows[i] += 1
                    cols[j] += 1
                    indices.append((i, j))

        connected_servers_count = 0
        for i, j in indices:
            if rows[i] > 1 or cols[j] > 1:
                connected_servers_count += 1

        print(connected_servers_count)
        return connected_servers_count


grid = [[1, 1, 0, 0], [0, 0, 1, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
s = Solution()
s.countServers(grid=grid)

"""
Here we know that for each server in the grid, if we know that if any server in the same row or column exists then we know that server can communicate. So, we have to find
the count of ALL SERVERS THAT CAN COMMUNICATE. 

If s1 exists in first row and s2 exists in 8th row os same 0th column, then we know both s1 and s2 CAN CONNECT ANY SERVER.
Now, since we just need to know, WHETHER ANOTHER SERVER EXISTS IN SAME ROW/COLUMN, we can store the occurences of server in each row and column and then for
grid[r][c] having server 'sr', we check if row[r] or col[c] have count of server more than 1 (as 1 server is 'sr' itself) 

if rows[r]>1 or cols[c]>1:
    connected_server_count+=1
"""

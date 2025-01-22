from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        n = len(isWater)
        m = len(isWater[0])

        vis = set()
        q = []
        for i in range(n):
            for j in range(m):
                if isWater[i][j] == 1:
                    vis.add((i, j))
                    q.append((i, j))  # add as the first sources

        res = [[0 for _ in range(m)] for _ in range(n)]
        level = -1  # set to 0 for the water in first iteration
        dirs = [0, 1, 0, -1, 0]
        while len(q):
            level += 1
            temp = []

            for x in range(len(q)):
                r, c = q[x]  # row and column
                res[r][c] = level  # mark their height

                for d in range(len(dirs) - 1):
                    nrow, ncol = r + dirs[d], c + dirs[d + 1]

                    if (
                        nrow < 0
                        or nrow >= n
                        or ncol < 0
                        or ncol >= m
                        or (nrow, ncol) in vis
                    ):
                        continue
                    temp.append((nrow, ncol))
                    vis.add((nrow, ncol))
            q = temp  # get the layer of BFS
        # print(res)
        return res


isWater = [[0, 0, 1], [1, 0, 0], [0, 0, 0]]
s = Solution()
s.highestPeak(isWater=isWater)

"""
So at each index i,j where we have water, it is sure it will have value 0. Also, it's neighbouring elements have to be 1 to follow the condition - Two adjacent cells must
have height difference AT MOST 1. Now, we have to assign values such that height is maximized.

The thing to note is that adjacent elements of 1s which are not 0 can be either 1 or 2 only. Also, as we go away from cell 0, inorder to maxmize, the value of the cell
0,5 will be much higher than 0,1 where 0,0 is the land cell with value '0'.

Considering this, rather than finding largest value cells and then checking values of matrix that could fit with existing '0' value cells, we do multi-source BFS from all '0'
valued cells KEEPING TRACK OF SEEN CELLS as because we use BFS, the cell found via any '0' element will have the shortest path to the element '0'.

Also, we keep variable level/value initially set at 1 which sets values of all land cells via multi-source BFS and does LEVEL+=1 for next iteration to MAXIMIZE THE ANSWER for
cell 

"""

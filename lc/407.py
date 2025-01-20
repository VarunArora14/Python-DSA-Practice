from typing import List
import heapq
import copy


class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        q = []
        n = len(heightMap)
        m = len(heightMap[0])
        print(n, m)

        vis = set()  # store the index of elements visited

        for i in range(n):
            for j in range(m):
                if i == 0 or i == n - 1 or j == 0 or j == m - 1:
                    heapq.heappush(q, (heightMap[i][j], i, j))
                    vis.add((i, j))
        print(q)
        dirs = [0, 1, 0, -1, 0]
        new_hmap = copy.deepcopy(heightMap)

        max_h = -1  # maintain a max height
        # boundaries have been added
        while len(q):
            top_ele, trow, tcol = heapq.heappop(q)  # pick the smallest element

            max_h = max(
                max_h, top_ele
            )  # store the max height and use it to set to smaller neighbours, important to update as we go from smaller to larger elements
            new_hmap[trow][tcol] = max_h  # update here with the max value

            for d in range(len(dirs) - 1):
                nrow = trow + dirs[d]
                ncol = tcol + dirs[d + 1]
                if nrow < 0 or ncol < 0 or nrow >= n - 1 or ncol >= m - 1:
                    continue
                if (nrow, ncol) not in vis:
                    vis.add((nrow, ncol))
                    heapq.heappush(q, (new_hmap[nrow][ncol], nrow, ncol))

        counter = 0
        for i in range(n):
            for j in range(m):
                if new_hmap[i][j] != heightMap[i][j]:
                    print(new_hmap[i][j], heightMap[i][j], i, j)
                counter += new_hmap[i][j] - heightMap[i][j]
        # print("new_hmap:", new_hmap)
        # print("heightmap:", heightMap)
        print(counter)
        return counter


s = Solution()
hmap = [[1, 4, 3, 1, 3, 2], [3, 2, 1, 3, 2, 4], [2, 3, 3, 2, 3, 1]]
hmap = [
    [12, 13, 1, 12],
    [13, 4, 13, 12],
    [13, 8, 10, 12],
    [12, 13, 12, 12],
    [13, 13, 13, 13],
]
s.trapRainWater(heightMap=hmap)

"""
This problem has a trick. Instead of covering from the boundaries layer by layer which introduces problem in case below - 

Input:
[
    [12, 13, 1, 12],
    [13, 4, 13, 12],
    [13, 8, 10, 12],
    [12, 13, 12, 12],
    [13, 13, 13, 13],
]

Result:
[
    [12, 13, 1, 12],
    [13, 13, 13, 12],
    [13, 13, 12, 12],
    [12, 13, 12, 12],
    [13, 13, 13, 13],
]

This is wrong as 3rd row 2nd and 3rd column should be rather 12 as water will flow of those columns

The better way to solve this is to NOT go LAYER BY LAYER but start from outside taking the smallest value and then go to 4 directions and add nodes to heap which
are non-visited to this min heap. By this, you will be going to the smallest element each time and update it with the max_height variable OR do res+=max_height-h[i][j]

By creating another Data structure it is easier to visualise the answer and use the res for better memory management.

Now, since we start from the SMALLEST VALUE BOUNDARY, it is not possible that we go to a smaller element which shares even smaller boundary leading to miscalculation. To the new elements
found as neighbours, this max height is the height it will have water till top of. Try creating diagrams to find otherwise.

The trick is maintain a max height and to start from the smallest boundary and keep maintaining min heap of neighbours where you set their value to max height.
As you go to new node, do `max_height = max(max_height,h)` so we increase this height for inner elements.

Think of starting from the lowest boundary and then going to fill other places where you maintain a variable max_height which is the largest height of smallest elements of max heap
till now where all other non-visited elements cannot have height/water height below this value!
"""

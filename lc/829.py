from typing import List, Set


class Solution:
    def __init__(self) -> None:
        self.max_size = -1

    def dfs(self, vis: Set, grid: List[List[int]], row: int, col: int, idx: int, islandSizes: List[List[int]]) -> int:
        if (row, col) in vis or row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
            return 0

        vis.add((row, col))
        islandSizes[row][col] = idx

        size = 1

        # Explore neighbors using DFS
        size += self.dfs(vis, grid, row + 1, col, idx, islandSizes)
        size += self.dfs(vis, grid, row - 1, col, idx, islandSizes)
        size += self.dfs(vis, grid, row, col + 1, idx, islandSizes)
        size += self.dfs(vis, grid, row, col - 1, idx, islandSizes)

        return size

    def largestIsland(self, grid: List[List[int]]) -> int:
        idx = 2
        vis = set()

        # Now we go through all 0's and find if
        islandSizes = [[0 for _ in range(len(grid))] for _ in range(len(grid))]
        island_size_mapper = {}
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in vis:
                    # fill the component with idx
                    islandSizes[i][j] = idx
                    sz = self.dfs(vis=vis, grid=grid, row=i, col=j, idx=idx, islandSizes=islandSizes)
                    self.max_size = max(sz, self.max_size)  # max w/o 0s
                    island_size_mapper[idx] = sz
                    idx += 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    # go through neighbors
                    island_idx_set = set()  # unique island idx  values
                    if i - 1 >= 0:
                        island_idx_set.add(islandSizes[i - 1][j])
                    if j - 1 >= 0:
                        island_idx_set.add(islandSizes[i][j - 1])
                    if i + 1 < len(grid):
                        island_idx_set.add(islandSizes[i + 1][j])
                    if j + 1 < len(grid[0]):
                        island_idx_set.add(islandSizes[i][j + 1])

                    count = 1
                    for island_idx in island_idx_set:
                        count += island_size_mapper.get(island_idx, 0)

                    self.max_size = max(self.max_size, count)

        return self.max_size


sol = Solution()

grid = [[1, 1], [1, 0]]

print(sol.largestIsland(grid))

"""
LeetCode 827: Making A Large Island

Problem: Given a binary grid, we can change at most one 0 to 1. Return the size of the largest island after the change.

Solution Approach:
We got TLE when we tried changing each 0->1 and then doing floodfill, so we use a more efficient approach:

1. **Island Discovery Phase**: 
   - Use DFS to find all existing islands in the grid
   - Assign each island a unique identifier (starting from idx=2)
   - Store the size of each island in island_size_mapper
   - Track the maximum island size found so far

2. **Optimization Phase**:
   - For each 0 cell, check its 4 neighbors
   - Collect unique island identifiers from neighboring cells
   - Calculate potential new island size by summing:
     - 1 (for converting the 0 to 1)
     - Sizes of all unique neighboring islands
   - Update maximum size if this combination is larger

Key Optimizations:
- Mark each island cell with its island identifier to avoid recalculating sizes
- Use a set to ensure we don't double-count islands when a 0 has multiple neighbors from the same island
- Pre-compute all island sizes to make the second phase O(1) lookups

Time Complexity: O(N²) where N is the grid dimension
Space Complexity: O(N²) for the visited set and island tracking structures
"""

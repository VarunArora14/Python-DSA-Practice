from typing import List, Set


class Solution:
    def flood_fill(self, grid: List[List[int]], vis: Set, row: int, col: int, curr_sum: int):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or (row, col) in vis or grid[row][col] == 0:
            return curr_sum

        # vis.add((row, col))

        curr_sum += grid[row][col]
        # print(row, col)
        grid[row][col] = 0

        curr_sum = self.flood_fill(
            grid=grid, vis=vis, row=row + 1, col=col, curr_sum=curr_sum
        )  # go in all directions and pass the current sum as well
        curr_sum = self.flood_fill(grid=grid, vis=vis, row=row - 1, col=col, curr_sum=curr_sum)
        curr_sum = self.flood_fill(grid=grid, vis=vis, row=row, col=col + 1, curr_sum=curr_sum)
        curr_sum = self.flood_fill(grid=grid, vis=vis, row=row, col=col - 1, curr_sum=curr_sum)

        return curr_sum

    def findMaxFish(self, grid: List[List[int]]) -> int:
        vis = set()
        max_sum = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0 and (i, j) not in vis:
                    max_sum = max(self.flood_fill(grid=grid, vis=vis, row=i, col=j, curr_sum=0), max_sum)

        return max_sum


grid = [[0, 2, 1, 0], [4, 0, 0, 3], [1, 0, 0, 4], [0, 3, 2, 0]]
s = Solution()
print(s.findMaxFish(grid=grid))


"""
Here the fisherman goes inside the water (grid[r][c]!=0) and then goes in all directions with water to maximise the fishes earned. He cannot go to land but stay in the water
in form of BFS traversal to cover all directions. We have to find such water place which provides the max value of traversal on floodfill while marking them as visited
"""

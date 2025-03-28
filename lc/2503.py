from typing import List


class Cell:
    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value


class Query:
    def __init__(self, index, value):
        self.index = index
        self.value = value


class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.size = [1] * n

    def find(self, node):
        if self.parent[node] < 0:
            return node
        return self.find(self.parent[node])

    def union(self, nodeA, nodeB):
        rootA = self.find(nodeA)
        rootB = self.find(nodeB)
        if rootA == rootB:
            return False

        if self.size[rootA] > self.size[rootB]:
            self.parent[rootB] = rootA
            self.size[rootA] += self.size[rootB]
        else:
            self.parent[rootA] = rootB
            self.size[rootB] += self.size[rootA]
        return True

    def get_size(self, node):
        return self.size[self.find(node)]


class Solution:
    ROW_DIRECTIONS = [0, 0, 1, -1]  # Right, Left, Down, Up
    COL_DIRECTIONS = [1, -1, 0, 0]  # Corresponding column moves

    def maxPoints(self, grid, queries):
        row_count, col_count = len(grid), len(grid[0])
        total_cells = row_count * col_count

        sorted_queries = [
            Query(i, val) for i, val in enumerate(queries)
        ]  # Store queries with their original indices to maintain result order
        sorted_queries.sort(key=lambda x: x.value)  # Sort queries in ascending order

        sorted_cells = [
            Cell(row, col, grid[row][col]) for row in range(row_count) for col in range(col_count)
        ]  # Store all grid cells and sort them by value
        sorted_cells.sort(key=lambda x: x.value)  # Sort cells by value

        uf = UnionFind(total_cells)
        result = [0] * len(queries)

        cell_index = 0
        for query in sorted_queries:  # Process queries in sorted order
            while (
                cell_index < total_cells and sorted_cells[cell_index].value < query.value
            ):  # Process cells whose values are smaller than the current query value
                row = sorted_cells[cell_index].row
                col = sorted_cells[cell_index].col
                cell_id = row * col_count + col  # Convert 2D position to 1D index

                for direction in range(
                    4
                ):  # Merge the current cell with its adjacent cells that have already been processed
                    new_row = row + Solution.ROW_DIRECTIONS[direction]
                    new_col = col + Solution.COL_DIRECTIONS[direction]
                    if 0 <= new_row < row_count and 0 <= new_col < col_count and grid[new_row][new_col] < query.value:
                        uf.union(cell_id, new_row * col_count + new_col)

                cell_index += 1

            result[query.index] = (
                uf.get_size(0) if query.value > grid[0][0] else 0
            )  # Get the size of the component containing the top-left cell (0,0)

        return result

    def bfs(self, grid, query_item, vis, i, j):
        n = len(grid)
        m = len(grid[0])

        if i < 0 or j < 0 or i >= n or j >= m or (i, j) in vis:
            return

        if grid[i][j] >= query_item:
            return
        vis.add((i, j))
        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        for x, y in dirs:
            self.bfs(grid=grid, i=i + x, j=j + y, query_item=query_item, vis=vis)

    def maxPointsTLE(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        res = []
        for q in queries:
            vis = set()
            self.bfs(grid=grid, query_item=q, i=0, j=0, vis=vis)
            res.append(len(vis))

        return res


grid = [[5, 2, 1], [1, 1, 2]]
queries = [3]
s = Solution()
print(s.maxPoints(grid=grid, queries=queries))

"""
For each queries[i], we start from grid[0][0] and do BFS for possible non-visited nodes if the nbr is less than queries[i]

Optimisation DSU - 

Instead of handling queries one by one, we can take a different approach where we process all grid cells first and answer queries afterward. This allows us to efficiently determine the number of reachable points for each query without having to traverse the grid multiple times.

To better understand this approach, let's reiterate our previous observation in a slightly different way. Think about what each query is asking. A query provides a threshold value and asks how many cells in the grid can be reached from the top-left corner (0,0), while ensuring that all visited cells have values strictly less than this threshold. Instead of iterating over the grid every time a query is given, we can reverse the problem: first process the grid in increasing order of cell values, then efficiently answer all queries using this precomputed information.

To do this, we first extract all the grid cells and sort them in ascending order based on their values. By processing these cells in this order, we can simulate how the reachable area grows as the threshold increases. We maintain a disjoint set union (Union-Find) data structure to dynamically merge connected components as we encounter new cells with increasing values.

As we iterate through the sorted grid cells, we add each cell to our Union-Find structure. Whenever we add a cell, we also check its four adjacent neighbors (up, down, left, and right). If a neighbor has already been processed, we merge the current cell with its neighboring cell in the Union-Find structure. This ensures that, at any given moment, all connected components represent regions of the grid where all cells have values strictly less than the current threshold.

At the same time, we also sort the queries in ascending order based on their values. As we process each query, we continue adding cells to our Union-Find structure until the current cell values reach or exceed the query threshold. Once we finish adding all the relevant cells for a query, we determine how many of these cells are reachable from (0,0). Since the Union-Find structure keeps track of the size of connected components, we can efficiently find the number of reachable cells by checking the size of the component that contains (0,0).

If the query value is greater than grid[0][0], then the number of reachable cells is simply the size of the connected component containing (0,0). Otherwise, no additional cells are reachable, and the answer for this query is 0.
"""

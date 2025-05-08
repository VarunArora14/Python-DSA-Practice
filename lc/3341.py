import heapq
from typing import List


class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        # since there are no negative times, I am thinking of poentially graph or DP solution as its about minimizing the time taken
        # we can go in any direction so BFS can work with visited set for cycle avoid

        q = []
        heapq.heappush(q, (0, 0, 0))

        vis = set()
        vis.add((0, 0))
        print("movetime lens:", len(moveTime), len(moveTime[0]))

        dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while len(q):
            curr_time, x, y = heapq.heappop(q)
            # print(curr_time, x, y)

            if x == len(moveTime) - 1 and y == len(moveTime[0]) - 1:
                return curr_time

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if nx < 0 or ny < 0 or nx >= len(moveTime) or ny >= len(moveTime[0]) or (nx, ny) in vis:
                    continue
                else:
                    # consider the current time and add set time = max(curr_time, nums[x][y]) + 1
                    new_time = max(curr_time, moveTime[nx][ny]) + 1
                    heapq.heappush(q, (new_time, nx, ny))
                    vis.add((nx, ny))

                    # if nx == len(moveTime) - 1 and ny == len(moveTime) - 1:
                    #     return new_time

        return -1


sol = Solution()
nums = [[0, 0, 0], [0, 0, 0]]
print(sol.minTimeToReach(moveTime=nums))

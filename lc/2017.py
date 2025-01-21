from typing import List


class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        # initially we assume we take the entire upper path for robot2. Now, the 0,0 and 1,n-1 will be set 0 as robot1 has gone through it
        first_row = sum(grid[0])
        last_row = 0
        ans = float("inf")

        # we do simulation where for each index i we see the bottom sum of left and top sum of right (as the top left and bottom right is 0 taken by robot1)
        # we then take max of this value and then minimize this value for different indices i of the 2d array
        # starts with 0th index
        for i in range(len(grid[0])):
            first_row -= grid[0][i]
            ans = min(ans, max(first_row, last_row))
            last_row += grid[1][i]
            # the reason it is done after is that this score has to be calculated after moving down operation done. At i=0, robo1 moves down and the last_row sum stays 0

        return ans


arr = [[2, 5, 4], [1, 5, 1]]
s = Solution()
print(s.gridGame(arr))


"""
First we have to maximise the first iteration going bottom and right positions only and set the values of the path to 0. We can store the previous elements array for each
element and check whether the left or the above column (if they exist)
The aim of this game is to minimize the profit made by ROBOT 2 and NOT TO MAXIMIZE ROBOT 1 PROFIT.

We have to put find such path for robot1 that path for robot2 is minimised.

Now, understand this. There are total possible n paths for robot1 where n = len(arr). When it traverses each of the path, it leaves some remaining bottom sum and top sum
remaining. For robot2, we have to minimise this possible path.

Better explanation - https://leetcode.com/problems/grid-game/solutions/1486340/c-java-python-robot1-minimize-topsum-and-bottomsum-of-robot-2-picture-explained

Why not maxmimize robot1?

Consider case - 

10 50 50 30
50 50 10 10

Here if we take the largest points route, then it becomes - 

00 00 00 00
50 50 10 00

which is still 110 points for robot2, but if we do - 

00 00 50 30
50 00 00 00

then it makes at max 80 only and nothing more than this is possible.
"""

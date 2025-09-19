from typing import List


class Solution:
    def brute_force(self, heights: List[int]) -> int:
        n = len(heights)
        heights = [0] + heights + [0]  # base case edges
        max_height = 0

        for i in range(1, n + 1):
            curr = heights[i]
            prev_smaller = i - 1
            while prev_smaller >= 0 and heights[prev_smaller] >= curr:
                prev_smaller -= 1

            next_smaller = i + 1
            while next_smaller < n + 2 and heights[next_smaller] >= curr:
                next_smaller += 1

            print(curr, next_smaller, prev_smaller, next_smaller - prev_smaller - 1)
            max_height = max(max_height, curr * (next_smaller - prev_smaller - 1))

        return max_height

    def optimised(self, heights: List[int]) -> int:
        n = len(heights)
        if n == 0:
            return 0
        prev_smaller_list = [0 for _ in range(n)]
        next_smaller_list = [0 for _ in range(n)]

        stack = []

        # first find NSE
        for i in range(n - 1, -1, -1):
            # if next ele bigger then pop
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            next_smaller_list[i] = n if stack == [] else stack[-1]
            stack.append(i)

        stack.clear()
        # find the previous smaller element list
        for i in range(n):
            # if prev ele bigger then pop
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            prev_smaller_list[i] = -1 if stack == [] else stack[-1]
            stack.append(i)

        print("prev list", prev_smaller_list)
        print("nexrt list", next_smaller_list)

        max_area = 0
        for i in range(n):
            curr_height_area = heights[i] * (next_smaller_list[i] - prev_smaller_list[i] - 1)
            max_area = max(max_area, curr_height_area)

        return max_area

    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.optimised(heights=heights)


sol = Solution()
heights = [2, 1, 5, 6, 2, 3]
print(sol.largestRectangleArea(heights))

"""

To find the largest area in histogram, we consider how this rectangle is calculated.

We take a rectangle where the area is width (dist between elements) X height (min height between nodes)

Now, this mi height is important and we could find the pattern that for heights[i] to be min height considered for any rectangle, we need to find the next smallest and next largest element from that node.

The largest area that can be made using height[i] can be found using this. If we do this for all heights, we can find the max area and this is the biggest hint.

Brute force: For each element, go to left and right subarray and then find the next smallest element index for width and use height[i] as height to calc the rectangle area
"""

from typing import List


class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        if len(arr) == 1:
            return 0  # pos of only element

        n = len(mat)
        m = len(mat[0])
        rows = [
            m for _ in range(n)
        ]  # store number of non-painted columns of that row (initially length of column)
        cols = [
            n for _ in range(m)
        ]  # store n initially which is number of non-painted items in the column(i.e. number of rows as value)

        mapper = {}  # store the mapping of value -> position
        for i in range(n):
            for j in range(m):
                mapper[mat[i][j]] = (i, j)

        for i in range(len(arr)):
            r, c = mapper[arr[i]]

            # for that row 'r' and col 'c' reduce one element as it is now markes as painted
            rows[r] -= 1
            cols[c] -= 1

            if rows[r] == 0 or cols[c] == 0:
                return i
        return -1  # failure?


arr = [2, 8, 7, 4, 1, 3, 5, 6, 9]
mat = [[3, 2, 5], [1, 4, 6], [8, 7, 9]]
s = Solution()
print(s.firstCompleteIndex(arr, mat))

"""

If any of the row or col fills up, return the idx of a. Now the main concern is to find a way and then an efficient way to check if any row is completely
filled or not. The items in array/matrix are NOT sorted.

Inefficient way is to check each row and column which will make this O((m*n)^2) where first m*n is for traversal of arr and then inner for check. We want to see if we can
do something of checking if in colored elements we find a row/col being completed.

We can have array of rows[] and cols[] where each of them store m,n as default values each of length n and m respectively and then for each element arr[i]
we get the index (r,c) from mapper[arr[i]] and then do row[r]-=1 and col[c]-=1. 
If the row[r] or col[c] becomes 0 then return index i

The trick in this question was to have an array rows[] and cols[] which for each row and column store the count of non-painted items which if reached to 0 should return the 
index of array i.

The initial approach of maintaining the frow, fcol, lrow and lcol doesn't make sense as it can be any row/col to fill up that should return the answer and not just the border ones
"""

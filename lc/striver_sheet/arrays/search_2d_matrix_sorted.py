import bisect
from typing import List


def bs(nums: List[int], target: int):
    print(nums, target)
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return True
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False


def solve(matrix: List[List[int]], target: int):
    n = len(matrix)
    m = len(matrix[0])
    if n == 0 or m == 0:
        return False

    # find the correct row
    pos = -1
    for i, row in enumerate(matrix):
        if row[0] <= target <= row[-1]:
            return bs(row, target)
            break

    return False


def optimized_solve(matrix: List[List[int]], target: int):
    n = len(matrix)
    m = len(matrix[0])

    start, end = 0, n * m - 1
    while start <= end:
        mid = (start + end) // 2
        row = mid // m
        col = mid % m
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            start = mid + 1
        else:
            end = mid - 1

    return False


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
target = 8

# matrix = [[1, 2, 4], [6, 7, 8], [9, 10, 34]]
# target = 78
print(optimized_solve(matrix, target))

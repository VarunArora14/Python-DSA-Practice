from typing import List


class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        if n == 0:
            return []

        groupStart = [0 for _ in range(n)]
        for i in range(1, n):
            if nums[i] - nums[i - 1] > maxDiff:
                groupStart[i] = i
            else:
                groupStart[i] = groupStart[i - 1]

        result = []
        for u, v in queries:
            if u == v:
                result.append(True)
            else:
                result.append(groupStart[u] == groupStart[v])

        return result


sol = Solution()
n = 4
nums = [2, 5, 6, 8]
maxDiff = 2
queries = [[0, 1], [0, 2], [1, 3], [2, 3]]
print(sol.pathExistenceQueries(n=n, nums=nums, maxDiff=maxDiff, queries=queries))

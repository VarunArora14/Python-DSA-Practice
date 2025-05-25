class Solution:
    def minCuttingCost(self, n: int, m: int, k: int) -> int:
        def helper(x):
            if x <= k:
                return 0
            lo = max(1, x - k)
            hi = min(k, x - 1)
            # Evaluate cost at both endpoints
            c1 = lo * (x - lo)
            c2 = hi * (x - hi)
            return min(c1, c2)

        return helper(n) + helper(m)


sol = Solution()
print(sol.minCuttingCost(4, 4, 6))

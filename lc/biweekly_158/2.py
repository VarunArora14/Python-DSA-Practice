from typing import List


class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        dp = [[float("-inf")] * 3 for _ in range(k + 1)]
        for t in range(k + 1):
            dp[t][0] = 0

        for p in prices:
            dp2 = [[dp[t][pos] for pos in range(3)] for t in range(k + 1)]

            for t in range(k + 1):
                dp2[t][1] = max(dp2[t][1], dp[t][0] - p)

                dp2[t][2] = max(dp2[t][2], dp[t][0] + p)

                if t < k:
                    dp2[t + 1][0] = max(dp2[t + 1][0], dp[t][1] + p)

                if t < k:
                    dp2[t + 1][0] = max(dp2[t + 1][0], dp[t][2] - p)

            dp = dp2
        return max(dp[t][0] for t in range(k + 1))


sol = Solution()
prices = [1, 7, 9, 8, 2]
k = 2

prices = [12, 16, 19, 19, 8, 1, 19, 13, 9]
k = 3
print(sol.maximumProfit(prices, k))

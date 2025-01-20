class Solution:
    def longestPalindromeLength(self, s: str) -> int:
        n = len(s)
        rev_s = s[::-1]

        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

        # set the first row and col as 0
        for i in range(n + 1):
            dp[i][0] = 0
            dp[0][i] = 0

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == rev_s[j - 1]:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        print(dp)


s = Solution()
s.longestPalindromeLength("baba")

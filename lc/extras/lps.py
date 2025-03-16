class Solution:
    def check_palindrome(self, substr):
        if len(substr) == 1:
            return True

        start, end = 0, len(substr) - 1
        while start < end:
            if substr[start] != substr[end]:
                return False
            start += 1
            end -= 1

        return True

    def longestPalindrome_dp(self, s: str) -> str:
        resIdx, resLen = 0, 0
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    if resLen < (j - i + 1):
                        resIdx = i
                        resLen = j - i + 1

        return s[resIdx : resIdx + resLen]

    def longestPalindrome(self, s: str) -> str:
        res = ""
        if len(s) == 1:
            return s

        # O n^2 time
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                substr = s[i:j]  # space created
                print(substr)
                if self.check_palindrome(substr) and len(res) < len(substr):
                    res = substr

        return res


s = Solution()
print(s.longestPalindrome_dp("ac"))

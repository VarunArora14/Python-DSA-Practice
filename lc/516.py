from functools import cache


class Solution:
    @cache
    def helper(self, i: int, j: int, string: str):
        if i > j:
            return 0

        if i == j:
            return 1

        if string[i] == string[j]:
            return 2 + self.helper(i + 1, j - 1, string)

        return max(self.helper(i + 1, j, string), self.helper(i, j - 1, string))

    def longestPalindromeSubseq(self, s: str) -> int:
        return self.helper(0, len(s) - 1, s)


sol = Solution()
print(sol.longestPalindromeSubseq("bbab"))

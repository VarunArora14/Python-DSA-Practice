class Solution:
    def __init__(self):
        self.maxlen = 0

    def helper(self, s: str, curr: str, idx: int, k: int, memo={}):
        if curr != "" and int(curr, 2) <= k and self.maxlen < len(curr):
            self.maxlen = len(curr)

        if idx < len(s):
            self.helper(s, curr=curr + s[idx], idx=idx + 1, k=k)
            self.helper(s, curr=curr, idx=idx + 1, k=k)

    def longestSubsequence(self, s: str, k: int) -> int:
        self.helper(s, "", 0, k)
        return self.maxlen


sol = Solution()

s = "001010101011010100010101101010010"
print(sol.longestSubsequence(s, 1))

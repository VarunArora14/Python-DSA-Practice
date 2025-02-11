class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while s.find(part) != -1:
            idx = s.find(part)
            if idx != -1:
                s = s[:idx] + s[idx + len(part) :]
                # print(s)
        return s


s = Solution()
# print(s.removeOccurrences(s="daabcbaabcbc", part="abc"))
print(s.removeOccurrences(s="axxxxyyyyb", part="xy"))

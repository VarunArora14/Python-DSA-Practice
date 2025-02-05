class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if "".join(sorted(s1)) != "".join(sorted(s2)):
            return False

        n = len(s1)
        diff_count = 0
        for i in range(n):
            if s1[i] != s2[i]:
                diff_count += 1
        return diff_count == 0 or diff_count == 2


s = Solution()
s1 = "bank"
s2 = "kanb"
print(s.areAlmostEqual(s1, s2))

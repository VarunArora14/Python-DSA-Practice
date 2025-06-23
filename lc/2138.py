from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []
        for i in range(0, len(s), k):
            substr = s[i : i + k]
            fill_ctr = k - len(substr)
            print(fill_ctr)
            substr += fill_ctr * fill
            res.append(substr)

        return res


sol = Solution()
print(sol.divideString("abcdefghi", 3, "x"))
print(sol.divideString("abcdefghij", 3, "x"))

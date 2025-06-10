from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        mapper = dict()
        for char in s:
            if char not in mapper:
                mapper[char] = 0
            mapper[char] += 1

        max_odd = -float("inf")
        min_even = float("inf")
        for v in mapper.values():
            if v % 2 != 0:
                max_odd = max(max_odd, v)
            else:
                min_even = min(min_even, v)

        return max_odd - min_even


sol = Solution()
print(sol.maxDifference("abcabcab"))
print(sol.maxDifference("aaaaabbc"))
print(sol.maxDifference("tzt"))

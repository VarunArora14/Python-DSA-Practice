from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        if len(words) == 0:
            return []

        res = [words[0]]
        for i in range(1, len(words)):
            if sorted(words[i]) != sorted(words[i - 1]):
                res.append(words[i])

        return res


words = ["abba", "baba", "bbaa", "cd", "cd"]
words = ["a", "b", "a"]
sol = Solution()
print(sol.removeAnagrams(words))

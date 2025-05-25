from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        odd_two_letter_word = False

        mapper = {}
        for w in words:
            if w not in mapper:
                mapper[w] = 0
            mapper[w] += 1

        res = 0
        for k, v in mapper.items():
            if k[::-1] == k:
                if v % 2 != 0:
                    odd_two_letter_word = True
                res += (v // 2) * 4
                print("res:", res)
            else:
                if k[::-1] in mapper:
                    val = min(mapper[k], mapper[k[::-1]])
                    res += val * 2

        if odd_two_letter_word:
            res += 2
        return res


sol = Solution()
words = ["cc", "ll", "xx"]
print(sol.longestPalindrome(words=words))

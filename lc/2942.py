from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        res = []
        for idx, word in enumerate(words):
            if x in word:
                res.append(idx)

        return res

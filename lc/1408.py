from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: len(x)) # do we need this? time = O(n*logn) where n = number of words

        res = []
        n=len(words)
        for i in range(n-1):
            for j in range(i+1, n):
                if words[i] in words[j]: 
                    res.append(words[i])
                    break
        return res
    
s=Solution()
s.stringMatching(["blue","green","bu"])
        
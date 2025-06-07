class Solution:
    def checkOccurence(self, needle, haystack, idx):
        rem_len = len(haystack) - idx
        if rem_len < len(needle):
            return False
        
        for i in range(len(needle)):
            if haystack[idx + i]!=needle[i]:
                return False
        return True
        
    def strStr(self, haystack: str, needle: str) -> int:
        idx=0
        n = len(haystack)
        while idx<n:
            if haystack[idx] == needle[0] and self.checkOccurence(needle, haystack, idx):
                return idx
            idx+=1
        
        return -1
                
                

sol = Solution()
needle = "leeto"
haystack = "leetcode"
print(sol.strStr(haystack, needle))
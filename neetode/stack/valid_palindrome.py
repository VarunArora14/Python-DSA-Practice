from ast import literal_eval

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        if len(s)<2:
            return True
        
        start,end = 0, len(s)-1
        while start<end:
            while start<end and  not s[start].isalnum():
                start+=1
            while start<end and not s[end].isalnum():
                end-=1
            if s[start]!=s[end]:
                print(start,end)
                return False
            start+=1
            end-=1
        
        return True


inp = input()
inp.lower()
s=Solution()
print(s.isPalindrome(inp))

"Was it a car or a cat I saw?".isalnum()
" ".isalnum()

s = "No lemon, no melon"
print(s[9], s[8])
class Solution:
    def helper(self, n):
        if n == 1:
            return "1"
        
        prev = self.helper(n - 1)
        i=0
        while i<len(n):
            curr = ""
            for idx in range(len(n)):
                

    def countAndSay(self, n: int) -> str:
        return self.helper(n)


s = Solution()
print(s.countAndSay(4))
# 1211

class Solution:
    def __init__(self):
        self.counter=0
    def numDecodings(self, s: str, memo={}) -> int:
        mapper = {}
        for i in range(1,27):
            mapper[chr(64+i)] = i
        
        def helper(string:str, idx:int=0):
            n = len(string)
            
            if idx>n:
                return
            # base case
            if idx == n:
                
                self.counter+=1
                
            # we don't need loop but 2 conditions each time
            # in case 
            if idx<n and string[idx] == '0':
                return
            
            if idx<n-1 and 1<=int(string[idx:idx+2])<=26:
                helper(string, idx+2)
            helper(string, idx+1)
        
        helper(s)
        return self.counter
    
s=Solution()
# print(s.numDecodings("11106"))
# print(s.numDecodings("226"))
# print(s.numDecodings("12"))
print(s.numDecodings("06"))
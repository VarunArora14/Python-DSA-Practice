# https://www.geeksforgeeks.org/minimum-steps-to-delete-a-string-after-repeated-deletion-of-palindrome-substrings/

# find the biggest palindromes and then delete it and then check remaining string

def checkPalindrome(s:str,start,end):
    i=start
    j=end
    while i<=j:
        if s[i]!=s[j]:
            return False
        i+=1
        j-=1
    print(s[start:end+1])
    return True

def helper(s:str, start:int, end:int)->int:
    if start==end:
        return 1
    
    res = end-start+1
    for i in range(start, end+1):
        for j in range(i+1, end+1):
            if s[i]==s[j]:
                print(f"i: {i}, j: {j}")
                if checkPalindrome(s=s, start=i, end=j):
                    temp_s = s[start:i] + s[j+1:end] # concat the remaining string
                    res = min(res, 1 + helper(s=temp_s, start=start, end=i-1))
    
    return res

s = "1234"
s = "1234"
s = "1234"
s = "2553432"

print(helper(s=s, start=0, end=len(s)-1))        

# time total O(n^4) where checkPalindrome is O(n) as for each checkPalindrome => a helper method would be called whose occurence is related to len(n) => n*n = n^2 and
# thne there are 2 loops anyways    
    
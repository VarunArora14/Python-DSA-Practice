def solution(s:str):
    
    n=  len(s)
    res=0
    for i in range(1,n):
        diff = abs(ord(s[i]) - ord(s[i-1]))
        res+=diff
    
    print(res)
    return res

solution('zaz')
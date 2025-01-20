def Solution(k:int):
    if k<=1:
        return k
    
    dp = [0 for _ in range(k+1)]
    dp[1]=1
    dp[2]=2
    for i in range(3,k+1):
        if i%2==0:
            dp[i] = 1+dp[i-1]
        else:
            dp[i] = dp[int(i/2)]+1
    
    print(dp)
    print(len(dp))
    return dp[k]

k = 80
print(Solution(k=k))
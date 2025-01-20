n=5

# consider n=2, we have 4 trees, out of which only 2 are BST, for i=2 we have left = solve(2-1) and right = solve(2-2) (solve(i-1) + solve(n-i))
# now for left and right values, we don't have to take sum, but multiply them as combinations and n=0 means empty tree which is valid as well
# since we want BST, for each i, we consider left tree as solve(i-1) and right as solve(n-i) respectively

def recurse(n):
    if n==0 or n==1:
        return 1
    
    total_trees=0
    for i in range(1, n+1):
        left = recurse(i-1)
        right = recurse(n-i) # it's values range from [0...n-1]
        total_trees += (left*right)
    
    # print(total_trees)
    return total_trees


# using memoization, we store the solution of sub-problems which we use as optimization to recursion
def memoization(n, memo = {}):
    memo[0]=1 # empty bst
    memo[1]=1 # single node bst
    
    def solve(n):
        if n in memo:
            return memo[n] # optimisation of recusion

        total_trees=0
        for i in range(1, n+1):
            left = solve(i-1)
            right = solve(n-i)
            total_trees+=(left*right)
        
        memo[n]=total_trees
        return memo[n]

    solve(n)
    print(memo)
    return memo[n]
            
 
def dp_solve(n):
    dp = [0 for _ in range(n+1)]
    dp[0]=1
    dp[1]=1
    
    # find solution for each i from 1 to n as solution to sub-problems 
    for i in range(2,n+1):
         for j in range(1,i+1):
             dp[i] = dp[i] + (dp[j-1]*dp[i-j]) # same as solve(i-1)*solve(n-i)
    
    print(dp)
    return dp[n]

            
print(dp_solve(17))
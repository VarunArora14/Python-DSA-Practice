# class Solution:
#   def minCostClimbingStairs(self, cost: list[int]) -> int:


# s= Solution()


cost =  [1,100,1,1,1,100,1,1,100,1]

# start from the end and find the optimal solution to the first element, bottom up approach
l = len(cost)
dp = [float('inf') for _ in range(l)]
dp[l-1] = cost[l-1]
dp[l-2] = cost[l-2]
for i in range(l-3,-1,-1):
  dp[i] = min(dp[i+1], dp[i+2]) + cost[i] # pay cost at current step as well

print(dp)
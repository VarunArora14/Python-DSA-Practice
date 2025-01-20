import math

cost = [2, 3, 4, 2]
time = [1, 1, 1, 1]

# we have to maximise the time spent by the paid painter and focus on free painter doing the workie


l = len(cost)

# time taken by paid painter equal walls painted by free painter

# find items with smallest cost/time and minimize the cost

# sort based on time/cost ratio
for i in range(0, l):
    for j in range(i + 1, l):
        if (time[i] / cost[i]) < (time[j] / cost[j]):
            time[i], time[j] = time[j], time[i]
            cost[i], cost[j] = cost[j], cost[i]
        elif cost[i] == cost[j] and time[i] < time[j]:  # make painter take more time
            time[i], time[j] = time[j], time[i]

print(f"total walls: {l}")
finalCost = 0
i = 0
while i < l:
    finalCost += cost[i]
    l -= time[i]
    print(finalCost)
    print(l)
    print()
    i += 1

print(f"final cost is {finalCost}")

# number of walls by free painter <= time to paint walls by paid painter


def optimized():
    l = len(time)
    dp = [float("inf") for _ in range(l + 1)]
    dp[0] = 0

    # go through each cost[i] and check if dp[j - time[i]-1] + cost[i] < dp[j]
    for c, t in zip(cost, time):
        for j in range(l, 0, -1):
            dp[j] = min(dp[j], dp[max(j - 1 - t, 0)] + c)
            # min of current cost, dp[j-1-t] where (j-1-t) >=0 and add the current cost to paint as well
    return dp[l]


# we need DP for this
# [42,8,28,35,21,13,21,35]
# [2,1,1,1,2,1,1,2]

# find the best solution to take minimum time to paint j walls

# with cost[i] we can paint time[i]+1 walls(time[i] by free painter and 1 for paid)
# dp[X]=Y is minimum cost to paint X walls is Y

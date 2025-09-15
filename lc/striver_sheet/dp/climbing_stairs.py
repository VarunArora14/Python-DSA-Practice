def helper(idx: int, n: int, memo=None):
    if memo is None:
        memo = {}
    if idx > n:
        return 0
    if idx == n:
        return 1

    if idx in memo:
        return memo[idx]

    one_step = helper(idx + 1, n)
    two_step = helper(idx + 2, n)
    memo[idx] = one_step + two_step
    return one_step + two_step


def dp(n: int):
    # base cases for no steps to take and 1 step
    if n == 0 or n == 1:
        return n

    dp = [0 for _ in range(n + 1)]
    dp[n] = 1
    dp[n - 1] = 1

    for i in range(n - 2, -1, -1):
        dp[i] = dp[i + 1] + dp[i + 2]

    return dp[0]  # as we start from 0th stair


def find_unique_paths(n: int):
    if n <= 0:
        return 0

    # return helper(0, n)
    return dp(n)


print(find_unique_paths(1))
print(find_unique_paths(0))
print(find_unique_paths(5))
print(find_unique_paths(3))
print(find_unique_paths(8))

"""
Given n stairs, find number of distinct ways to go from 0 to n

Now, if we are at nth stair, we can perform 0 actions.

If we are at n-1 then we can do single action => go +1 stair

If we are at n-2th stair then we have 2 options => go +2 stairs or go +1 stair and repeat till n reach

So base case we know is that we have to reach Nth stair. Now consider handling of 0th or negative stairs.

If we reach n-x<0 then simply return not possible for this path to be considered
"""

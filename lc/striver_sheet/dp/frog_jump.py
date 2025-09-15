from typing import List


def helper(idx: int, n: int, arr: List[int], memo=None):
    if memo is None:
        memo = {}

    if idx >= n:
        return float("inf")

    if idx == n - 1:
        return 0  # no cost last stair

    if idx in memo:
        return memo[idx]

    # cost for one step jump
    cost1 = abs(arr[idx] - arr[idx + 1]) + helper(idx + 1, n, arr, memo)

    # cost for two step jump (if possible)
    if idx + 2 < n:
        cost2 = abs(arr[idx] - arr[idx + 2]) + helper(idx + 2, n, arr, memo)
    else:
        cost2 = float("inf")

    memo[idx] = min(cost1, cost2)
    return memo[idx]


def frog_jump(n: int, arr: List[int]):
    memo = {}
    helper(0, n, arr, memo)
    return memo[0]


n = 4
arr = [10, 20, 30, 10]
print(frog_jump(n, arr))

"""
Here we have a frog who can jump 1 or 2 stairs but here we want to find min energy used by the frog where this energy is calculated by abs(height[i]-height[j]) where height[i] is height of ith stair.

This is DP as we have to minimize this height value for the frog (optimal solution) and it has branches/choices to be made at each step.

Also, the best choice made of n-xth step can be further used at previous steps for optimal answer
"""

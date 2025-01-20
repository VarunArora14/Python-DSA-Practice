memo = {}
memo[0] = 1


def factorial(n: int, memo: dict) -> int:
    if n in memo:
        return memo[n]

    memo[n] = n * factorial(n - 1, memo)
    return memo[n]
    # return n*factorial(n-1)


print(factorial(7, memo=memo))
print(factorial(8, memo=memo))
print(memo)
# Memoization - Similar to caching where to store the previous results and then keep calculating using the old correct answers
# with memoization, we can store the previous solutions so when we come to that subproblem later, we can use the solved answer instead of solving
# same subproblems again

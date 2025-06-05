def recurse(n: int, memo={}):
    # base cases

    if n == 0:
        return 0

    if n < 9:
        return 1

    if n in memo:
        return memo[n]

    digits = [int(char) for char in str(n)]

    min_val = float("inf")
    for d in digits:
        if d > 0:
            print(n - d)
            min_val = min(min_val, recurse(n - d))  # find the minimum value returned

    memo[n] = 1 + min_val
    return memo[n]


def solve(n: int):
    print(recurse(n))


n = int(input())
solve(n)

from functools import cache


@cache
def helper(i: int, j: int, string: str):
    if i > j:
        return 0
    if string[i] == string[j]:
        return 2 + helper(i + 1, j - 1, string)

    # check if we can find better solution by moving i+1 or j-1
    return max(helper(i + 1, j, string), helper(i, j - 1, string))


def solve(string: str):
    n = len(string)
    return helper(0, n - 1, string)


string = "bbbab"
print(solve(string))

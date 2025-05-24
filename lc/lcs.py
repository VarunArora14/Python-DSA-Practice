s1 = "AGGTAB"
s2 = "GXTXAYB"

# memo = {}


def helper(
    s1: str,
    s2: str,
    i: int,
    j: int,
    memo: dict,
):
    if i == len(s1) or j == len(s2):
        return 0
    if (i, j) in memo:
        return memo[(i, j)]

    res = -1
    if s1[i] == s2[j]:
        res = 1 + helper(s1, s2, i + 1, j + 1, memo)
    else:
        # this takes the previous indices solution to pass on till the end as we want longest subsequence
        res = max(helper(s1, s2, i + 1, j, memo), helper(s1, s2, i, j + 1, memo))

    memo[(i, j)] = res
    return memo[(i, j)]


def solve_lcs():
    s1 = "AGGTAB"
    s2 = "GXTXAYB"
    # print(memo)
    memo = {}

    # in a way we are returning memo[(0,0)]
    return helper(s1, s2, 0, 0, memo)


print(solve_lcs())

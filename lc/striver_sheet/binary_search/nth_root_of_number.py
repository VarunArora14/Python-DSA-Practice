def helper(n: int, m: int, mid: int):
    ans = 1
    for _ in range(n):
        ans = ans * mid

    return ans


def solve(n: int, m: int):
    if m < 0 or n < 0:
        return -1

    if m == 0 or m == 1:
        return m

    if n == 1:
        return m

    start, end = 1, m

    while start <= end:
        mid = (start + end) // 2
        power_val = pow(mid, n)
        if power_val == m:
            return mid
        elif power_val < m:
            start = mid + 1
        else:
            end = mid - 1

    return -1


n, m = 3, 27
print(solve(n, m))

n, m = 4, 69
print(solve(n, m))

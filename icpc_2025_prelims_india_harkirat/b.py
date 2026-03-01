def solve(n: int, d: int, arr: list[int]):
    print("array", arr)
    if len(arr) == 1:
        return "yes" if arr[0] <= d else "no"

    arr.sort()
    for i in range(len(arr) - 1):
        if abs(arr[i] - arr[i + 1]) > d:
            return "no"

    return "yes"


t = int(input())
for _ in range(t):
    [n, d] = input().split(" ")
    n = int(n)
    d = int(d)
    print(f"n: {n}, d: {d}")

    arr = input().split(" ")
    arr = [int(v) for v in arr]
    print(solve(n, d, arr))

# for odd len array, try removing each element and vall this solve method bcos of conditions that ai-an+1-i
# diff must be <=d so if we have an anomaly, we can remove it but first find it by removing each number
# and then checking if any of them works then return "yes"

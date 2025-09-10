from typing import List


def search_single_ele_sorted(arr: List[int]):
    # base case
    if len(arr) == 1:
        return arr[0]

    n = len(arr)

    # edge case
    if arr[0] != arr[1]:
        return arr[0]
    if arr[n - 1] != arr[n - 2]:
        return arr[n - 1]

    start, end = 0, n
    while start < end:
        mid = (start + end) // 2
        print(mid, arr[mid])
        if arr[mid] != arr[mid + 1] and arr[mid] != arr[mid - 1]:
            return arr[mid]

        if (mid % 2 == 0 and arr[mid] == arr[mid + 1]) or (mid % 2 == 1 and arr[mid] == arr[mid - 1]):
            # the ele is on right side if this order is
            start = mid + 1
        else:
            end = mid - 1

    return -1


arr = [1, 1, 3, 2, 2, 4, 4, 5, 5]
arr2 = [1, 1, 2, 2, 3, 4, 4, 5, 5]
arr3 = [1, 1, 2, 2, 4, 4, 3, 5, 5]

print(search_single_ele_sorted(arr))

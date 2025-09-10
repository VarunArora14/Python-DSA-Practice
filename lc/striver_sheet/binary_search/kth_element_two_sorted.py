from typing import List


def kth_element_two_Arr_sorted(l1: List[int], l2: List[int], k: int):
    i, j = 0, 0
    n, m = len(l1), len(l2)

    curr = -1
    while i < n and j < m and k > 0:
        if l1[i] <= l2[j]:
            curr = l1[i]
            i += 1
            k -= 1
        else:
            curr = l2[j]
            j += 1
            k -= 1

        # print("curr is ", curr)
        if k == 0:
            return curr

    # assuming 1 list was shorter, we traverse others
    # while i < n:
    #     i += 1
    #     k -= 1

    #     if k == 0:
    #         return l1[i - 1]
    if i < n:
        return l1[i + k - 1]  # arr2 is smaller so we come here and we know k<=n+m

    # while j < m:
    #     j += 1
    #     k -= 1

    #     if k == 0:
    #         return l2[j - 1]
    if j < m:
        return l2[j + k - 1]

    return -1


l1 = [2, 3, 6, 7, 9]
l2 = [1, 4, 5]
k = 6
print(kth_element_two_Arr_sorted(l1, l2, k))

"""
For 2 arrays sorted we have to return the kth element assuming these lists were combined in a sorted manner optimally. Avoid using extra space

As per constraints we know that 1<=k<n+m
"""

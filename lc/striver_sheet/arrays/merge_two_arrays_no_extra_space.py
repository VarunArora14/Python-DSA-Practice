def solve(n, m, arr1, arr2):
    i = n - 1
    j = 0
    while i >= 0 and j < m:
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]  # swap to put larger element in arr2
            i -= 1
            j += 1
        else:
            break

    # elements in arr2 are all bigger than arr1 but not sorted (changes sort of arr1 as well)
    arr1.sort()
    arr2.sort()
    print(arr1)
    print(arr2)


n = 4
arr1 = [-5, -2, 4, 5]
m = 3
arr2 = [-3, 1, 8]

solve(n, m, arr1, arr2)
"""
Here we have 2 sorted arrays where we want to make arr1 and arr2 sorted both such that arr1 contains first N sorted elements and arr2 contains next M sorted
elements considering both arrays of size N and M. Do it in-place.

Now, we can potentially think of creating extra array and then sorting it and then assigning arr1 = arr2[:n+1] and arr2 = arr3[n:] but that uses space

For without space, we need to find a way such that all larger elements come inside arr2 and all smaller inside arr1. For this we can traverse arr1
from end and arr2 from start (since both are in asending order sorted).
If we find arr1[i]>arr2[j] then we swap them and do i-=1 and j+=1. This will make sure the largest of arr1 is in arr2 if the smallest of arr2 or smaller
than their largest. Consider cases like - 

arr1 = [100,101,102,104]
arr2 = [1,2,3,4,5]

arr1 = [4,8,12,15,21]
arr2 = [7,8,30]

By comparing the last elements of arr1 with start if arr2, we make sure that only smaller elements of arr2 go in arr1 and as we do i-1 and j+1 for
arr1 and arr2, we go for next potential elements to replace.
Now, if arr2[j]>arr1[i] at a certain point, then this means that all elements arr2[j:] are now larger than all elements of arr1[:i] and so we break 
at this point.
"""

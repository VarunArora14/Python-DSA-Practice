arr = [3, 1, 2, 4] 

def customSort()


def PrintAllSubarrays(arr:list[int]):
    res = []
    n = len(arr)
    for i in range(n):
        for j in range(i+1,n+1):
            slice = arr[i:j]
            res.append(slice)
    
    res = sorted(res, key= lambda x: len(x))
    res2 = sorted(res,)
    print(res)

PrintAllSubarrays(arr=arr)
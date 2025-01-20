target=7
arr = [2,3,1,2,4,3]

# target  = 7
# arr = [1,1,1,1,1,1000]

# traverse this to find the SMALLEST SUB-ARRAY whose sum>=target

def findSmallestLengthSubarray(target:int, arr:list[int]):
    if arr ==[]:
        return 0
    
    resLen = 1e9+7
    i=0
    currSum=0
    for j in range(0, len(arr)):
        currSum+=arr[j]
        if currSum >= target:
            print(f"currSum: {currSum}, j: {j}, i: {i}")
            resLen = min(resLen, j-i+1)
            
            while j>=i and currSum - arr[i] >=target:
                currSum-=arr[i]
                print(currSum)
                i+=1
                resLen = min(resLen, j-i+1)
                print(f"currSum: {currSum}, j: {j}, i: {i}")
        
        # print(f"i: {i}, j: {j}, resLen: {resLen}")
    
    return resLen if resLen != 1e9+7 else 0

resLen = findSmallestLengthSubarray(target=target, arr=arr)
print(resLen)
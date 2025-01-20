nums = [10,9,2,5,3,7,101,18]

def Solution(nums:list[int]):
    n = len(nums)
    sequence_store = [1 for _ in range(n)]
    sequence_store[n-1]=1
    
    for i in range(n-1, -1, -1):
        maxSubsequence = 1
        for j in range(i, n):
            if nums[i] < nums[j]:
                maxSubsequence = max(maxSubsequence, 1 + sequence_store[j]) # max of current and jth element + subsequence for [i...n]
        sequence_store[i] = maxSubsequence
    
    print(sequence_store)
    
    res = 0
    for s in sequence_store:
        res = max(res, s)
    
    return res

Solution(nums=nums)
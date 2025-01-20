def maxProfitAssignment(self, difficulty, profit, worker):
    arr = []
    for i in range(len(difficulty)):
        arr.append((difficulty[i], profit[i]))
    arr = sorted(arr, key=lambda x: x[0])

    maxProfit, maxProfits = 0, []
    for _, gain in arr:
        maxProfit = max(maxProfit, gain)
        maxProfits.append(maxProfit)

    total = 0
    for person in worker:
        idx = self.uppperBsearch(arr, person) - 1
        if idx > -1:
            total += maxProfits[idx]

    return total

def uppperBsearch(self, arr, target):
    left = 0
    right = len(arr)
    while left < right:
        mid = (left + right)//2
        if target >= arr[mid][0]:
            left = mid + 1
        else:
            right = mid
    return right

# class Solution:
#     def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        
#         sortedJobs = sorted(zip(difficulty, profit), key = lambda x: x[0]) # smallest to largest difficulty
#         res=i=best=0
#         # resArr = []
        
#         # sort worker to go to max skill storing the best
#         for workerSkill in sorted(worker):
#             while i<len(sortedJobs) and workerSkill>=sortedJobs[i][0]:
#                 best=max(best, sortedJobs[i][1])
#                 i+=1
#             res+=best
#             # resArr.append(best)
        
#         # print(resArr)
#         return res
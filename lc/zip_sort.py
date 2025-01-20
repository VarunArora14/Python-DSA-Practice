from dataclasses import dataclass

@dataclass
class ProfitDifficulty:
    profit:int
    difficulty:int
# pdList: list[ProfitDifficulty] = []


difficulty = [2,4,6,8,10]
profit = [10,20,30,40,50]
worker = [4,5,6,7]

# difficulty = [1,2,3,4,5,4,5]
# profit = [1,2,3,4,5,10,3]

# worker will pick job with max profit and at most difficulty[i] <= worker[i]

sortedJobs = sorted(list(zip(difficulty, profit)), key = lambda x: x[0])
print(sorted(worker))
print(sortedJobs)

# print(sorted(zipped_list, key=lambda x: x[0]))
# now we traverse sorted worker list and traverse maintaining best profit
res = i = best = 0
resArr = []
for workerSkill in sorted(worker):
    while i < len(sortedJobs) and workerSkill >= sortedJobs[i][0]:
        best = max(sortedJobs[i][1], best) # max of profit
        i+=1 
    res+=best # add the max profit
    resArr.append(best)

print(resArr)



# for x,y in zipped_list:
#     pdList.append(ProfitDifficulty(profit=x, difficulty=y))
# print(pdList)


# def binary_search(arr:list[int], item:int)->int:
#     start=0
#     end = len(arr)-1
    
#     while start < end:
#         mid = int((end-start)/2 + start)
#         if arr[mid] == item:
#             return mid
#         elif arr[mid] > item:
#             end = mid-1
#         else:
#             start = mid+1
    
#     return -1

# here we have to find the FIRST NUMBER LARGER THAN ITEM instead of it's occurence
# def binary_search_max_occurence(arr:list[int], item:int)->int:
#     start=0
#     end = len(arr)-1
#     if start==end:
#         return start if arr[start] == item else -1
#     print("yo")
#     res=-1
    
#     # go till <=end as this condition of start==end we avoid
#     while start <= end:
#         mid = (end-start)//2 + start
#         if arr[mid] == item:
#             start = mid+1
#             res=mid # store occurence and move forward
#         elif arr[mid] > item:
#             end = mid-1
#         else:
#             start=mid+1
    
#     return res

# https://leetcode.com/problems/most-profit-assigning-work/solution/
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
        


# arr = [2,2,2]
# print(bs_max_occurence(arr=arr, item=2))
# item=5
# print(bs(arr=arr, item=item))
# item=7

# print(bs(arr=arr, item=item))

# instead of bs and zip elements, we store the max profit we can make at a given difficulty
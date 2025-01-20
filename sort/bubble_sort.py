'''
idea of bubble sort is to have an array [7,3,2,5,1,8] and continously sort it in each iteration where the last ieration leads to array being 
completely sorted. It takes O(n^2) max/avg. 

It is a comparison based sorting method which where you put the largest element to it's correct location while swapping
so the largest element is at the end.

Swaps are done if two elements are not correctly placed relative to each other
'''


nums = [7,8,3,5,4,2,1]

# how i sort in my mind 😏
def bruteSort(nums:list) ->list:
  if len(nums)<2:
  return nums
  
  for i in range(0,len(nums)):
  for j in range(i+1,len(nums)):
    if nums[i] > nums[j]:
    temp =nums[i]
    nums[i]=nums[j]
    nums[j]=temp
  return nums



def bubbleSort(nums:list)->list:
  if len(nums)<2:
  return nums
  
  n=len(nums)

# the reason we go from n-1 to 0 instead of small steps is we can see if the larger thing is laready sorted or not
  for i in range(n-1,-1,-1): # -1 end to reach 0, step=-1 for reverse
  for j in range(0, i):
    if nums[j] > nums[j+1]:
    temp = nums[j]
    nums[j]=nums[j+1]
    nums[j+1]=temp
  
  return nums

def optBubbleSort(nums:list)->list:
  if len(nums)<2:
  return nums

  n = len(nums)
  didSwap=False
  
  for i in range(n-1,-1,-1):
  for j in range(0,i):
    # put the largest element at end and relative sort the array in each iteration
    if nums[j] > nums[j+1]:
    temp = nums[j]
    nums[j] = nums[j+1]
    nums[j+1]=temp
    didSwap=True
    
  if didSwap==False:
    return nums # the nums is already sorted
  return nums
  
  
res = optBubbleSort(nums)
print(res)
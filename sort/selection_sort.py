'''
here we place the minimum element at the initial position in each iteration make the array at a point in 2 parts - sorted and unsorted
'''

def selectionSort(nums:list)->list:
  n = len(nums)
  
  if len(nums)<2:
  return nums
  
  for i in range(0,n):
  idx=i
  for j in range(i+1,n):
    # keep finding the smallest element to swap to
    if nums[j]<nums[idx]:
    idx=j  
    
  if idx!=i:
    # swap nums[i] and nums[j]
    tmp = nums[i]
    nums[i]=nums[idx]
    nums[idx]=tmp  
    
  return nums  
nums = [7,8,3,5,4,2,1]
ans = selectionSort(nums=
        nums)
print(ans)

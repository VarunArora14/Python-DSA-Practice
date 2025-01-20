nums = [0,1,2,3,45,23]
target=23

def twoSum(nums: list[int], target: int):
   n = len(nums)
   
   for i in range(0,n):
   for j in range(i+1,n):
     if nums[i]+nums[j] == target:
     return [i,j]
   
def set_ans(nums: list[int], target:int):
  n = len(nums)
  
  s = dict()
  
  for i in range(0,n):
  rem = target - nums[i]
  if rem in s.keys():
    return [i, s[rem]]
  
  s[nums[i]]=i # store the element as key and value as the index

print(set_ans(nums=nums, target=target))
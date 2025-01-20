def foursum(nums: list[int], target: int) -> list[int]:
  nums.sort()
  res = []
  for i in range(len(nums)):
  for j in range(i+1, len(nums)):
    for k in range(j+1, len(nums)):    
    if nums[i] + nums[k] + nums[j] > target:
      break
    for l in range(k+1, len(nums)):
      if nums[i] + nums[j] + nums[k] + nums[l] > target:
      break # sorted array, no point going forward
      if nums[i] + nums[j] + nums[k] + nums[l] == target:
      arr= [nums[i], nums[j], nums[k], nums[l]]
      if arr not in res:
        res.append(arr)
   
  print(res)
  return res 
      


foursum([2,2,2,2,2],8)
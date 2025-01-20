def bs(nums: list, item:int) -> int:
  start:int=0
  end=len(nums)-1
  
  while(start<end):
    mid:int = int(start + (end-start)/2)
    
    if nums[mid] == item:
      return mid
    elif nums[mid] > item:
      end=mid-1
    else:
      start=mid+1
  
  return -1

def main():
  nums = [1,11,23,44,67,102,420]
  item=45
  print(bs(nums=nums, item=item))

main()
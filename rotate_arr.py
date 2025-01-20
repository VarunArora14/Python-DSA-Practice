

# Time O(n) and Space O(n)
def rotatev1():
  nums = [1,2,3,4,5,6]
  sz=  len(nums)
  shift = int(input("enter the shift amount"))
  shift = shift%sz
  
  # move the array right to left shift
  second_half = nums[:shift]
  first_half = nums[shift:]
  nums = first_half + second_half
  print(nums)

def rotatev2():
  nums = [1,2,3,4,5,6]
  shift = int(input("enter the shift: "))
  sz = len(nums)
  shift = shift % sz

  # rotate the array from 0 to shift
  for i in range(0, int(shift/2)):
  # print(f"nums[shift-i]: {nums[shift-i]}")
  temp = nums[i]
  nums[i] = nums[shift-i-1]
  nums[shift-i-1]=temp
  
  print(nums)
  
  # rotate the other half
  for i in range(shift, shift + int(sz/2)):
  temp = nums[i]
  nums[i] = nums[sz-i-1]
  nums[sz-i-1] = temp
  print(nums)
  
  
rotatev2()

def isPalindrome(x: int):
  if x<0:
  return False
  
  str_num = str(x) # O(x digit count)
  if str_num == str_num[::-1]:
  return True
  return False
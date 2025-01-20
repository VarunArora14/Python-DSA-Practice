def func(s:str):
  
  allowed = '1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
  old_s=''
  for ch in s:
  if ch!=' ' and ch in allowed:
    old_s+=ch
    
  old_s = old_s.lower()
  
  checkPalindrome(old_s)
  
def checkPalindrome(s:str):
  print(s[::-1])
  return s == s[::-1]

func("A yo")
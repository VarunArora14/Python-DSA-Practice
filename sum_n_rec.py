
def sum_rec(n:int):
  if n==0:
  return n
  
  return n + sum_rec(n-1)
  
n = input("enter count")
print(sum_rec(5))
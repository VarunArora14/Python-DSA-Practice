class Solution:
  
  # Time O(n^2) and Space O(n)
  def numIdenticalPairs(self, nums: list[int]):
    goodPairs=0
    n = len(nums)
    for i in range(n):
      for j in range(0,i):
        if nums[i]==nums[j]:
          goodPairs+=1
    return goodPairs

  # Time O(n) and Space O(n)
  def dictionarySolution(self, nums:list[int]):
    goodPairs=0
    ref = {} # here we store the past items and when same encountered then add 1 to current value, later take sum of all values in dict
    for i in range(len(nums)):
      ref[nums[i]] = 1+ref.get(nums[i], 0) # set nums[i] as it is unique for pairs, also use .get() with default value 0 if it doesnt exist
    for key,val in ref.items():
      if val > 1:
        goodPairs+=(val*(val-1))//2 # if 1 comes 4 times then {1: 3} and so pairs = 4*(4-1)//2 floor => 6
    return goodPairs
  
  def simpleDictSolution(nums:list[int]):
    goodPairs=0
    d = {}
    for num in nums:
      if num in d:
        # do something
        goodPairs+=d[num] # add previous occurences
        d[num]+=1
      else:
        d[num]=1
    
    
s = Solution()
nums = [1,1,1,1]
res=s.dictionarySolution(nums)
print(res)
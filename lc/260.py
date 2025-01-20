'''
here given a list of numbers, we have to find 2 numbers who are not in pairs while others are in pairs. We have to use constant space and linear time.

[2,4,5,2] => [4,5]

We could have sorted it and check occurences of nums[i] and nums[i+1] using nlogn time

We could have used map to store occurences and then O(n) space but can't do, so we will use bitwise operations only.

We know for a fact that end result will be - n1 xor n2
This cannot be 0 as that would mean both numbers are same. It will have at least 1 set bit and that will help to identify the number
'''


def solution(nums:list[int]):
    
    xor = nums[0]
    for i in range(1, len(nums)):
        xor = xor ^ nums[i]
    
    # this xor is n1^n2
    print(xor)
    
    pos=0
    flag=False
    while xor and flag!=True:
        print(xor)
        if xor &1:
            flag=True
        else:
            xor = xor>>1 # go one bit right
            pos+=1 # position from right
    
    print(f"pos: {pos}")
    
    # find all nums which have same set bit to true and take their xor. Since all nums would be pair except in in this case(as other number would not have same 
    # set bit as per the condition), we will get this number
    
    n1,n2=-1,-1
    for num in nums:
        # check set bit at pos
        if num>>pos & 1:
            n1 = n1^num
        else:
            n2 = n2^num
    
    n1 = n1^-1
    n2 = n2^-1
    
    print(n1,n2)

solution([-1,0])

# [2,2,3,4]

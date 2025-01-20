nums = [14,12,14,14,12,14,14,12,12,12,12,14,14,12,14,14,14,12,12]

def Solution(nums:list[int]):
    mapper = {}
    for num in nums:
        if num not in mapper:
            mapper[num]=1
        else:
            mapper[num]+=1
    
    print(mapper)
    res=0
    for key,val in mapper.items():
        if val==1:
            return -1
        elif val%3==0:
            res+=int(val/3)
        elif val%3==2:
            res+=1 + (val-2)/3
        else:
            # val%3==1
            res+=2 + (val-4)/3 # here val >=4 and if we remove 4 from val where val%3==1 we get multiple of 3
    return int(res)

print(Solution(nums=nums))
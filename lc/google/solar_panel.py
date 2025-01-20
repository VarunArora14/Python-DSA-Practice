res = []
def solution(area):
    if area<0:
        return solution(-area)
    elif area==0:
        return
    
    elif area==1:
        res.append(1)
        return

    root_ele = int(pow(area, 0.5)) 
    res.append(pow(root_ele,2))
    solution(area - pow(root_ele,2))

def solution2(area):
    res=[]
    while area>0:
        if area==1:
            res.append(1)
            return res
        else:
            root_ele = int(pow(area, 0.5)) 
            res.append(pow(root_ele,2))
            area = area - pow(root_ele,2)
    return res

print(solution2(12))
print(solution2(15324))


# find the largest square and call the function for remaining
# 12 -> 9 as largest, append to res, then solution(3) and so on..
# problem -> find the largest square <= number

num =3

res= int(pow(num, 0.5))
print(res)
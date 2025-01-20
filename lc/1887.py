import heapq
nums = [1,1,2,2,3]

tdict = {}

for n in nums:
    if n in tdict:
        tdict[n]+=1
    else:
        tdict[n]=1

q = []

for key, val in tdict.items():
    heapq.heappush(q, (-key,val))

counter=0
while len(q)>1:
    (tkey, tval) = heapq.heappop(q)
    (slKey, slVal) = heapq.heappop(q)
    
    slVal+=tval
    counter+=tval
    heapq.heappush(q, (slKey, slVal))
    
print(q)
print(counter)


# steps - find the largest ele
# find the second largest, set largest = secondLargest
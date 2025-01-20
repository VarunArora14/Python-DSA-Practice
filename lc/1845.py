import heapq

q=[]

heapq.heappush(q,1)
heapq.heappush(q,4)
heapq.heappush(q,3)
heapq.heappush(q,2)

pop = heapq.heappop(q)
print(pop)
pop = heapq.heappop(q)
print(pop)
heapq.heappush(q,1)
pop = heapq.heappop(q)
print(pop)
print(q)

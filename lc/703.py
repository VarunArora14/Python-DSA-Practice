import heapq

q = []

def add(val):
    heapq.heappush(val)

q = [4,3,8,5,7, 2]

heapq.heapify(q)
print(q)
k=3

while len(q)>k:
    heapq.heappop(q)

kth_element = heapq.heappop(q)
print(kth_element)
heapq.heappush(q,kth_element)


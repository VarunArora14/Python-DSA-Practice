import heapq
from typing import List

q = []
k=2
nums = [1,2,3,4]

q = nums

heapq.heapify(q)

while len(q) > k:
    heapq.heappop(q)

print(q[0])

heapq.heappush(q,7)


# class KthLargest:

#     def __init__(self, k: int, nums: List[int]):

#         self.q = nums
#         heapq.heapify(self.q)
#         while len(q)

#         # here we know that k is fixed, so what we can do is we maintain heap of size k which contains
#         # k elements and for each new element added, we pop the smallest elements till heap of size k

#     def add(self, val: int) -> int:
        

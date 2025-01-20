# https://neetcode.io/problems/k-closest-points-to-origin

import heapq
from math import sqrt

k=3

points = [
    [1,2],
    [4,5],
    [6,6],
    [3,3],
    [5,7],
    [1,1]
]

def k_closest(points, k):
    q = []
    for i,p in enumerate(points):
        dist = sqrt(p[0]**2 + p[1]**2)
        heapq.heappush(q, (-dist, i))
        if len(q)> k:
            heapq.heappop(q)
    
    print(q)
k_closest(points,k)
import heapq
def solution():
    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 4
    n = len(hand)
    
    
    if n%groupSize!=0:
        return False
    
    q = []
    for h in hand:
        heapq.heappush(q,h)
    i=0
    while i<n and len(q):
        top = heapq.h
import heapq

from sortedcontainers import SortedList


class MedianFinder:
    def __init__(self):
        self.arr = SortedList()
        self.min_heap = []  # stores larger elements in ascending order
        self.max_heap = []  # stores smaller elements in descending order

    def addNumSortedList(self, num: int) -> None:
        self.arr.add(num)

    def findMedianSortedList(self) -> float:
        print(self.arr._lists)
        n = self.arr._len
        if n < 2:
            return 0
        elif n % 2 != 0:
            return self.arr[n // 2]
        else:
            return (self.arr[n // 2] + self.arr[n // 2 - 1]) / 2

    def addNum(self, num: int) -> None:
        if not self.max_heap or num < -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)

        if len(self.max_heap) < len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        elif len(self.max_heap) - len(self.min_heap) > 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        return -self.max_heap[0]


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(2)
obj.addNum(3)
obj.addNum(4)

param_2 = obj.findMedian()
print(param_2)


"""
We maintain 2 heaps, one containing descending order of half the elements(THE SMALLER HALF) and 2nd heap maintaining ascending order of 2nd half(larger one).

We then see if they both have same length then take their top elements and return avg, if diff if 1 then take the larger len pop() element
"""

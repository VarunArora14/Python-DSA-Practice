import bisect
from collections import deque
from typing import List

from sortedcontainers import SortedList


class Router:
    def __init__(self, memoryLimit: int):
        self.packet_set = set()  # for checking duplicated
        self.memory_limit = memoryLimit  # upper bound
        self.fifo_queue = deque()
        self.timestamps_of_dest = dict()

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if (source, destination, timestamp) in self.packet_set:
            return False  # duplicate

        if destination not in self.timestamps_of_dest:
            self.timestamps_of_dest[destination] = SortedList()
            # store the timestamps of dest sorted for getCount() fast retrieval

        if len(self.packet_set) == self.memory_limit:
            (old_source, old_destination, old_timestamp) = self.fifo_queue.popleft()  # O(1) operation due to deque
            self.packet_set.remove((old_source, old_destination, old_timestamp))  # O(1) time
            self.timestamps_of_dest[old_destination].discard(
                old_timestamp
            )  # binary search + element removal => O(logn) operation
            # above line removes the old timestamp via implementing bisect_left internally on SortedList with old_timestamp to find and then removing the element

        self.packet_set.add((source, destination, timestamp))
        self.fifo_queue.append((source, destination, timestamp))
        self.timestamps_of_dest[destination].add(timestamp)  # O(logn) time to add and maintain sorted order
        return True

    def forwardPacket(self) -> List[int]:
        if len(self.fifo_queue):
            (src, dest, timestamp) = self.fifo_queue.popleft()
            self.packet_set.remove((src, dest, timestamp))

            # discard the element from the timestamps as well
            self.timestamps_of_dest[dest].discard(timestamp)

            return (src, dest, timestamp)

        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.timestamps_of_dest:
            return 0
        # to find this in max nlogn space, we maintain a data structure with algo
        # where we find the indices meeting timestamp>=startTime and timeStamp<=endTime with sorted times
        # and then return end_idx - start_idx+1 as the result

        # finds the first idx where startTime can be inserted so we can find lower bound index of timestamps after which next indices
        # have self.timestamps_of_dest[destination][next_idx] have values bigger than startTime

        left = self.timestamps_of_dest[destination].bisect_left(startTime)
        # both 'left', 'right' have O(logn) time as this does binary search for lower and upper bounds and is named bisect_left() for lower bound index
        # and bisect_right() for upper bound index of the value passed as parameter 'startTime' to find where this would have been inserted in less
        # time as we don't want this to be O(n) operation due to constraints

        # Similarly, we do bisect_right which is binary search on sorted array self.timestamps_of_dest[destination] to find the index 'right' where new element
        # with time bigger than endTime can be added. We use these 2 values of indices and consider count as 'right-left' as 'left' would be the correct idx
        # of first element falling in the startTime and 'right' would correct position of end plus 1 position, so 'right-end' should be the count
        right = self.timestamps_of_dest[destination].bisect_right(endTime)

        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


"""
For addPacket() => first check whether duplicate exists 
    => yes then return False, no then check memory full
        => yes, pop the oldest timestamp, no then add to the data structure
        

If getCount() was not there, we simply needed a FIFO queue (deque) and a set to store the objects (source, destination, timestamp) which is hashable
to be put in set.

Since we wanted to do getCount() in less than O(n) time as n=10^5 and it would have led to TLE had we done O(n) time, we maintain another datastructure
where for each destination, we maintain sorted list of times and update their values in addPacket() and forwardPacket()

Now, in the getCount(), we consider the startTime and endTime as potential values to put in this array for a 'destination' and find the exact indices where
they should be put so that we can use these indices to find the number of elements between them as the count of elements with same destination and being
inclusive of range [startTime, endTime] 

"""

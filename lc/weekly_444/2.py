import bisect
from collections import deque
from typing import List


# use bisect for simpler find in array
class Router:
    def __init__(self, memoryLimit: int):
        self.pack_set = set()
        self.memory_limit = memoryLimit
        self.time_stamps = dict()
        self.pack_queue = deque()  # FIFO

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        key = (source, destination, timestamp)
        if key in self.pack_set:
            return False

        # Initialize the destination in time_stamps if it doesn't exist
        if destination not in self.time_stamps:
            self.time_stamps[destination] = []

        # route full
        if len(self.pack_queue) == self.memory_limit:
            old_src, old_dst, old_time = self.pack_queue.popleft()
            self.pack_set.remove((old_src, old_dst, old_time))
            # returns index in sorted list
            idx = bisect.bisect_left(self.time_stamps[old_dst], old_time)
            if idx >= 0 and idx < len(self.time_stamps[old_dst]) and self.time_stamps[old_dst][idx] == old_time:
                self.time_stamps[old_dst].pop(idx)

        # Add the new packet
        self.pack_queue.append(key)
        self.pack_set.add(key)
        bisect.insort(self.time_stamps[destination], timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.pack_queue:
            return []

        source, destination, timestamp = self.pack_queue.popleft()
        self.pack_set.remove((source, destination, timestamp))

        idx = bisect.bisect_left(self.time_stamps[destination], timestamp)
        if idx >= 0 and idx < len(self.time_stamps[destination]) and self.time_stamps[destination][idx] == timestamp:
            self.time_stamps[destination].pop(idx)

        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.time_stamps:
            return 0

        timestamps = self.time_stamps[destination]
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)
        return right - left


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)


router = Router(3)
router.addPacket(1, 4, 90)
router.addPacket(2, 5, 90)
router.addPacket(1, 4, 90)
router.addPacket(3, 5, 95)
router.addPacket(4, 5, 105)
router.forwardPacket()
router.addPacket(5, 2, 110)
router.getCount(5, 100, 110)

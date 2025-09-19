import heapq


class TaskManager(object):
    def __init__(self, tasks):
        self.heap = []
        self.taskPriority = {}
        self.taskOwner = {}
        for t in tasks:
            self.add(t[0], t[1], t[2])

    def add(self, userId, taskId, priority):
        heapq.heappush(self.heap, (-priority, -taskId))
        self.taskPriority[taskId] = priority
        self.taskOwner[taskId] = userId

    def edit(self, taskId, newPriority):
        heapq.heappush(self.heap, (-newPriority, -taskId))
        self.taskPriority[taskId] = newPriority

    def rmv(self, taskId):
        self.taskPriority[taskId] = -1

    def execTop(self):
        while self.heap:
            negp, negid = heapq.heappop(self.heap)
            p = -negp
            tid = -negid
            if self.taskPriority.get(tid, -2) == p:
                self.taskPriority[tid] = -1
                return self.taskOwner.get(tid, -1)
        return -1


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()

"""
- The heap is used with "lazy updates": add/edit push a new tuple (-priority, -taskId) but don't remove old heap entries immediately.
- edit() does two things: pushes the new (-newPriority, -taskId) into the heap and updates taskPriority[taskId] = newPriority.
- execTop() pops entries from the heap until it finds one that matches the current priority in taskPriority:
  - it reads p = -negp and tid = -negid,
  - then checks if self.taskPriority.get(tid, -2) == p.
  - If they match, that heap entry is the current valid top task; execTop marks it removed (sets priority to -1) and returns the owner.
  - If they don’t match, the entry is stale (an older priority or a removed task) and execTop skips it and continues popping.
- Because edit updates the authoritative taskPriority map, the new heap entry will eventually be recognized as the valid one when execTop reaches it. Old entries are ignored by the equality check.
- This pattern (push-on-update + map check on pop) avoids costly arbitrary removals from the heap; the trade-off is that stale entries stay in the heap until popped.
"""

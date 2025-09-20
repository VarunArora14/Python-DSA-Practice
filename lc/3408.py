import heapq


class TaskManager(object):
    def __init__(self, tasks):
        self.heap = []
        self.task_to_priority = {}
        self.task_to_userId = {}
        for [u, t, p] in tasks:
            self.add(u, t, p)

    def add(self, userId, taskId, priority):
        heapq.heappush(self.heap, (-priority, -taskId))
        self.task_to_priority[taskId] = priority
        self.task_to_userId[taskId] = userId

    def edit(self, taskId, newPriority):
        self.task_to_priority[taskId] = newPriority
        heapq.heappush(self.heap, (-newPriority, -taskId))  # add new element

    def rmv(self, taskId):
        self.task_to_priority[taskId] = -1  # soft delete
        self.task_to_userId[taskId] = -1

    def execTop(self):
        # loop run untils the task -> priority does not have same priority as per heap negative val
        # since we change the priority in edit and added element, it will return userId only when
        # same priority in heap for a taskId as per map
        while self.heap:
            (negative_priority, negative_taskId) = heapq.heappop(self.heap)
            priority = -negative_priority
            taskId = -negative_taskId

            if self.task_to_priority[taskId] == priority:
                # execute the task
                self.task_to_priority[taskId] = -1

                # return userId for this task
                return self.task_to_userId[taskId]

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

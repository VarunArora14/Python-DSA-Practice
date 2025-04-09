import heapq


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.q = []

    def get(self, key: int) -> int:
        if key in self.cache:
            return self.cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        pass


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
In the LRU cache, we store the operations done on the key, whether put/get for determining
if it was least recently used or not, we change the operations+=1 for any get/put
"""

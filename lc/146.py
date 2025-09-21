class Node:
    def __init__(self, key, val) -> None:
        self.val = val
        self.key = key
        self.next: Node | None = None
        self.prev: Node | None = None


class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __remove_node(self, node):
        prev = node.prev
        nex = node.next
        prev.next = nex
        nex.prev = prev

    def __add_to_tail(self, node):
        tail_prev = self.tail.prev
        tail_prev.next = node
        node.prev = tail_prev
        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            # Update DLL logic
            node = self.cache[key]
            self.__remove_node(node)
            self.__add_to_tail(node)

            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            # remove this node between it's parents and set this to before tail
            self.__remove_node(node)
            self.__add_to_tail(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.__add_to_tail(node)

        # Deletion logic for overflow
        if len(self.cache.keys()) > self.capacity:
            node_to_remove = self.head.next
            self.__remove_node(node_to_remove)
            del self.cache[node_to_remove.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

"""
Why need DLL here?

We can see we need mapping/dict as this is a cache implementation. The thing we need to focus is mainly about maintaining
the order of the cache for LRU.

For this, consider a existing flow like [1,2,3,4] where if we make put/get request for key 3 then ideally the cache
should become [1,2,4,3]. Now, we cannot just copy this node value to end and later reduce the size as duplicates of 3
would be there. For this, we have ordering such that this node is removed from this list and comes to end leading to 
DLL solution.

For each node, we need to add it to end so maintaing tail is needed.
When overflow, we remove the node from start so head is important here as well

bugs to avoid:
- not have key stored inside node as deleting key from cache needs it
- not have head and tail pointers initialized to each other
- have common and same code without methods leading to missing logic in repeated code (create remove_node and add_to_tail)
helper methods for this
- review the logic again and consider empty lists and single node lists for edge cases
"""

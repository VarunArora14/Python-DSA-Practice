class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def printListNodes(node: ListNode | None):
    res = []
    while node:
        res.append(node.val)
        node = node.next

    print(" ".join(str(x) for x in res))


def createNode():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = ListNode(1)
    curr = head
    for num in nums[1:]:
        curr.next = ListNode(num)
        curr = curr.next

    return head


n = createNode()
printListNodes(n)


def splitToParts(node, k=3):
    curr = node
    sz = 0
    while curr:
        curr = curr.next
        sz += 1

    base_len = sz // k
    rem_len = sz % k

    print(base_len, rem_len)

    curr = node
    final_arr = []

    for _ in range(k):
        temp = curr
        for j in range(base_len + (rem_len > 0) - 1):
            curr = curr.next

        if curr:
            x = curr.next
            curr.next = None
            curr = x  # get the next value of listnode
        final_arr.append(temp)

        rem_len -= 1

    for f in final_arr:
        printListNodes(f)


splitToParts(n)

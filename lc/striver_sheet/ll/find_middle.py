from typing import List


class Node:
    def __init__(self, val) -> None:
        self.next: Node | None = None
        self.val = val


def print_ll(head: Node | None):
    print("Printing list:")
    tmp = head
    while tmp:
        print(tmp.val, end=" ")
        tmp = tmp.next
    print("\n")


def populate_ll(arr: List[int]) -> Node | None:
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    tmp = head
    for i in range(1, len(arr)):
        print(arr[i])
        node = Node(arr[i])
        tmp.next = node
        tmp = node

    tmp.next = None
    return head


def find_middle(head: Node | None):
    if head is None:
        return None

    fast = head
    slow = head

    while fast and fast.next and slow:
        fast = fast.next.next
        slow = slow.next
    return slow


arr = [1, 3, 2, 4, 5, 6, 7]
head = populate_ll(arr)
if head is not None:
    print_ll(head)

node = find_middle(head)
if node is not None:
    print("middle node value", node.val)
# print_ll(head)


"""
Understanding the need for fast pointer and fast.next

If we have 5 element list then fast pointer goes to 5th element when slow pointer is at 3rd element. This is where we use fast.next check as well as for [1,2,3,4,5]
if fast is at 5, then fast.next does not exist and we want to stop there and return the slow pointer.

The reason we do not check for fast.next.next is because for even lengths lists => [1,2,3,4,5,6], when fast is at 5, then slow is at 3. Now, as per ques, we want the 
2nd occurence for even list nodes, for this having a check for fast.next.next would stop otherwise and slow=3 will be returned but the answer should be 4. So we move
fast to pointer Null after 6 and make slow come at 4.

"""

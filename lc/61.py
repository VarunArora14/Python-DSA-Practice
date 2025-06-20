from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # base case of empty list
        if head is None:
            return head

        # find length of list to reach n-k position
        n = 0
        tmp = head
        while tmp:
            tmp = tmp.next
            n += 1

        # take mod if k>n
        k = k % n
        t = head

        # reach n-kth position
        for _ in range(n - k - 1):
            t = t.next

        # mark new head as next element of n-k+1 position
        new_head: ListNode = t.next
        t.next = None  # mark tail of n-kth node

        # edge case
        if new_head is None:
            return head

        dummy = new_head

        # take the chopped list from new_head and make the last element point to head
        while dummy.next:
            dummy = dummy.next
        dummy.next = head

        return new_head

    def traverse(self, head: ListNode):
        tmp = head
        while tmp:
            print(tmp.val, end=" ")
            tmp = tmp.next


h = ListNode(1)
h.next = ListNode(2)
h.next.next = ListNode(3)
h.next.next.next = ListNode(4)
h.next.next.next.next = ListNode(5)
sol = Solution()
sol.traverse(h)
print()
new_h = sol.rotateRight(h, 2)
sol.traverse(new_h)

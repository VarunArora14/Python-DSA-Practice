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


def reverse_ll(head: Node | None):
    if head is None:
        return None

    prev = None
    curr = head
    nex = head.next

    while curr:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex

    return prev


arr = [1, 3, 2, 4]
head = populate_ll(arr)
if head is not None:
    print_ll(head)

head = reverse_ll(head)
print_ll(head)

"""
For 1->3->2->4

when we had the below logic - 

    while nex:
        curr.next = prev
        prev = curr
        curr = nex
        nex = nex.next

    return curr
    
The problem was that when nex=None, then list was - N<-1<-3<-2(prev)-> 4(curr)->N(nex)

This return incorrect list as 4 is where curr is at and the returned list will be 4->N

what we want is one more iteration of the loop to become N<-1<-3<-2<-4(prev)<-N(curr)->N(nex)

and then you should return prev as the result


"""

class Node:
    def __init__(self, val) -> None:
        self.next = None
        self.val = val


class LinkedList:

    def __init__(self) -> None:
        self._head = None

    def traverse(self):
        h = self._head
        while h is not None:
            print(h.val)
            h = h.next

    def insertAtHead(self,data:int):
        node = Node(data)
        if self._head is None:
            self._head=node
        else:
            node.next = self._head
            self._head=node
    
    def insertAtEnd(self, data:int):
        node = Node(data)
        if self._head is None:
            self._head = node
            return
        
        h = self._head
        while h.next is not None:
            h = h.next
        
        h.next = node
    
    def removeAtHead(self):
        if self._head is None:
            return
        h = self._head
        self._head = self._head.next
        del h

    def removeAtEnd(self):
        if self._head is None:
            print("Empty list!")
            return
        
        h= self._head
    
    def findLengthLL(self):
        h = self._head
        length=0
        while h is not None:
            length+=1
            h = h.next
        return length
    
    def insertAtIndex(self,idx:int, val: int): 
        length = self.findLengthLL()
        
        # handle case for incorrect length
        if idx<0 or idx >= length:
            print("Item cannot be inserted due to invalid index")
            return
        
        # base case
        if idx==0:
            self.insertAtHead(val)
            
        counter=0
        h= self._head
        
        while counter < idx-1:
            h = h.next
            counter+=1
        
        node = Node(val)
        temp = h.next
        h.next = node
        node.next=temp
        
    
l = LinkedList()
l.insertAtEnd(5)
l.insertAtEnd(2)
l.insertAtEnd(3)
l.insertAtEnd(4)
l.insertAtIndex(idx=2, val=10)
l.traverse()
print()
l.removeAtHead()
l.traverse()
mapper = {}

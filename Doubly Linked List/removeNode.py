class Node:
    def __init__(self,  data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    
class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def insert(self, data):
        newNode = Node(data)
        head = self.head
        
        if head is None:
            self.head = newNode
            self.tail = newNode
            return
        
        newNode.next = head
        head.prev = newNode
        self.head = newNode
        return
    
    def printList(self):
        head = self.head
        if head is None:
            return
        while head:
            print(f"{head.data} -> ", end='')
            head = head.next
    
    def removeNodeFirst(self):
        head = self.head
        if head is None:
            return
        
        self.head = head.next
        head.next.prev = None
        del head
        return
    
    def removeNodeLast(self):
        tail = self.tail
        if tail is None:
            return
        
        self.tail = tail.prev
        tail.prev.next = None
        del tail
        return
        

    # Remove node by given value from a doubly linked list
    def removeNodeByValue(self, value):
        head = self.head
        if head is None:
            return
        
        # if value is first node data
        if value == head.data:
            self.head = head.next
            
            if head.next: # if list has single node
                head.next.prev = None
            del head
            return
        
        # if value is last node data
        if value == self.tail.data:
            tail = self.tail
            self.tail = tail.prev
            self.tail.next = None
            del tail
            return
        
        while head:
            if head.data == value:
                temp = head
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del temp
            head = head.next
        return


if __name__ == '__main__':
    llist = DoublyLinkedList()
    llist.insert(10)
    llist.insert(9)
    llist.insert(8)
    llist.insert(8)
    llist.insert(7)
    llist.insert(6)
    llist.insert(5)
    
    print('Head data: ',llist.head.data)
    print('Tail data', llist.tail.data)
    
    print(llist.printList())
    llist.removeNodeFirst()
    print(llist.printList())
    
    llist.removeNodeLast()
    print(llist.printList())
    
    llist.removeNodeByValue(6)
    llist.removeNodeByValue(8)
    llist.removeNodeByValue(7)
    llist.removeNodeByValue(9)
    print(llist.printList())
    